import numpy as np
import pandas as pd
import streamlit as st
import pydeck as pdk
import plotly.express as px

emoji = ':airplane_arriving::cloud::airplane_departure::cloud::airplane_arriving:'
title = 'My Last Flight'
st.logo(st.session_state['logo_img'])
st.set_page_config(page_title=title,
                   page_icon=emoji,
                   layout='wide',
                   )
st.header(f'{title} {emoji}', divider='rainbow')

from Kapoot import sb_scores
sb_scores()

# @st.cache_data
def calculate():
    df = st.session_state['df_data']
    country_coord = st.session_state['country_coord']
    israel_coord = country_coord.get('ישראל', 0)

    df_weekend = df['דרכון']
    from collections import Counter
    item_counts = Counter(df_weekend)
    # st.write(item_counts)

    # Print the item counts
    items = []
    counts = []
    coords = []
    lats = []
    lons = []
    il_lats = []
    il_lons = []

    passport_coord = st.session_state['passport_coord']

    for item, count in item_counts.items():
        # print(f"{item}: {count}")
        if item == 'ללא':
            coord = israel_coord
        else:
            coord = passport_coord.get(item, 0)
        items.append(item)
        counts.append(count)
        coords.append(coord)
        lats.append(coord[0])
        lons.append(coord[1])
        il_lats.append(israel_coord[0])
        il_lons.append(israel_coord[1])

    weekend_dic = {
        'country': items,
        'counts': counts,
        'coords': coords,
        'lats': lats,
        'lons': lons,
        'il_lats': il_lats,
        'il_lons': il_lons,
    }
    df_chart = pd.DataFrame(weekend_dic)
    # st.write(df_chart)
    df_chart = df_chart.sort_values(by='counts', ascending=False)
    # st.write(df_chart)

    return df_chart


df_chart = calculate()

with st.container():
    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')

        with st.expander(f'Weekends Map :'):

            df_map = pd.DataFrame()
            df_map['lat'] = df_chart['lats']
            df_map['lon'] = df_chart['lons']
            st.map(df_map, size=2000, color='#0044ff')

        with st.expander(f'Question :'):
            st.subheader('? לאן כולנו טסנו בפעם האחרונה הכי הרבה')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':blue[הודו]')
                with col2:
                    st.header(':green[אוסטריה]')
                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[יוון]')
                with col4:
                    st.header(':orange[מונטנגרו]')

    with col02:
        st.header('A')

        with st.expander(f'Map :'):

            country_coord = st.session_state['country_coord']
            israel_coord = country_coord.get('ישראל', 0)

            df_map = df_chart.iloc[0:1]
            # st.write(df_map)
            st.pydeck_chart(pdk.Deck(
                map_style="mapbox://styles/mapbox/streets-v11",  # Street map style
                initial_view_state=pdk.ViewState(
                    latitude=israel_coord[0],
                    longitude=israel_coord[1],
                    zoom=6,
                    pitch=0,
                ),
                layers=[
                    pdk.Layer(
                        "GreatCircleLayer",
                        data=df_map,
                        get_source_position='[il_lons, il_lats]',
                        get_target_position='[lons, lats]',
                        get_source_color=[20, 0, 250, 160],
                        get_target_color=[200, 30, 0, 160],
                        pickable=True,
                        getWidth=5,
                        getTooltip={"text": "{private} to {home}"},  # Tooltip
                    ),
                ],

            ))

        with st.expander(f'Answer :'):
            st.header(':green[אוסטריה]')

            bar_df = df_chart[['country', 'counts']]
            bar_df = bar_df.sort_values(by='counts', ascending=False)
            # Create pie chart
            fig = px.bar(
                bar_df,
                title='',
                x='country',
                y='counts',
            )
            st.plotly_chart(fig)

st.header(f'', divider='rainbow')
from Kapoot import clock_run
clock_run()
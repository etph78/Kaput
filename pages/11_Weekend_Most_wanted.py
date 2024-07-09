import numpy as np
import pandas as pd
import streamlit as st
import pydeck as pdk
import plotly.express as px

emoji = ':desert_island:'
title = 'Weekend Vacation'
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

    df_weekend = df['סופש']
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

    weekend_coord = st.session_state['weekend_coord']

    for item, count in item_counts.items():
        coord = weekend_coord.get(item, 0)
        items.append(item)
        counts.append(count)
        coords.append(coord)
        lats.append(coord[0])
        lons.append(coord[1])
        il_lats.append(israel_coord[0])
        il_lons.append(israel_coord[1])

        # print(f"{item}: {count}")
    weekend_dic = {
        'city': items,
        'counts': counts,
        'coords': coords,
        'lats': lats,
        'lons': lons,
        'il_lats': il_lats,
        'il_lons': il_lons,
    }
    df_chart = pd.DataFrame(weekend_dic)
    # st.write(weekend_df)
    df_chart = df_chart.sort_values(by='counts', ascending=False)
    # st.write(df_chart)

    return df_chart


df_chart = calculate()

with st.container():
    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')

        with st.expander(f'Weekends Map :'):

            country_coord = st.session_state['country_coord']
            israel_coord = country_coord.get('ישראל', 0)

            st.pydeck_chart(pdk.Deck(
                map_style="mapbox://styles/mapbox/streets-v11",  # Street map style
                initial_view_state=pdk.ViewState(
                    latitude=israel_coord[0],
                    longitude=israel_coord[1],
                    zoom=1,
                    pitch=0,
                ),
                layers=[
                    pdk.Layer(
                        "GreatCircleLayer",
                        data=df_chart,
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

        with st.expander(f'Question :'):
            st.subheader('? לאן הכי רציתם לטוס לסופש בחול')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':blue[פריז]')
                with col2:
                    st.header(':green[רומא]')
                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[לונדון]')
                with col4:
                    st.header(':orange[לפלנד]')


    with col02:
        st.header('A')

        with st.expander(f'Map :'):
            city = list(df_chart['city'])[0]
            lat = list(df_chart['lats'])[0]
            lon = list(df_chart['lons'])[0]

            st.pydeck_chart(pdk.Deck(
                map_style="mapbox://styles/mapbox/streets-v11",  # Street map style
                initial_view_state=pdk.ViewState(
                    latitude=lat,
                    longitude=lon,
                    zoom=10,
                    pitch=0,
                ),
            ))

        with st.expander(f'Answer :'):

            st.header(':blue[פריז]')

            bar_df = df_chart[['city', 'counts']]
            bar_df = bar_df.sort_values(by='counts', ascending=False)
            # Create pie chart
            fig = px.bar(
                bar_df,
                title='',
                x='city',
                y='counts',
            )
            st.plotly_chart(fig)

st.header(f'', divider='rainbow')
from Kapoot import clock_run
clock_run()
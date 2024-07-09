import numpy as np
import pandas as pd
import streamlit as st
import pydeck as pdk
import great_circle_calculator.great_circle_calculator as gcc

emoji = ':factory:'
title = 'From Home to Netanel'
st.logo('Assets\\Pictures\\logo.jpeg')
st.set_page_config(page_title=title,
                   page_icon=emoji,
                   layout='wide',
                   )
st.header(f'{title} {emoji}', divider='rainbow')

enable_sb_menu = st.session_state['enable_sb_menu']
if enable_sb_menu:
    from Kapoot import set_sidebar_menu
    set_sidebar_menu()

from Kapoot import sb_scores
sb_scores()

# @st.cache_data
def calculate():
    df = st.session_state['df_data']

    # calc range from home to work1 & work2
    name_list = list(df['פרטי'])
    home_list = list(df['ישוב'])
    list_len = len(home_list)
    home_dic = st.session_state['home_coord']
    work_dic = st.session_state['work_coord']
    work = work_dic.get('נתנאל', 0)

    home_coord = [np.nan] * list_len
    home_lat = [np.nan] * list_len
    home_lon = [np.nan] * list_len
    work_coord = [work] * list_len
    work_lat = [work[0]] * list_len
    work_lon = [work[1]] * list_len
    home_2_work = [work] * list_len

    for i in range(list_len):
        key = home_list[i]
        value = home_dic.get(key, 0)
        if value == 0:
            home = work
        else:
            home = value

        home_coord[i] = home
        home_lat[i] = home[0]
        home_lon[i] = home[1]
        dist = gcc.distance_between_points(home, work,
                                            unit='kilometers',
                                            haversine=True)
        home_2_work[i] = dist

        # st.write(f'home: {home_coord}')
        # st.write(f'work: {work_coord}')
        # st.write(f'dist: {home_2_work}')

    dict_chart = {
        'private': name_list,
        'home': home_list,
        'home_coord': home_coord,
        'home_lat': home_lat,
        'home_lon': home_lon,
        'work_coord': work_coord,
        'work_lat': work_lat,
        'work_lon': work_lon,
        'dist': home_2_work,
    }
    df_chart = pd.DataFrame(dict_chart)
    df_chart = df_chart.sort_values(by='dist', ascending=False)

    return df_chart


df_chart = calculate()

with st.container():

    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')
        with st.expander(f'Question :'):
            st.subheader('? מי גר הכי רחוק מהמשרדים בנתנאל')
            st.subheader('(Using Great Circle Distance)')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':blue[אריק]')
                with col2:
                    st.header(':green[רומן]')
                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[אלעד]')
                with col4:
                    st.header(':orange[ליאורה]')
    with col02:
        st.header('A')

        with st.expander(f'Result :'):
            winner_df = df_chart[['private', 'home_lat', 'home_lon', 'work_lat', 'work_lon', 'dist']]
            winner_df = winner_df[0:1]

            work_dic = st.session_state['work_coord']
            work_coord = work_dic.get('נתנאל', 0)

            st.pydeck_chart(pdk.Deck(
                map_style="mapbox://styles/mapbox/streets-v11",  # Street map style
                initial_view_state=pdk.ViewState(
                    latitude=work_coord[0],
                    longitude=work_coord[1],
                    zoom=15,
                    pitch=0,
                ),
                layers=[
                    pdk.Layer(
                        "GreatCircleLayer",
                        data=df_chart,
                        get_source_position='[home_lon, home_lat]',
                        get_target_position='[work_lon, work_lat]',
                        get_source_color=[20, 0, 250, 160],
                        get_target_color=[200, 30, 0, 160],
                        pickable=True,
                        getWidth=5,
                        getTooltip={"text": "{private} to {home}"},  # Tooltip
                    ),
                    pdk.Layer(
                        "GreatCircleLayer",
                        data=winner_df,
                        # get_source_position="source",
                        # get_target_position="target",
                        get_source_position='[home_lon, home_lat]',
                        get_target_position='[work_lon, work_lat]',
                        get_source_color=[20, 250, 0],
                        get_target_color=[200, 30, 0, 160],
                        pickable=True,
                        getWidth=10,
                        getTooltip={"text": "{private} to {home}"},  # Tooltip

                    ),
                ],

            ))

        with st.expander(f'Answer :'):
            winner = list(winner_df['private'])[0]
            distance = list(winner_df['dist'])[0]
            col1, col2 = st.columns(2)
            with col1:
                st.header(f':green[{winner}]')
            with col2:
                st.header(f':green[{int(distance)}[km]]')

st.header(f'', divider='rainbow')
from Kapoot import clock_run
clock_run()

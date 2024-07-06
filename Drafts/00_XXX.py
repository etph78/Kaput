import numpy as np
import pandas as pd
import streamlit as st
import pydeck as pdk
import great_circle_calculator.great_circle_calculator as gcc

emoji = ':sparkles:'
title = 'XXX'
st.logo('Assets\\Pictures\\logo.jpeg')
st.set_page_config(page_title=title,
                   page_icon=emoji,
                   layout='wide',
                   )
st.header(f'{title} {emoji}', divider='rainbow')


def calculate():
    df = st.session_state['df_data']
    df_chart = df
    # df_chart = df_chart.sort_values(by='dist', ascending=False)

    return df_chart


st.header('Q')
with st.expander(f'Question :'):
    st.subheader('Who Has the Most Distance from Home to Netanel ?')
    st.write('(Great Circle Distance)')
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.header(':blue[XXX]')
        with col2:
            st.header(':green[YYY]')
        col3, col4 = st.columns(2)
        with col3:
            st.header(':red[WWW]')
        with col4:
            st.header(':orange[ZZZ]')

st.divider()
from Kapoot import clock_run

clock_run()

st.header('A')
df_chart = calculate()

with st.expander(f'Answer :'):
    winner_df = df_chart
    # winner_df = winner_df[['private', 'home_lat', 'home_lon', 'work_lat', 'work_lon',]]
    winner_df = winner_df[0:1]
    st.write(winner_df)

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

emoji = ':office_worker:'
title = 'Work Time'
st.logo('Assets\\Pictures\\logo.jpeg')
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
    df['mean'] = df['ותק'].mean()
    df['std'] = df['ותק'].std()
    df_chart = df
    # df_chart = df_chart.sort_values(by='ותק', ascending=True)

    return df_chart


df_chart = calculate()

with st.container():
    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')

        with st.expander(f'Graph :'):
            with st.container():
                # graph_height = 300
                # Create a histogram
                # Create a scatter plot for the first half of the data
                scatter_df = df_chart
                fig = px.scatter(scatter_df,  y='ותק', color_discrete_sequence=['red'])

                # Display the plot
                st.plotly_chart(fig, use_container_width=True)

        with st.expander(f'Question :'):
            st.subheader('הותק שלנו בחברה (בחודשים)')
            st.subheader('? מה ממוצע וסטיית התקן')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':blue[Mean:205, STD:35]')
                with col2:
                    st.header(':green[Mean:280, STD:76]')
                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[Mean:86, STD:113]')
                with col4:
                    st.header(':orange[Mean:116, STD:112]')

    with col02:
        st.header('A')

        with st.expander(f'Graph :'):
            with st.container():
                # graph_height = 300
                # Create a histogram
                # Create a scatter plot for the first half of the data
                scatter_df = df_chart
                fig = px.scatter(scatter_df,  y='ותק', color_discrete_sequence=['red'])

                # Add a line plot for the second half of the data
                line_df = df_chart
                fig.add_trace(px.line(line_df, y='mean', color_discrete_sequence=['blue']).data[0])

                # Display the plot
                st.plotly_chart(fig, use_container_width=True)

        with st.expander(f'Answer :'):

            # st.write(df_chart)
            mean = list(df_chart['mean'])[0]
            std = list(df_chart['std'])[0]
            # col1, col2 = st.columns(2)
            # with col1:
            st.header(f':orange[Mean:  {int(mean)} [months]]')
            # with col2:
            st.header(f':orange[STD   :  {int(std)} [months]]')
            st.subheader('')
            st.subheader('')

st.header(f'', divider='rainbow')
from Kapoot import clock_run
clock_run()
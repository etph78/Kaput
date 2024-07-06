import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

emoji = ':high_heel:'
title = 'Height Statistics'
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
    df['mean'] = df['גובה'].mean()
    df['diff'] = abs(df['גובה'] - df['mean'])
    df_chart = df
    df_chart = df_chart.sort_values(by='diff', ascending=True)

    return df_chart

df_chart = calculate()

with st.container():
    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')
        with st.expander(f'Question :'):
            st.subheader('? מי הכי קרוב לגובה הממוצע של כולנו')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':blue[שלי]')
                with col2:
                    st.header(':green[אורן]')
                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[מאור]')
                with col4:
                    st.header(':orange[אביחי]')

            with st.container():
                graph_height = 300
                # Create a histogram
                # Create a scatter plot for the first half of the data
                scatter_df = df_chart
                fig = px.scatter(scatter_df,  y='גובה', color_discrete_sequence=['red'])

                # Add a line plot for the second half of the data
                line_df = df_chart
                fig.add_trace(px.line(line_df, y='mean', color_discrete_sequence=['blue']).data[0])

                # Display the plot
                st.plotly_chart(fig, use_container_width=True)

    with col02:
        st.header('A')

        with st.expander(f'Answer :'):
            # st.write(df_chart)
            private = list(df_chart['פרטי'])[0]
            height = list(df_chart['גובה'])[0]
            mean = list(df_chart['mean'])[0]
            diff = list(df_chart['diff'])[0]
            col1, col2, col3, col4 = st.columns(4)
            st.header(f':green[{private}]')
            st.header(f':green[Height: {int(height)} [cm]]')
            st.header(f':green[Mean: {int(mean)} [cm]]')
            st.header(f':green[Diff: {int(diff)} [cm]]')

            # col1, col2, col3, col4 = st.columns(4)
            # with col1:
            #     st.header(f':green[{private}]')
            # with col2:
            #     st.header(f':green[Height:{int(height)}[cm]]')
            # with col3:
            #     st.header(f':green[Mean:{int(mean)}[cm]]')
            # with col4:
            #     st.header(f':green[Diff:{int(diff)}[cm]]')

st.header(f'', divider='rainbow')
from Kapoot import clock_run
clock_run()
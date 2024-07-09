import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

emoji = ':children_crossing:'
title = 'Children Distribution'
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
    df_chart = df
    df_chart = df_chart.sort_values(by='קומה', ascending=False)

    return df_chart


df_chart = calculate()

with st.container():
    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')
        with st.expander(f'Question :'):
            st.subheader(' ... מכל בתי המגורים שלנו')
            st.subheader(' ... בקומה בה יש ילדים')
            st.subheader('? באיזו קומה גרים הכי מעט ילדים')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':blue[קומת קרקע]')
                with col2:
                    st.header(':green[קומה 1]')
                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[קומה 7]')
                with col4:
                    st.header(':orange[קומה 3]')

    with col02:
        st.header('A')

        with st.expander(f'Answer :'):
            st.header(':orange[קומה 3]')

            graph_height = 300
            # Create a histogram
            # Create a scatter plot for the first half of the data
            fig = px.bar(df_chart, x='קומה', y='ילדים', color_discrete_sequence=['orange'])
            # Display the plot

            # # Add a line plot for the second half of the data
            # line_df = df_chart
            # fig.add_trace(px.line(line_df, y='mean', color_discrete_sequence=['blue']).data[0])
            st.plotly_chart(fig, use_container_width=True)


st.header(f'', divider='rainbow')
from Kapoot import clock_run
clock_run()
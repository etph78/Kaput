import numpy as np
import pandas as pd
import streamlit as st
import pydeck as pdk
import great_circle_calculator.great_circle_calculator as gcc

emoji = ':kiwifruit:'
title = 'Fruit Case'
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
    # df_chart = df_chart.sort_values(by='dist', ascending=False)

    return df_chart


df_chart = calculate()

with st.container():
    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')
        with st.expander(f'Question :'):
            st.subheader('צריך להביא פרי אחד ככיבוד')
            st.subheader('? מה הפרי הכי מבוקש')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':blue[אבטיח]:watermelon:')
                with col2:
                    st.header(':green[אננס]:pineapple:')
                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[דודבן]:cherries:')
                with col4:
                    st.header(':orange[מנגו]:mango:')

    with col02:
        st.header('A')
        with st.expander(f'Answer :'):
            st.header(':blue[אבטיח]:watermelon:')

            # Define a list of items
            df = df_chart['פרי']
            # Use Counter to count the frequency of each item
            from collections import Counter
            item_counts = Counter(df)
            # Print the item counts
            items = []
            counts = []
            for item, count in item_counts.items():
                items.append(item)
                counts.append(count)
                # print(f"{item}: {count}")
            pie_dic = {
                'items': items,
                'counts': counts,
            }
            pie_df = pd.DataFrame(pie_dic)
            pie_df = pie_df.sort_values(by='counts', ascending=False)
            pull = [0] * len(counts)
            pull[0] = 0.2

            # Display chart
            import plotly.express as px

            labels = item
            values = count
            # Create pie chart
            fig = px.pie(
                pie_df,
                title='',
                values='counts',
                names='items',
            )
            colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
            fig.update_traces(
                textposition='inside',
                textinfo='percent+label',
                insidetextorientation='radial',
                textfont_size=30,
                marker=dict(colors=colors, line=dict(color='#000000', width=2)),
                hole=.3,
                # pull=[0, 0, 0.2, 0],
                pull=pull,
            )
            st.plotly_chart(fig)

st.header(f'', divider='rainbow')
from Kapoot import clock_run
clock_run()
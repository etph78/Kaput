import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

emoji = ':baby_bottle::beer::tropical_drink::wine_glass:'
title = 'Booze Most Wanted'
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
    df_chart = df
    my_df = list(df['אלכוהול'])
    # st.write(animals_df)
    my_list = []
    for items in my_df:
        # st.write(f'items: {items}')
        if items != '-':
            items_list = items.split(',')
            for item in items_list:
                # st.write(f'item: {item}')
                my_list.append(item)
        else:
            pass
    # st.write(animals_list)
    # df_chart = df_chart.sort_values(by='dist', ascending=False)
    return df_chart, my_list


df_chart, my_list = calculate()

with st.container():
    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')
        with st.expander(f'Question :'):
            st.subheader('רוצים לשתות משהו')
            st.subheader('ושיהיה קצת יותר חזק ממים')
            st.subheader('? מה הכי כדאי להציע לכם')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':blue[בירה או כלום]')
                with col2:
                    st.header(':green[יין או כלום]')
                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[יין או בירה]')
                with col4:
                    st.header(':orange[ויסקי או בירה]')

    with col02:
        st.header('A')
        with st.expander(f'Answer :'):
            st.header(':orange[ויסקי או בירה]')

            with st.container():
                col1, col2, col3 = st.columns(3)
                with col2:
                    st.header(':sake::beers:')

            from collections import Counter
            # Define a list of items
            df = my_list
            # Use Counter to count the frequency of each item
            item_counts = Counter(df)
            # Print the item counts
            items = []
            counts = []
            pull_pie = []
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

            # Display chart
            labels = item
            values = count
            colors = ['red', 'green', 'blue', 'orange']
            fig = px.bar(pie_df, x='counts', y='items', orientation='h', color='items',
                         color_discrete_sequence=colors)
            st.plotly_chart(fig)

st.header(f'', divider='rainbow')
from Kapoot import clock_run
clock_run()

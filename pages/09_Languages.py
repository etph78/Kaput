import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

emoji = ':books:'
title = 'Lingo'
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

    lang_df = list(df['שפות'])
    # st.write(animals_df)
    lang_list = []
    for items in lang_df:
        # st.write(f'items: {items}')
        if items != '-':
            items_list = items.split(',')
            for item in items_list:
                # st.write(f'item: {item}')
                lang_list.append(item)
        else:
            pass
    # df_chart = df_chart.sort_values(by='dist', ascending=False)

    return df_chart, lang_list


df_chart, lang_list = calculate()

with st.container():
    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')
        with st.expander(f'Question :'):
            st.subheader('אנחנו מדברים 6 שפות')
            st.subheader('? מה שלוש השפות הכי נדירות')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':blue[רוסית, צרפתית, ערבית]')
                with col2:
                    st.header(':green[אוקראינית, סרבית, צרפתית]')
                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[סרבית, צרפתית, רוסית]')
                with col4:
                    st.header(':orange[צרפתית, רוסית, ערבית]')

    with col02:
        st.header('A')

        with st.expander(f'Answer :'):
            from collections import Counter
            # Define a list of items
            df = lang_list
            # Use Counter to count the frequency of each item
            item_counts = Counter(df)
            # Print the item counts
            items = []
            counts = []
            for item, count in item_counts.items():
                items.append(item)
                counts.append(count)
                # print(f"{item}: {count}")
            bar_dic = {
                'items': items,
                'counts': counts,
            }
            bar_df = pd.DataFrame(bar_dic)
            bar_df = bar_df.sort_values(by='counts', ascending=True)

            # Create pie chart
            fig = px.bar(
                bar_df,
                title='',
                x='items',
                y='counts',
            )
            # colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']
            # fig.update_traces(
            #     textposition='inside',
            #     textinfo='percent+label',
            #     insidetextorientation='radial',
            #     textfont_size=30,
            #     marker=dict(colors=colors, line=dict(color='#000000', width=2)),
            #     hole=.0,
            #     # pull=[0, 0, 0.2, 0],
            #     # pull=pull,
            # )
            st.plotly_chart(fig)

from Kapoot import clock_run
clock_run()
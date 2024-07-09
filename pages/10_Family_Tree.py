import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px


emoji = ':mrs_claus::man-cartwheeling::woman-shrugging::male_mage:'
title = 'Family Tree'
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
    country_df = list(df_chart['ארצות'])
    # st.write(country_df)
    country_list = []
    for items in country_df:
        # st.write(f'items: {items}')
        if items != '-':
            items_list = items.split(',')
            for item in items_list:
                # st.write(f'item: {item}')
                country_list.append(item)
        else:
            pass
    # df_chart = df_chart.sort_values(by='dist', ascending=False)

    return df_chart, country_list


df_chart, country_list = calculate()

with st.container():
    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')
        with st.expander(f'Question :'):
            st.subheader('... אם היה אפשר, להפגיש את המשפחות שלנו')
            st.subheader('... אמא-אבא-סבא-סבתא')
            st.subheader('... חוץ מהישראלים')
            st.subheader('? איפה נולדו רוב המשתתפים')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':blue[מרוקו]')
                with col2:
                    st.header(':green[פולין]')
                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[אוקראינה]')
                with col4:
                    st.header(':orange[רוסיה]')

    with col02:
        st.header('A')

        with st.expander(f'Answer :'):

            st.header(':red[אוקראינה]')

            from collections import Counter
            # Define a list of items
            df = country_list
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
            bar_df = bar_df[bar_df['items'] != 'ישראל']
            bar_df = bar_df.sort_values(by='counts', ascending=False)

            # Create pie chart
            fig = px.bar(
                bar_df,
                title='',
                x='items',
                y='counts',
            )

            st.plotly_chart(fig)

from Kapoot import clock_run
clock_run()
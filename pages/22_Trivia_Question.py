import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_player import st_player

emoji = ':question:'
title = 'Trivia'
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
    # df_chart = df_chart.sort_values(by='dist', ascending=False)

    return df_chart


df_chart = calculate()

with st.container():
    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')
        with st.expander(f'Fact :'):
            st.subheader('הרוב אוהבים מדע... אז שאלת מדע')

            from collections import Counter
            # Define a list of items
            trivia = df_chart['טריויה']
            # Use Counter to count the frequency of each item
            item_counts = Counter(trivia)
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
            )
            st.plotly_chart(fig)

        with st.expander(f'Question :'):
            st.subheader('? איזה חלק בגוף האדם הוא בית השחי')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':blue[מכמונת יד]')
                with col2:
                    st.header(':green[עשיריון]')
                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[בית השחי]')
                with col4:
                    st.header(':orange[תיפתורת]')

    with col02:
        st.header('A')

        with st.expander(f'Answer :'):

            st.header(':red[בית השחי]')

            from PIL import Image
            image_size = (800, 600)
            question_img = st.session_state['question_img']
            st.image(question_img['criscros'], use_column_width='always')
            # url = 'https://www.youtube.com/watch?v=010KyIQjkTk'
            # st_player(url)
            audio_urls = st.session_state['audio_urls']
            st.audio(audio_urls.get('KrisKross.mp3'), format="audio/mp3", loop=False, autoplay=True)

st.header(f'', divider='rainbow')
from Kapoot import clock_run
clock_run()

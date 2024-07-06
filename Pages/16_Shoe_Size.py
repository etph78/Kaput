import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

emoji = ':athletic_shoe:'
title = 'Shoe Size'
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

    df_men = df[df['מין'] == 'm']
    df_women = df[df['מין'] == 'f']
    df_men_size = df_men['נעל']
    df_women_size = df_women['נעל']
    # st.write(df_men_size)
    # st.write(df_women_size)

    men_shoe = st.session_state['shoe_size_to_cm_men']
    women_shoe = st.session_state['shoe_size_to_cm_women']

    shoe_len = 0

    shoe = pd.DataFrame(men_shoe)
    sizes = list(df_men['נעל'])
    for size in sizes:
        ss = shoe[shoe['size']==size]
        if len(ss) > 0:
            cm = list(ss['cm'])[0]
        else:
            cm = 0
        shoe_len = shoe_len + (cm * 1)

    shoe = pd.DataFrame(women_shoe)
    sizes = list(df_men['נעל'])
    for size in sizes:
        ss = shoe[shoe['size']==size]
        if len(ss) > 0:
            cm = list(ss['cm'])[0]
        else:
            cm = 0
        shoe_len = shoe_len + (cm * 1)

    return df_chart, shoe_len


df_chart, shoe_len = calculate()

with st.container():
    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')
        with st.expander(f'Question :'):
            from PIL import Image
            image_size = (400, 250)

            st.subheader('מה הכי קרוב שנגיע אם נחבר כף רגל אחת')
            st.subheader('? מכל אחד מאיתנו בקו ישר אחד')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':blue[רוחב שער כדורגל]')
                    url = r'Assets\Pictures\goal.jfif'
                    image = Image.open(url)
                    new_image = image.resize(image_size)
                    st.image(new_image, use_column_width='always')

                with col2:
                    st.header(':green[אורך גל תדר גלגלצ]')
                    url = r'Assets\Pictures\wave.jpg'
                    image = Image.open(url)
                    new_image = image.resize(image_size)
                    st.image(new_image, use_column_width='always')

                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[אורך אוטובוס אקורדיון]')
                    url = r'Assets\Pictures\bus.jpg'
                    image = Image.open(url)
                    new_image = image.resize(image_size)
                    st.image(new_image, use_column_width='always')

                with col4:
                    st.header(':orange[רוחב תחת של 2 סוסים]')
                    url = r'Assets\Pictures\horses.jfif'
                    image = Image.open(url)
                    new_image = image.resize(image_size)
                    st.image(new_image, use_column_width='always')

        with st.expander(f'Shoe Chart :'):
            men_shoe = st.session_state['shoe_size_to_cm_men']
            women_shoe = st.session_state['shoe_size_to_cm_women']
            df_shoe_men = pd.DataFrame(data=men_shoe, columns=['size', 'cm'])
            df_shoe_women = pd.DataFrame(data=women_shoe, columns=['size', 'cm'])

            fig = px.line()
            fig.add_scatter(y=df_shoe_men['cm'], x=df_shoe_men['size'], mode='lines', name='Men')
            fig.add_scatter(y=df_shoe_women['cm'], x=df_shoe_women['size'], mode='lines', name='Women')
            fig.update_layout(
                showlegend=False,
                xaxis_title="Shoe Size",
                yaxis_title="CM",
                height=400,
                xaxis=dict(
                    showgrid=True,
                    gridwidth=0.1,
                    gridcolor='white',
                    zeroline=True,
                    showline=True,
                    showticklabels=True,
                    ticks='inside',
                    tickcolor='crimson',
                    tickwidth=2,
                    ticklen=10,
                    mirror=True,
                ),
                yaxis=dict(
                    showgrid=True,
                    gridwidth=0.1,
                    gridcolor='white',
                    zeroline=True,
                    showline=True,
                    showticklabels=True,
                    ticks='inside',
                    tickcolor='crimson',
                    tickwidth=2,
                    ticklen=10,
                    mirror=True,
                ),
            )
            st.plotly_chart(fig, use_container_width=True)

    with col02:
        st.header('A')

        with st.expander(f'Answer :'):

            st.header(':blue[רוחב שער כדורגל]')

            from PIL import Image
            image_size = (400, 250)
            url = r'Assets\Pictures\goal.jfif'
            image = Image.open(url)
            new_image = image.resize(image_size)
            st.image(new_image, use_column_width='always')

            len_m = int(shoe_len / 100)
            st.header('')
            st.header(f'סכום אורך כפות הרגליים = {len_m} מטר')
            st.subheader('')
            st.subheader(f'תחת שני סוסים = 1.87 מטר')
            st.header(':blue[שער כדורגל = 7.32 מטר]')
            st.subheader(f'אוטובוס אקורדיון = 18 מטר')
            st.subheader(f'אורך גל-גלצ = 32.7 מטר')

st.header(f'', divider='rainbow')
from Kapoot import clock_run
clock_run()
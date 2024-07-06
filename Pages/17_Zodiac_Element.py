import numpy as np
import pandas as pd
import streamlit as st

emoji = ':fire::ocean::seedling::wind_blowing_face:'
title = 'Zodiac & Elements'
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

        with st.expander(f'Our Zodiac and Elements :'):
            with st.container():
                # with st.container():
                #     col00, col01 = st.columns(2)
                #     with col00:
                # Graphviz chart
                graph = '''
                digraph {
                    Air         [label="Air",   fillcolor="aquamarine", style="filled"]
                    Earth       [label="Earth", fillcolor="green",      style="filled"]
                    Water       [label="Water", fillcolor="cyan",       style="filled"]
                    Fire        [label="Fire",  fillcolor="red",        style="filled"]

                    Gemini      [label="Gemini\n(תאומים)",  fillcolor="aquamarine", style="filled"]
                    Libra       [label="Libra\n(מאזניים)",  fillcolor="aquamarine", style="filled"]
                    Aquarius    [label="Aquarius\n(דלי)",   fillcolor="aquamarine", style="filled"]
                    Taurus      [label="Taurus\n(שור)",     fillcolor="green",      style="filled"]
                    Virgo       [label="Taurus\n(בתולה)",   fillcolor="green",      style="filled"]
                    Capricorn   [label="Capricorn\n(גדי)",  fillcolor="green",      style="filled"]
                    Cancer      [label="Cancer\n(סרטן)",    fillcolor="cyan",       style="filled"]
                    Pisces      [label="Pisces\n(דגים)",    fillcolor="cyan",       style="filled"]
                    Scorpio     [label="Scorpio\n(עקרב)",   fillcolor="cyan",       style="filled"]
                    Aries       [label="Aries\n(טלה)",      fillcolor="red",        style="filled"]
                    Leo         [label="Leo\n(אריה)",       fillcolor="red",        style="filled"]
                    Sagittarius [label="Sagittarius\n(קשת)",fillcolor="red",        style="filled"]

                    Air -> Gemini
                    Air -> Libra
                    Air -> Aquarius
                    Earth -> Taurus
                    Earth -> Virgo
                    Earth -> Capricorn
                    Water -> Cancer
                    Water -> Pisces
                    Water -> Scorpio
                    Fire -> Aries
                    Fire -> Leo
                    Fire -> Sagittarius

                    Pisces -> שלי
                    Leo -> איגור
                    Leo -> אלעד
                    Cancer -> ליאורה
                    Cancer -> רומן
                    Libra -> אורן
                    Libra -> רועי
                    Taurus -> דביר
                    Taurus -> איתן
                    Capricorn -> שמעון
                    Capricorn -> מאור
                    Aries -> אופיר
                    Gemini -> אריק
                    Virgo -> אלחי
                    Sagittarius -> אביחי
                }
                '''
                # Display chart
                st.graphviz_chart(graph)

        with st.expander(f'Question :'):
            st.subheader('? כמה לא ידעו איזה אלמנט הם')
            st.subheader('אוויר \ אדמה \ מים \ אש')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':blue[9 :confused:]')
                with col2:
                    st.header(':green[2 :grin:]')
                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[10 :confounded:]')
                with col4:
                    st.header(':orange[5 :yum:]')

    with col02:
        st.header('A')

        with st.expander(f'Zodiac and Elements Results :'):
            with st.container():

                # with st.container():
                #     col00, col01 = st.columns(2)
                #     with col00:
                # Graphviz chart
                graph = '''
                digraph {
                    Air         [label="Air",   fillcolor="aquamarine", style="filled"]
                    Earth       [label="Earth", fillcolor="green",      style="filled"]
                    Water       [label="Water", fillcolor="cyan",       style="filled"]
                    Fire        [label="Fire",  fillcolor="red",        style="filled"]

                    Gemini      [label="Gemini\n(תאומים)",  fillcolor="aquamarine", style="filled"]
                    Libra       [label="Libra\n(מאזניים)",  fillcolor="aquamarine", style="filled"]
                    Aquarius    [label="Aquarius\n(דלי)",   fillcolor="aquamarine", style="filled"]
                    Taurus      [label="Taurus\n(שור)",     fillcolor="green",      style="filled"]
                    Virgo       [label="Virgo\n(בתולה)",    fillcolor="green",      style="filled"]
                    Capricorn   [label="Capricorn\n(גדי)",  fillcolor="green",      style="filled"]
                    Cancer      [label="Cancer\n(סרטן)",    fillcolor="cyan",       style="filled"]
                    Pisces      [label="Pisces\n(דגים)",    fillcolor="cyan",       style="filled"]
                    Scorpio     [label="Scorpio\n(עקרב)",   fillcolor="cyan",       style="filled"]
                    Aries       [label="Aries\n(טלה)",      fillcolor="red",        style="filled"]
                    Leo         [label="Leo\n(אריה)",       fillcolor="red",        style="filled"]
                    Sagittarius [label="Sagittarius\n(קשת)",fillcolor="red",        style="filled"]

                    איגור      [label="איגור",  fillcolor="green",      style="filled"]
                    אורן       [label="אורן",   fillcolor="red",        style="filled"]
                    איתן       [label="איתן",   fillcolor="red",        style="filled"]
                    שמעון      [label="שמעון",  fillcolor="cyan",       style="filled"]
                    אלעד       [label="אלעד",   fillcolor="green",      style="filled"]
                    אופיר      [label="אופיר",  fillcolor="aquamarine", style="filled"]
                    אלחי       [label="אלחי",   fillcolor="red",        style="filled"]
                    רומן       [label="רומן",   fillcolor="green",      style="filled"]
                    מאור       [label="מאור",   fillcolor="aquamarine", style="filled"]
                    אביחי      [label="אביחי",  fillcolor="aquamarine", style="filled"]

                    Air -> Gemini
                    Air -> Libra
                    Air -> Aquarius
                    Earth -> Taurus
                    Earth -> Virgo
                    Earth -> Capricorn
                    Water -> Cancer
                    Water -> Pisces
                    Water -> Scorpio
                    Fire -> Aries
                    Fire -> Leo
                    Fire -> Sagittarius

                    Pisces -> שלי
                    Leo -> איגור
                    Leo -> אלעד
                    Cancer -> ליאורה
                    Cancer -> רומן
                    Libra -> אורן
                    Libra -> רועי
                    Taurus -> דביר
                    Taurus -> איתן
                    Capricorn -> שמעון
                    Capricorn -> מאור
                    Aries -> אופיר
                    Gemini -> אריק
                    Virgo -> אלחי
                    Sagittarius -> אביחי
                }
                '''
                # Display chart
                st.graphviz_chart(graph)

        with st.expander(f'Answer :'):

            st.header(':red[10 :confounded:]')

st.header(f'', divider='rainbow')
from Kapoot import clock_run
clock_run()


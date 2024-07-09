import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

emoji = ':movie_camera:'
title = 'TV Shows'
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
    my_list = list(df['origin'])
    len_list = len(my_list)
    color_list = [''] * len_list
    for i in range(len_list):
        if my_list[i] == 'Israel':
            color_list[i] = 'blue'
        elif my_list[i] == 'Overseas':
            color_list[i] = 'green'
        else:
            color_list[i] = 'red'
    df_chart['color'] = color_list

    df_chart = df_chart.sort_values(by='color', ascending=False)
    return df_chart


df_chart = calculate()

with st.container():
    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')
        with st.expander(f'Question :'):
            st.subheader('אנחנו רואים תוכניות')
            st.subheader('... שמקורן בעיקר')
            with st.container():
                col1, col2 = st.columns(2)
                with col1:
                    st.header(':green[תוצרת חוץ]')
                with col2:
                    st.header(':blue[ישראלי]')
                col3, col4 = st.columns(2)
                with col3:
                    st.header(':red[לא רואה]')
                with col4:
                    st.header(':orange[? מי בוחר בי]')

    with col02:
        st.header('A')

        with st.expander(f'Answer :'):
            st.header(':green[תוצרת חוץ]')

            # Graphviz chart
            graph = '''
            digraph {
                ישראלי  [label="ישראלי",   fillcolor="blue",  style="filled"]
                חוצלארץ [label="חוצלארץ",  fillcolor="green", style="filled"]
                גל_שקט [label="גל_שקט",     fillcolor="red",   style="filled"]

                שלי     [label="שלי\n(Bridgerton)",]
                ליאורה  [label="ליאורה\n(עספור)",]
                אורן    [label="אורן\n(בלקספייס)",]
                איתן    [label="איתן\n(Bodies)",]
                רועי    [label="רועי\n(Baby Raindeer)",]
                שמעון   [label="שמעון\n(חדשות)",]
                אלעד    [label="אלעד\n(האיש שרצה לדעת הכל)",]
                אריק    [label="אריק\n(אף אחד לא עוזב את פאלו אלטו)",]
                רומן    [label="רומן\n(One Day)",]
                דביר    [label="דביר\n(Tour de France)",]
                אביחי   [label="אביחי\n(Snatch)",]
                איגור   [label="איגור\n(לא צופה)",]
                אופיר   [label="אופיר\n(לא צופה)",]
                אלחי    [label="אלחי\n(לא צופה)",]
                מאור    [label="מאור\n(לא צופה)",]

                ישראלי -> ליאורה
                ליאורה -> אורן
                אורן -> שמעון
                שמעון -> אלעד
                אלעד -> אריק

                חוצלארץ -> שלי
                שלי -> איתן
                איתן -> רועי
                רועי -> רומן
                רומן -> דביר
                דביר -> אביחי
                
                גל_שקט -> איגור
                איגור -> אופיר
                אופיר -> אלחי
                אלחי -> מאור
            }
            '''
            # Display chart
            st.graphviz_chart(graph)

st.header(f'', divider='rainbow')
from Kapoot import clock_run
clock_run()
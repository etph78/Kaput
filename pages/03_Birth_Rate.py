import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

emoji = ':baby:'
title = 'Birth Rate'
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
    private = list(df['פרטי'])
    birth = list(df['לידה'])

    dict_chart = {
        'private': private,
        'birth': birth,
    }
    df_chart = pd.DataFrame(dict_chart)
    df_chart = df_chart.sort_values(by='birth', ascending=False)

    birth1 = np.random.randint(1960, 2005, size=len(df_chart))
    birth2 = np.random.randint(1960, 2005, size=len(df_chart))
    birth3 = np.random.randint(1960, 2005, size=len(df_chart))

    return df_chart, birth1, birth2, birth3


df_chart, birth1, birth2, birth3 = calculate()

with st.container():
    col01, col02 = st.columns(2)
    with col01:
        st.header('Q')
        with st.expander(f'Question :'):
            st.subheader('? מה היסטוגרמת פילוג הגילאים')
            st.subheader('(לפי עשורים)')
            with st.container():
                graph_height = 300
                col1, col2 = st.columns(2)
                with col1:
                    fig = px.histogram(birth1, nbins=5, height=graph_height,
                                       color_discrete_sequence=["blue",],)
                    # Labels
                    fig.update_layout(
                        title_text='',  # no title
                        xaxis_title_text='עשור',  # no xaxis label
                        showlegend=False,  # no legend
                        bargroupgap=0.1  # gap between bars of the same location coordinates
                    )
                    st.plotly_chart(fig)

                with col2:
                    fig = px.histogram(birth2, nbins=5, height=graph_height,
                                       color_discrete_sequence=["green",],)
                    # Labels
                    fig.update_layout(
                        title_text='',  # no title
                        xaxis_title_text='עשור',  # no xaxis label
                        showlegend=False,  # no legend
                        bargroupgap=0.1  # gap between bars of the same location coordinates
                    )
                    st.plotly_chart(fig)

                col3, col4 = st.columns(2)
                with col3:
                    birth = df_chart['birth']
                    # Create a histogram
                    fig = px.histogram(birth, nbins=5, height=graph_height,
                                       color_discrete_sequence=["red", ], )
                    # Labels
                    fig.update_layout(
                        title_text='',  # no title
                        xaxis_title_text='עשור',  # no xaxis label
                        showlegend=False,  # no legend
                        bargroupgap=0.1  # gap between bars of the same location coordinates
                    )
                    st.plotly_chart(fig)

                with col4:
                    # st.header(':orange[D]')
                    fig = px.histogram(birth3, nbins=5, height=graph_height,
                                       color_discrete_sequence=["orange",],)
                    # Labels
                    fig.update_layout(
                        title_text='',  # no title
                        xaxis_title_text='עשור',  # no xaxis label
                        showlegend=False,  # no legend
                        bargroupgap=0.1  # gap between bars of the same location coordinates
                    )
                    st.plotly_chart(fig)

    with col02:
        st.header('A')
        with st.expander(f'Answer :'):
            birth = df_chart['birth']
            # Create a histogram
            fig = px.histogram(birth,
                               nbins=5, height=670,
                               title='Histogram',
                               color_discrete_sequence=["red",],)
            # Labels
            fig.update_layout(
                title_text='',  # no title
                xaxis_title_text='עשור',  # no xaxis label
                # yaxis_title_text='#',  # no yaxis label
                showlegend=False,  # no legend
                # bargap=0.2,  # gap between bars of adjacent location coordinates
                bargroupgap=0.1  # gap between bars of the same location coordinates
            )
            # Display the plot in Streamlit
            st.plotly_chart(fig)

st.header(f'', divider='rainbow')
from Kapoot import clock_run
clock_run()
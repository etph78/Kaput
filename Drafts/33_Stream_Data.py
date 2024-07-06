import numpy as np
import pandas as pd
import streamlit as st
import pydeck as pdk
import great_circle_calculator.great_circle_calculator as gcc
from datetime import datetime, timedelta

st.set_page_config(
    page_title="XXX",
    page_icon="📊",
    layout='wide',
)


# @st.cache_data
def calculate():
    df = st.session_state['df_data']
    df_chart = df
    # df_chart = df_chart.sort_values(by='dist', ascending=False)

    return df_chart


st.header('Q')
with st.expander(f'Question :'):
    st.subheader('Who Has the Most Distance from Home to Netanel ?')
    st.write('(Great Circle Distance)')
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.header(':blue[XXX]')
        with col2:
            st.header(':green[YYY]')
        col3, col4 = st.columns(2)
        with col3:
            st.header(':red[WWW]')
        with col4:
            st.header(':orange[ZZZ]')


st.divider()
from Kapoot import clock_run
clock_run()

st.header('A')
df_chart = calculate()
st.session_state['stream_data'] = df_chart

with st.expander(f'Answer :'):
    winner_df = df_chart
    # winner_df = winner_df[['private', 'home_lat', 'home_lon', 'work_lat', 'work_lon',]]
    winner_df = winner_df[0:1]
    st.write(winner_df)


    def get_recent_data(last_timestamp):
        """Generate and return data from last timestamp to now, at most 60 seconds."""
        now = datetime.now()
        if now - last_timestamp > timedelta(seconds=60):
            last_timestamp = now - timedelta(seconds=60)
        sample_time = timedelta(seconds=0.5)  # time between data points
        next_timestamp = last_timestamp + sample_time
        timestamps = np.arange(next_timestamp, now, sample_time)

        sample_values = np.random.randn(len(timestamps), 2)
        data = pd.DataFrame(sample_values, index=timestamps, columns=["A", "B"])

        # stream_data = st.session_state['stream_data']
        # sample_values = {
        #     'shoe': list(stream_data['נעל']),
        #     'age': list(stream_data['לידה']),
        #     'floor': list(stream_data['קומה']),
        # }
        # data = pd.DataFrame(sample_values, index=timestamps)

        return data


    if "data" not in st.session_state:
        st.session_state.data = get_recent_data(datetime.now() - timedelta(seconds=60))

    if "stream" not in st.session_state:
        st.session_state.stream = False


    def toggle_streaming():
        st.session_state.stream = not st.session_state.stream


    st.title("Data Stream")
    st.sidebar.slider(
        "Update Every: [sec]", 0.5, 5.0, value=1.0, key="run_every"
    )
    st.sidebar.button(
        "Start streaming", disabled=st.session_state.stream, on_click=toggle_streaming
    )
    st.sidebar.button(
        "Stop streaming", disabled=not st.session_state.stream, on_click=toggle_streaming
    )

    if st.session_state.stream is True:
        run_every = st.session_state.run_every
    else:
        run_every = None


    @st.experimental_fragment(run_every=run_every)
    def show_latest_data():
        last_timestamp = st.session_state.data.index[-1]
        st.session_state.data = pd.concat(
            [st.session_state.data, get_recent_data(last_timestamp)]
        )
        st.session_state.data = st.session_state.data[-100:]
        st.line_chart(st.session_state.data)


    show_latest_data()
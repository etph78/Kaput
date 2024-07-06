import os
import numpy as np
import pandas as pd
import streamlit as st


def clock_run():
    import time

    seconds = 30
    col1, col2, col3, col4, col5, col6, col7, col8, = st.columns(8)
    with col1:
        run = st.button(f"Run {seconds}sec")
    with col2:
        stop = st.button("Stop")

    my_bar = st.progress(0, text=f'{seconds} [sec]')
    if run:
        my_bar.empty()

        bip1_flag = False
        bip2_flag = False

        for percent_complete in range(100):
            time_left = seconds * (1 - (percent_complete / 100))
            time.sleep(seconds / 100)
            my_bar.progress(percent_complete, text=f'{time_left:0.0f} [sec]')
            if stop:
                break
            if time_left < 13:
                if bip1_flag == False:
                    bip1_flag = True
                    st.audio(r'Assets\Audio\bip2.wav', format="audio/wav", loop=False, autoplay=True)
                else:
                    pass

            if time_left < 3:
                if bip2_flag == False:
                    bip2_flag = True
                    st.audio(r'Assets\Audio\bip4.wav', format="audio/wav", loop=False, autoplay=True)
                else:
                    pass

            if percent_complete == 100 - 1:
                st.balloons()
                bip1_flag = False
                bip2_flag = False


def read_score():
    import pandas as pd
    # st.session_state['folder'] = r'C:\Users\e025553\OneDrive - Elbit Systems 365\Documents\Work\StreamLit_Kapoot'
    st.session_state['folder'] = r''
    st.session_state['file'] = r'score.csv'

    folder = st.session_state['folder']
    file = st.session_state['file']
    score_file = os.path.join(folder, file)
    st.session_state['score_file'] = score_file

    file_exist = os.path.isfile(score_file)
    if file_exist:
        score_df = pd.read_csv(score_file)
    else:
        score_df = pd.DataFrame()
    st.session_state['score_df'] = score_df

    return


def write_score():

    score_file = st.session_state['score_file']
    score_df = st.session_state['score_df']
    score_df.to_csv(score_file, index=False)

    return


def get_data():
    import pandas as pd

    st.session_state['folder'] = r'C:\Users\e025553\OneDrive - Elbit Systems 365\Documents\Work\StreamLit_Kapoot'
    st.session_state['file'] = r'Kapoot.xlsx'

    folder = st.session_state['folder']
    file = st.session_state['file']
    xls_file = os.path.join(folder, file)
    st.session_state['data_file'] = xls_file

    file_exist = os.path.isfile(xls_file)
    if file_exist:
        df_xls = pd.read_excel(xls_file)
    else:
        df_xls = pd.DataFrame()
    st.session_state['df_data'] = df_xls

    return


def score_group1():
    num = '1'
    score_df = st.session_state['score_df']
    # st.write(score_df)
    Current = score_df.at[0, f'Group{num}']
    with st.form(key=f'form{num}'):
        New_Score = st.text_input(f"Add to Group{num}")
        set_val = st.form_submit_button(f"Set{num}")
        if set_val:
            # Handle the user input here
            try:
                New_Score = int(New_Score)
                Updated = Current + New_Score

            except Exception as e:
                Updated = score_df.at[0, f'Group{num}']
        else:
            Updated = score_df.at[0, f'Group{num}']

    score_df.at[0, f'Group{num}'] = Updated
    st.session_state['score_df'] = score_df
    st.metric(label="ניקוד", value=f"{Updated}", delta='')


def sb_score_group1():
    num = '1'
    sb = st.sidebar
    score_df = st.session_state['score_df']
    # Current = score_df.at[0, f'Group{num}']
    # with sb.form(key=f'form{num}'):
    #     New_Score = st.text_input(f"Add to Group{num}")
    #     set_val = st.form_submit_button(f"Set{num}")
    #     if set_val:
    #         # Handle the user input here
    #         try:
    #             New_Score = int(New_Score)
    #             Updated = Current + New_Score
    #
    #         except Exception as e:
    #             Updated = score_df.at[0, f'Group{num}']
    #     else:
    #         Updated = score_df.at[0, f'Group{num}']
    #
    # score_df.at[0, f'Group{num}'] = Updated
    # st.session_state['score_df'] = score_df
    Updated = score_df.at[0, f'Group{num}']
    sb.write(f"Group{num} Score: {Updated}")


def score_group2():
    num = '2'
    score_df = st.session_state['score_df']
    # st.write(score_df)
    Current = score_df.at[0, f'Group{num}']
    st.session_state[f'Group{num}_Current_Score'] = Current

    with st.form(key=f'form{num}'):
        New_Score = st.text_input(f"Add to Group{num}")
        set_val = st.form_submit_button(f"Set{num}")
        if set_val:
            # Handle the user input here
            try:
                New_Score = int(New_Score)
                Updated = Current + New_Score

            except Exception as e:
                Updated = score_df.at[0, f'Group{num}']
        else:
            Updated = score_df.at[0, f'Group{num}']

    score_df.at[0, f'Group{num}'] = Updated
    st.session_state['score_df'] = score_df
    st.metric(label="ניקוד", value=f"{Updated}", delta='')


def sb_score_group2():
    num = '2'
    sb = st.sidebar
    score_df = st.session_state['score_df']
    # Current = score_df.at[0, f'Group{num}']
    # st.session_state[f'Group{num}_Current_Score'] = Current
    #
    # with sb.form(key=f'form{num}'):
    #     New_Score = st.text_input(f"Add to Group{num}")
    #     set_val = st.form_submit_button(f"Set{num}")
    #     if set_val:
    #         # Handle the user input here
    #         try:
    #             New_Score = int(New_Score)
    #             Updated = Current + New_Score
    #
    #         except Exception as e:
    #             Updated = score_df.at[0, f'Group{num}']
    #     else:
    #         Updated = score_df.at[0, f'Group{num}']
    #
    # score_df.at[0, f'Group{num}'] = Updated
    # st.session_state['score_df'] = score_df
    Updated = score_df.at[0, f'Group{num}']
    sb.write(f"Group{num} Score: {Updated}")


def score_group3():
    num = '3'
    score_df = st.session_state['score_df']
    # st.write(score_df)
    Current = score_df.at[0, f'Group{num}']
    st.session_state[f'Group{num}_Current_Score'] = Current

    with st.form(key=f'form{num}'):
        New_Score = st.text_input(f"Add to Group{num}")
        set_val = st.form_submit_button(f"Set{num}")
        if set_val:
            # Handle the user input here
            try:
                New_Score = int(New_Score)
                Updated = Current + New_Score

            except Exception as e:
                Updated = score_df.at[0, f'Group{num}']
        else:
            Updated = score_df.at[0, f'Group{num}']

    score_df.at[0, f'Group{num}'] = Updated
    st.session_state['score_df'] = score_df
    st.metric(label="ניקוד", value=f"{Updated}", delta='')


def sb_score_group3():
    num = '3'
    sb = st.sidebar
    score_df = st.session_state['score_df']
    # Current = score_df.at[0, f'Group{num}']
    # st.session_state[f'Group{num}_Current_Score'] = Current
    #
    # with sb.form(key=f'form{num}'):
    #     New_Score = st.text_input(f"Add to Group{num}")
    #     set_val = st.form_submit_button(f"Set{num}")
    #     if set_val:
    #         # Handle the user input here
    #         try:
    #             New_Score = int(New_Score)
    #             Updated = Current + New_Score
    #
    #         except Exception as e:
    #             Updated = score_df.at[0, f'Group{num}']
    #     else:
    #         Updated = score_df.at[0, f'Group{num}']
    #
    # score_df.at[0, f'Group{num}'] = Updated
    # st.session_state['score_df'] = score_df
    Updated = score_df.at[0, f'Group{num}']
    sb.write(f"Group{num} Score: {Updated}")


def scores():
    # Create three columns
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            score_group1()
        with col2:
            score_group2()
        with col3:
            score_group3()

    # score_df = st.session_state['score_df']
    # st.write(score_df)
    return


def sb_scores():
    # Create three columns
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            sb_score_group1()
        with col2:
            sb_score_group2()
        with col3:
            sb_score_group3()
    return


st.session_state['zodiac'] = {
    'דלי': 1,
    'דגים': 2,
    'טלה': 3,
    'שור': 4,
    'תאומים': 5,
    'סרטן': 6,
    'אריה': 7,
    'בתולה': 8,
    'מאזניים': 9,
    'עקרב': 10,
    'קשת': 11,
    'גדי': 12,
}

st.session_state['work_coord'] = {
    'נתנאל': (31.91180, 34.80500),
    'שחקים': (31.92519, 34.96992),
}

st.session_state['home_coord'] = {
    'מודיעין': (31.90899, 35.00555),
    'פתח-תקווה': (32.08438, 34.88959),
    'תל-אביב': (32.08441, 34.78008),
    'יבנה': (31.87570, 34.73460),
    'נס-ציונה': (31.92912, 34.79858),
    'גבעתיים': (32.07544, 34.80836),
    'רחובות': (31.8947, 34.81167),
    'נחלים': (32.05845, 34.91194),
    'הוד-השרון': (32.15001, 34.88450),
    'ראשון-לציון': (31.95906, 34.80236),
    'רעננה': (32.19210, 34.87472),
}

st.session_state['country_coord'] = {
    'ישראל': (31.789072229290998, 34.8829003410082),
    'פולין': (52.87592695313997, 18.634717795859522),
    'ליטא': (55.5073537292507, 23.884130613359563),
    'אוקראינה': (49.02040873611441, 31.789496276561906),
    'בלגיה': (50.533582689522554, 4.761269594374357),
    'קונגו': (-0.8444135093586751, 15.135108945799498),
    'יוון': (39.424329525574585, 22.353051855725518),
    'מרוקו': (31.948290642681204, -6.299993262901092),
    'לבנון': (34.22564422292364, 35.91403486631935),
    'אוסטרליה': (-24.988177544279587, 135.13292077333085),
    'גרמניה': (51.08641938474385, 10.354394017828739),
    'צכיה': (49.42854559840274, 15.41632777999925),
    'עירק': (33.00267258122371, 43.100730948413286),
    'רומניה': (45.76431039433079, 25.00900472435942),
    'רוסיה': (62.255576840512575, 93.7380403313164),
    'איטליה': (42.99588240875469, 12.916607434889132),
    'מולדובה': (47.56531423614694, 28.477366777857746),
    'הונגריה': (46.98826818985046, 19.81018482982935),
    'תימן': (15.859232635285528, 47.53328891747984),
}

st.session_state['passport_coord'] = {
    'אוסטריה': (47.653161373731706, 14.453489783607209),
    'מונטנגרו': (42.798871205926204, 19.213491487448803),
    'יוון': (39.424329525574585, 22.353051855725518),
    'שוויץ': (46.851737968850394, 7.628278257929917),
    'מלדיביים': (3.0947736027908257, 73.86116642345905),
    'קפריסין': (35.03639878171189, 33.20003496938621),
    'גיאורגיה': (42.23114351726932, 43.62807095986709),
    'הודו': (22.88245672747506, 79.4207849308533),
    'גרמניה': (51.08454953090897, 10.544625879874188),
    'ספרד': (39.68243219730833, -3.015702884518763),
}

st.session_state['weekend_coord'] = {
    'פריז': (48.85726634242172, 2.350640444419219),
    'טיווט': (42.4317776389908, 18.69865544067626),
    'לונדון': (51.510581140936004, -0.12562299902894508),
    'טוקיו': (35.70395823847689, 139.7535090157889),
    'רומא': (41.897691843242896, 12.484767221840162),
    'פראג': (50.081148314824, 14.438853255348818),
    'וינה': (48.20990907905498, 16.372434912167456),
    'מדריד': (40.84914080750264, -3.6936552118017527),
    'אמסטרדם': (52.3661685510937, 4.901559186569476),
    'אדינבורו': (55.94676334106096, -3.2152631923571735),
    'לפלנד': (66.50128085451867, 25.735575007371235),
}

st.session_state['shoe_size_to_cm_men'] = {
    'size': [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, ],
    'cm': [21.0, 22.4, 23.3, 23.7, 24.6, 25.0, 25.8, 26.4, 27.1, 27.7, 28.3, ],
}

st.session_state['shoe_size_to_cm_women'] = {
    'size': [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46],
    'cm': [21.2, 22.0, 22.4, 23.0, 23.7, 24.6, 25.0, 25.8, 26.4, 27.1, 27.7, 28.4, ],
}


def main():
    emoji = ':sloth:'
    st.logo('Assets\\Pictures\\logo.png')
    st.set_page_config(page_title="KaPoot",
                       page_icon=emoji,
                       layout='wide',
                       )

    st.image('Assets\\Pictures\\logo.jpeg', width=150)
    st.header(f'Welcome to "Ka-Poot" Game {emoji}', divider='rainbow')

    read_score()
    scores()

    with (st.container()):
        get_data()

        # Create three columns
        with st.expander(f'Groups'):
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.header(f'השולטים')
                    with st.container():
                        col11, col12 = st.columns(2)
                        with col11:
                            st.image('Assets/Pictures/logo.png', width=100)
                            st.image('Assets/Pictures/logo.png', width=100)
                        with col12:
                            st.image('Assets/Pictures/logo.png', width=100)
                            st.image('Assets/Pictures/logo.png', width=100)

                with col2:
                    st.header(f'אווירון', )
                    with st.container():
                        col21, col22 = st.columns(2)
                        with col21:
                            st.image('Assets/Pictures/logo.png', width=100)
                            st.image('Assets/Pictures/logo.png', width=100)
                            st.image('Assets/Pictures/logo.png', width=100)
                        with col22:
                            st.image('Assets/Pictures/logo.png', width=100)
                            st.image('Assets/Pictures/logo.png', width=100)

                with col3:
                    st.header(f'אווירה')
                    with st.container():
                        col21, col22 = st.columns(2)
                        with col21:
                            st.image('Assets/Pictures/logo.png', width=100)
                            st.image('Assets/Pictures/logo.png', width=100)
                            st.image('Assets/Pictures/logo.png', width=100)
                        with col22:
                            st.image('Assets/Pictures/logo.png', width=100)
                            st.image('Assets/Pictures/logo.png', width=100)
                            # st.image('Assets/Pictures/logo.png', width=100)

        write_score()

    with st.expander(f'Rules'):
        st.header('Rules:')
        st.subheader('1. You Dont Talk about KaPoot Club')
        st.subheader('2. May the Winner - Win')
        st.subheader('3. Cheating is Fun', )
        st.subheader('4. One Answer for All', )
        st.subheader('5. Are You Ready ???', divider='rainbow')

    with st.expander(f'Timer Example'):
        clock_run()

    df = st.session_state['df_data']
    with st.expander(f'Your Data {df.shape}'):
        st.write(f'Excel File:')
        st.write(st.session_state['data_file'])
        st.write(st.session_state['df_data'])

    sb = st.sidebar
    sb.header('')
    sb.header('')

    reset_all = sb.button(label="Reset ...", type="primary")
    if reset_all:
        score_df = st.session_state['score_df']
        score_df['Group1'] = [0]
        score_df['Group2'] = [0]
        score_df['Group3'] = [0]
        st.session_state['Group1_Updated_Score'] = 0
        st.session_state['Group2_Updated_Score'] = 0
        st.session_state['Group3_Updated_Score'] = 0
        write_score()

    refresh_all = sb.button(label="Refresh ...", type="primary")
    if refresh_all:
        read_score()

    # st.rerun()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

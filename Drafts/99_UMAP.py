import os
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="XXX",
    page_icon="📊",
    layout='wide',
)

st.session_state['param_to_drop'] = [
    'פרטי', 'משפחה', 'ישוב',
    'פרי', 'קינוח', 'בעח', 'שפות', 'ארצות',
    'סופש', 'דרכון', 'ממתיק', 'צבע', 'אלכוהול',
    'מזל', 'יסוד', 'רכב', 'תוכנית', 'חג', 'טריויה',
]


def calc_umap():

    # Buttons & Sliders
    # get_the_data = st.sidebar.button('(1) Get & Prepare Data')
    n_neighbors = st.sidebar.slider('N_Neighbours', value=10, min_value=1, max_value=100)  # 👈 this is a widget
    st.session_state['n_neighbors'] = n_neighbors
    calculate_umap = st.sidebar.button('(2) Calculate UMAP')

    clusters = st.sidebar.slider('Clusters', value=3, min_value=1, max_value=10)  # 👈 this is a widget
    st.session_state['clusters'] = clusters
    calculate_clusters = st.sidebar.button('(3) Calculate Clusters')

    make_graph = st.sidebar.button('(4) Make Graph')
    st.sidebar.divider()

    # Button is pressed
    if calculate_umap:
        print(f'calculate_umap')
        df_prep = st.session_state['df_prep']
        if df_prep.shape[0] > 0:
            st.write(f'Calculating UMAP...')
            calc_umap()
            st.write(f'UMAP Calc is Done')
        else:
            st.write(f'Please Get Data First')

    # Button is pressed
    if calculate_clusters:
        print(f'calculate_clusters')
        df_umap = st.session_state['df_umap']
        if df_umap.shape[0] > 0:
            st.write(f'Calculating Clusters...')
            calc_clusters()
            st.write(f'Clusters Calc is Done')
        else:
            st.write(f'Please Get UMAP First')

    # Button is pressed
    if make_graph:
        df_umap = st.session_state['df_umap']
        if df_umap.shape[0] > 0:
            graph = create_graph()
            st.bokeh_chart(graph)
        else:
            print(f'Empty df_umap')
            st.write(f'Please Get Clusters First')

    st.write(f'UMAP Params:')
    import umap
    from sklearn.preprocessing import MinMaxScaler

    st.session_state['df_umap'] = pd.DataFrame()
    st.session_state['labels_umap'] = st.session_state['param_to_drop']

    df = st.session_state['df_prep']
    columns = df.columns
    st.session_state['params_umap'] = columns
    for col in columns:
        df = df[df[col].notnull()]
    st.session_state['df_prep_no_nan'] = df

    # Print:
    st.write(f'df_prep without NaN DataFrame:')
    st.write(f'{columns}')
    st.write(f'df  size: {df.shape}')
    st.write(df)

    # normalize data
    # print(f'Normalize data')
    st.write(f'Normalize data:')
    scaler = MinMaxScaler()

    df = st.session_state['df_prep_no_nan']
    indexes = df.index.to_list()
    # st.write(f'indexes: {indexes}')

    df = df.reset_index(drop=True)
    indexes = df.index.to_list()
    # st.write(f're_indexes: {indexes}')

    st.write(df)
    columns = df.columns
    # st.write(f'columns: {columns}')

    for col in columns:
        # st.write(f'col: {col}')

        # Pass a DataFrame containing
        # a single row (i.e. single sample)
        # or a single column (i.e. single feature)
        df_col = df[[col]]
        # st.write(f'df_col:')
        # st.write(df_col)

        col_norm = scaler.fit_transform(df_col)
        # print(f'c{col_norm}')
        # st.write(col_norm)
        df[col] = col_norm

    # fit and transform the df
    # print(f'fit and transform the df')
    n_components = 2
    n_neighbors = st.session_state['n_neighbors']
    min_dist = 0.1
    random_state = 666

    umap_obj = umap.UMAP(
        n_components=n_components,
        n_neighbors=n_neighbors,
        min_dist=min_dist,
        random_state=random_state,
        metric='euclidean',
    )
    np_umap = umap_obj.fit_transform(df)
    df_umap = pd.DataFrame(np_umap)
    st.session_state['df_umap'] = df_umap
    # Print:
    st.write(f'df_umap DataFrame:')
    st.write(f'df_umap Data size: {df_umap.shape}')
    st.write(st.session_state['df_umap'])

def calc_clusters():

    import sklearn.cluster as cluster

    # fit and transform the df
    # print(f'fit and transform the df')
    n_clusters = st.session_state['clusters']
    df_umap = st.session_state['df_umap']
    np_umap = np.array(df_umap)

    # use k-means to cluster the UMAP projection
    # print(f'cluster the UMAP projection')
    kmeans = cluster.KMeans(
        n_clusters=n_clusters,
        n_init='auto',
    )
    kmeans.fit(np_umap)
    clusters_labels = kmeans.labels_

    st.session_state['labels_umap'] = clusters_labels

    return


def create_graph():
    from bokeh.plotting import figure
    from bokeh.plotting import ColumnDataSource
    from bokeh.models import HoverTool
    from bokeh.layouts import layout
    import bokeh.palettes as palettes

    df_prep = st.session_state['df_prep_no_nan']
    df_umap = st.session_state['df_umap']
    labels_umap = st.session_state['labels_umap']
    if df_umap.shape[0] > 0:
        columns = df_umap.columns.to_list()
        x = list(df_umap[columns[0]])
        y = list(df_umap[columns[1]])
        labels = list(labels_umap)
        df_prep['x_umap'] = x
        df_prep['y_umap'] = y
        df_prep['labels_umap'] = labels

    df = df_prep
    hover = HoverTool(
        tooltips=[
            # ("index", "$index"),
            # ("fm", "@ACT_FLIGHT_MODE"),
            ('(index, altitude, cas, ext_temp)', '($index, @UAV_ALTITUDE, @UAV_CAS, @EXT_AIR_TEMP_1)'),
        ]
    )
    tools = ["undo,redo,crosshair,pan,wheel_zoom,box_zoom,reset,save", hover]

    graph_width = 600
    graph_array = []
    graph = figure(
        title='#',
        tools=tools, toolbar_location="above",
        # tooltips=tooltips,
        plot_width=graph_width, plot_height=600)

    label = list(df['labels_umap'])
    unique_list = np.unique(label)
    print(f'label_set is :{unique_list}')
    Category10_10 = palettes.d3['Category10'][10]
    print(f'Category10 is :{Category10_10}')

    print(f'df is :\n{df}')

    for i in unique_list:
        df_i = df[df['labels_umap'] == i]
        label = f'Cluster {int(i)}'
        color = Category10_10[i]

        graph.circle(x='x_umap', y='y_umap', source=df_i,
                    legend_label=label,
                    width=50, color=color, alpha=0.5)

    graph_array.append([graph])

    # Arrange layout
    for debrief in graph_array:
        if type(debrief[0]) == type(figure()):
            debrief[0].legend.location = "top_left"
            debrief[0].legend.click_policy = "hide"
            debrief[0].legend.background_fill_alpha = 0.7
            debrief[0].legend.label_text_font_size = '8pt'
            debrief[0].toolbar.logo = None

    figure_array_size = len(graph_array)
    if figure_array_size > 0:
        graphs = layout(children=[[graph_array], ], )
    else:
        graphs = layout(children=[[], ], )
    # st.bokeh_chart(p, use_container_width=True)

    return graphs

def prepare_data():
    # change vacation city to enum
    col = 'סופש'
    new_col = 'vacation_num'
    get_list = list(df[col])
    list_len = len(get_list)
    # Create dictionary from list with frequencies
    dictionary = {}
    counter = 0
    for item in get_list:
        if item in dictionary:
            pass
        else:
            dictionary[item] = counter
            counter = counter + 1
    df[new_col] = [np.nan] * list_len
    for i in range(list_len):
        key = get_list[i]
        value = dictionary.get(key, 0)
        df.at[i, new_col] = value

    # change zodiac to enum
    col = 'מזל'
    new_col = 'zodiac_num'
    get_list = list(df[col])
    list_len = len(get_list)
    # Create dictionary from list with frequencies
    dictionary = st.session_state['zodiac']
    df[new_col] = [np.nan] * list_len
    for i in range(list_len):
        key = get_list[i]
        value = dictionary.get(key, 0)
        df.at[i, new_col] = value

    # change home to enum
    col = 'ישוב'
    new_col = 'home_2_work1'
    get_list = list(df[col])
    list_len = len(get_list)
    # Create dictionary from list with frequencies
    dictionary = {}
    counter = 0
    for item in get_list:
        if item in dictionary:
            pass
        else:
            dictionary[item] = counter
            counter = counter + 1
    df[new_col] = [np.nan] * list_len

    for i in range(list_len):
        key = get_list[i]
        value = dictionary.get(key, 0)
        df.at[i, new_col] = value
    # Drop un-wanted columns from later umap
    df_pre_umap = df
    # print(f'Drop param_to_drop from df_prep')
    param_to_drop = st.session_state['param_to_drop']
    for col in param_to_drop:
        # print(f'Drop: {col}')
        df_prep = df_pre_umap.drop(col, axis=1)
    st.session_state['df_pre_umap'] = df_pre_umap

    # Print:
    with st.expander(f'Pre UMAP DF - shape:{df_pre_umap.shape} :'):
        st.write(st.session_state['df_pre_umap'])

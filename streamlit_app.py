import pandas as pd
import streamlit as st

st.title('Data Visualization App')
upload_file = st.file_uploader("Upload your dataset", type=["csv", "txt"])
if upload_file is not None:
    data = pd.read_csv(upload_file)
    st.subheader('Displaying Dataframe')
    st.dataframe(data)
    st.subheader('Displaying initial rows from dataset')
    st.table(data.head())
    st.subheader('Displaying Summary Statistics')
    st.write(data.describe())
    st.subheader('Data Visualization')
    st.subheader('Area chart')
    selected_column_line=st.selectbox('Select a column for the area chart', data.columns)
    st.area_chart(data[selected_column_line])
    st.subheader('Scatter chart')
    selected_column_line=st.selectbox('Select a column for the scatter chart', data.columns)
    st.scatter_chart(data[selected_column_line])
    st.subheader('Line chart')
    selected_column_line=st.selectbox('Select a column for the Line chart', data.columns)
    st.line_chart(data[selected_column_line])
    st.subheader('Bar chart')
    selected_column_line=st.selectbox('Select a column for the Bar chart', data.columns)
    st.bar_chart(data[selected_column_line])
    st.balloons()
    st.snow()
    with st.sidebar:
    add_markdown = st.markdown(
        "Choose the plot to be viewed",
        ("Area", "Scatter","Line","Bar")
    )

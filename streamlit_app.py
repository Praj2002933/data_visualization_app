import pandas as pd
import streamlit as st

st.title('Data Visualization App')
upload_file = st.file_uploader("Upload your dataset", type=["csv", "txt"])
if upload_file is not None:
    data = pd.read_csv(upload_file)
    st.subheader('Display Data')
    st.dataframe(data)
    st.table(data.iloc[0:10])
    st.subheader('Summary Statistics')
    st.write(data.describe())
    st.subheader('Data Visualization')
    st.subheader('Area chart')
    selected_column_line=st.selectbox('Select a column for the area chart', data.columns)
    st.area_chart(data[selected_column_line])
    st.subheader('Bar chart')
    selected_column_bar = st.selectbox('Select a column for the bar chart', data.columns)
    st.bar_chart(data.index, data[selected_column_bar])
    st.subheader('Interactive Elements')
    num_points = st.slider("Select the number of data points to display", 1, len(data))
    selected_column_dropdown=st.selectbox('Select a column for the dropdown',data.columns)
    st.write(data.head(num_points))
    st.write(data[selected_column_dropdown].head(num_points))

!pip install matplotlib
!pip install pandas

import matplotlib.pyplot as plt
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
    st.subheader('Line Plot')
    selected_column_line=st.selectbox('Select a column for the line plot', data.columns)
    plt.plot(data[selected_column_line])
    st.pyplot()
    st.subheader('Bar Plot')
    selected_column_bar = st.selectbox('Select a column for the bar plot', data.columns)
    plt.bar(data.index, data[selected_column_bar])
    st.pyplot()
    st.subheader('Interactive Elements')
    num_points = st.slider("Select the number of data points to display", 1, len(data))
    selected_column_dropdown=st.selectbox('Select a column for the dropdown',data.columns)
    st.write(data.head(num_points))
    st.write(data[selected_column_dropdown].head(num_points))

import pandas as pd
import streamlit as st

st.title('Data Visualization App')
upload_file = st.file_uploader("Upload your dataset", type=["csv", "txt"])
if upload_file is not None:
    data = pd.read_csv(upload_file)
    st.subheader('Display Data')
    st.dataframe(data)
    st.table(data.head())
    st.subheader('Summary Statistics')
    st.write(data.describe())
    st.subheader('Data Visualization')
    st.subheader('Area chart')
    selected_column_line=st.selectbox('Select a column for the area chart', data.columns)
    st.area_chart(data[selected_column_line])
    st.subheader('Scatter chart')
    selected_column_line=st.selectbox('Select a column for the scatter chart', data.columns)
    st.scatter_chart(data[selected_column_line])
    st.subheader('Plotly chart')
    selected_column_line=st.selectbox('Select a column for the plotly chart', data.columns)
    st.plotly_chart(data[selected_column_line])
    st.subheader('Pydeck chart')
    selected_column_line=st.selectbox('Select a column for the pydeck chart', data.columns)
    st.pydeck_chart(data[selected_column_line])
    st.subheader('vega-lite chart')
    selected_column_line=st.selectbox('Select a column for the vega-lite chart', data.columns)
    st.vega_lite_chart(data[selected_column_line])
    

import pandas as pd
import streamlit as st

st.title('Data Visualization')
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
    selected_column_for_area_chart=st.selectbox('Select a column for the area chart', data.columns)
    st.area_chart(data[selected_column_for_area_chart])
    st.subheader('Scatter chart')
    selected_column_for_scatter_chart=st.selectbox('Select a column for the scatter chart', data.columns)
    st.scatter_chart(data[selected_column_for_scatter_chart])
    st.subheader('Line chart')
    selected_column_for_line_chart=st.selectbox('Select a column for the Line chart', data.columns)
    st.line_chart(data[selected_column_for_line_chart])
    st.subheader('Bar chart')
    selected_column_for_bar_chart=st.selectbox('Select a column for the Bar chart', data.columns)
    st.bar_chart(data[selected_column_for_bar_chart])
    st.balloons()
    st.snow()
    with st.sidebar:
         selected_area = st.sidebar.radio("Choose the plot to be viewed", ["Area", "Scatter", "Line", "Bar"])

if selected_area == "Area":
     st.area_chart(data[selected_column_for_area_chart])
elif selected_area == "Scatter":
     st.scatter_chart(data[selected_column_for_scatter_chart])
elif selected_area == "Line":
     st.line_chart(data[selected_column_for_line_chart])
else:
     st.bar_chart(data[selected_column_for_bar_chart])

           

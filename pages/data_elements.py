import streamlit as st
import pandas as pd

df = pd.read_csv('files/tips.csv')

# st.dataframe to display dataframes

st.header('st.dataframe')
st.caption('Display a dataframe as an interactive table')

st.dataframe(data=df,width=1000,height=100)
st.divider()

# st.static
st.header('st.table')
st.caption('Display a static table')

st.table(data=df.head(5))
st.divider()

# st.json
st.header('st.json')
st.caption('Display object or string as a pretty-printed JSON string')

json_values = df.head(3).to_dict()
st.json(json_values)


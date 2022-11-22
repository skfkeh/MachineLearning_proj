# app.py
import streamlit as st
import pandas as pd

st.title('Hello World!')

df = pd.DataFrame({
    'first column':[1, 2, 3, 4],
    'second column':[5, 6, 7, 8]
})

st.write(df)

selected1 = st.checkbox("I am box")
selected2 = st.checkbox("I am boy")
selected3 = st.checkbox("I am blue")

st.button('이걸 눌러봐라 닝겐')
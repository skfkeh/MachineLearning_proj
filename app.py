# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt # 시각화
from PIL import Image     # 이미지 처리 라이브러리


st.title('Hello World!')


path_to_annotation = "img/annotations/trimaps"
path_to_image = "img/images"

# 이미지 불러오기
annotation = Image.open(f"{path_to_annotation}/Abyssinian_1.png")
plt.subplot(1, 2, 1)
plt.title("annotation")
plt.imshow(annotation)

annotation = Image.open(f"{path_to_image}/Abyssinian_1.jpg")
plt.subplot(1, 2, 2)
plt.title("annotation")
plt.imshow(annotation)
plt.imshow(annotation)
plt.show()

selected1 = st.checkbox("I am box")
selected2 = st.checkbox("I am boy")
selected3 = st.checkbox("I am blue")

st.button('이걸 눌러봐라 닝겐')
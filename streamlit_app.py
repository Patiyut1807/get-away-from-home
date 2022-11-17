import streamlit as st
import pandas as pd


st.header("เบื่อแล้วอยู่บ้าน อยู่หอดีกว่า: 👏")
st.write("เว็บแอพสำหรับช่วยในการตัดสินใจเลือกหอพัก")
gender = st.selectbox(

    'Select the gender?',

    ('รวม','หญิง','ชาย'))
room = st.selectbox(

    'Select the Room type?',

    ('แอร์','พัดลม','สูท'))
price = st.slider('Price?', 2000, 12000, 4000)
distance = st.slider('Distance?', 900, 3000, 1000)
# distanceCheck = st.checkbox('I agree')

#displaying the selected option

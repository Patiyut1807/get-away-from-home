import streamlit as st
import pandas as pd
from calculate import calculate

st.header("เบื่อแล้วอยู่บ้าน อยู่หอดีกว่า: 👏")
st.write("เว็บแอพสำหรับช่วยในการตัดสินใจเลือกหอพัก")
gender = st.selectbox(

    'Select the gender?',

    ('รวม', 'หญิง', 'ชาย'))
room = st.selectbox(

    'Select the Room type?',

    ('แอร์', 'พัดลม', 'สูท'))
price = st.slider('Price?', 2000, 12000, 4000)
distance = st.slider('Distance?', 900, 3000, 1000)
# distanceCheck = st.checkbox('I agree')

# displaying the selected option
col1, col2, col3 = st.columns(3)
data = ""
with col2:
    if st.button('คำนวณ'):
        data = calculate(room, price, gender, distance)
if data != "":
    st.write(pd.DataFrame({
    'ชื่อหอ': [i[0][0] for i in data],
    'ประเภทห้อง': [i[0][1] for i in data],
    'ค่าเช่า': [i[0][2] for i in data],
    'ประเภทหอ': [i[0][3] for i in data],
    'ซอย': [i[0][4] for i in data],
    'ระยะทาง': [i[0][5] for i in data],
    'ค่าความคล้าย': [i[1] for i in data],
}))
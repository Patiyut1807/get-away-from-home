import streamlit as st
import pandas as pd
from calculate import calculate

st.header("เบื่อแล้วอยู่บ้าน อยู่หอดีกว่า: 👏")
st.write("เว็บแอพสำหรับช่วยในการตัดสินใจเลือกหอพัก")
gender = str(st.selectbox(

    'เลือกประเภทหอพัก?',

    ('รวม', 'ชาย', 'หญิง')))
room = str(st.selectbox(

    'เลือกประเภทห้องพัก?',

    ('แอร์', 'พัดลม', 'สูท')))
price = str(st.slider('ค่าเช่า?', 2000, 12000, 4000, 100))
distance = str(st.slider('ระยะทาง?', 900, 2500, 1000, 100))
# distanceCheck = st.checkbox('I agree')

# displaying the selected option
col1, col2, col3 = st.columns(3)
data = ""
with col2:
    if st.button('คำนวณ'):
        data, data_frame = calculate(room, price, gender, distance)
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
    st.write("ตารางค่าความคล้าย")
    st.caption("-> วิธีดูคือดูค่าของช่อง ผู้ใช้ ตรงกับหอต่างๆ")
    st.caption("-> ยิ่งค่าใกล้เคียง 1 มาก หมายความว่าหอมีความคล้ายกับข้อมูลที่เราใส่เข้าไปมาก")
    st.table(data_frame)

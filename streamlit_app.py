import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
choice = st.selectbox(

    'Select the Room type?',

    ('ชาย','หญิง','รวม'))



#displaying the selected option

st.write('You have selected:', choice)
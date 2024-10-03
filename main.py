import streamlit as st

st.title('Belajar Analisis Data dengan data Customer')

st.header('HI! Our Dear Customer')

st.subheader('Please fill Your Name')

st.metric(label="Temperature", value="28 °C", delta="1.2 °C")


name = st.text_input(label='Nama lengkap Customer', value='')
st.write('Nama: ', name)


number = st.number_input(label='Umur')
st.write('Umur: ', int(number), ' tahun')


if st.button('Say hello'):
    st.write('Hello there')
 
with st.sidebar:
    
    st.text('Ini merupakan sidebar')
    
    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)

pip install pandas matplotlib seaborn streamlit Babel
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')
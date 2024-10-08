import streamlit as st

st.title("Welcome to My Streamlit App!")

st.header('HI! Our Dear Customer')

st.subheader('Please fill Your Name')

Name = st.text_input(label='Full Name', value='')

City = st.text_input(label='City', value='')

State = st.text_input(label='State', value='')

CustomerID = st.text_input(label='Customer ID', value='')
 
with st.sidebar:
    
    st.text('Ini merupakan sidebar')
    
    values = st.slider(
        label='Select a range of values',
        min_value=0, max_value=100, value=(0, 100)
    )
    st.write('Values:', values)
    
import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://i.pinimg.com/564x/ed/6b/be/ed6bbe5838979e5bca84c998cd2a87e6.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

import streamlit as st
import matplotlib.pyplot as plt

# Misal data telah dimuat, jika belum, pastikan kamu memuatnya dari file atau sumber lain
# Contoh memuat data (jika data belum di-load)
# import pandas as pd
# data = pd.read_csv('path_to_your_data.csv')

# Menghitung 10 kota teratas
city_counts = data["customer_city"].value_counts().head(10)

# Membuat plot menggunakan matplotlib
fig, ax = plt.subplots()
ax.barh(city_counts.index, city_counts.values)
ax.set_xlabel("Number of Customers")
ax.set_title("Top 10 Cities by Number of Customers")

# Menambahkan label ke setiap bar
for index, value in enumerate(city_counts.values):
    ax.text(value, index, str(value))

# Menampilkan plot di Streamlit
st.pyplot(fig)



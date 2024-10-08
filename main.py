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

if st.button("Sign In"):
    st.write("You clicked on Sign In!")
    # Tambahkan logika untuk proses Sign In di sini

# Tombol Sign Up
if st.button("Sign Up"):
    st.write("You clicked on Sign Up!")




import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Menghitung 10 kota teratas
city_counts = data["customer_city"].value_counts().head(10)

# Mengatur subheader
st.subheader("Top 10 Cities by Number of Customers")

# Membuat plot dengan subplots (seperti pada contoh kedua)
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 10))

# Membuat barplot horizontal
colors = ["#90CAF9" if i == 0 else "#D3D3D3" for i in range(len(city_counts))]
sns.barplot(x=city_counts.values, y=city_counts.index, palette=colors, ax=ax)

# Mengatur label dan title
ax.set_xlabel("Number of Customers", fontsize=20)
ax.set_title("Top 10 Cities by Number of Customers", loc="center", fontsize=30)
ax.tick_params(axis='y', labelsize=15)
ax.tick_params(axis='x', labelsize=15)

# Menambahkan label ke setiap bar
for index, value in enumerate(city_counts.values):
    ax.text(value, index, str(value), fontsize=15)

# Menampilkan plot di Streamlit
st.pyplot(fig)





tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
 
with tab1:
    st.header("Tab 1")
    st.image("https://static.streamlit.io/examples/cat.jpg")
 
with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")
 
with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")


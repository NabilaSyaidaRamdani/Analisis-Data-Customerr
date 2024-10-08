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

# Membuat tombol Sign In
if st.button('Sign In'):
    # Membuka tab baru menggunakan JavaScript
    js = """
    <script type="text/javascript">
        window.open('https://your-sign-in-url.com', '_blank').focus();
    </script>
    """
    st.markdown(js, unsafe_allow_html=True)
 
# Tombol Sign Up
if st.button("Sign Up"):
    st.write("You clicked on Sign Up!")

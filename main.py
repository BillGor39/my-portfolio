import streamlit as st

st.set_page_config(layout="wide")

st.title("Home")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Edward")
    content = """
    Hi, My name is Edward. I graduated from university of Canterbury with Bachelor's degree in computer science 
     and I am currently studying a master degree in Applied Computing. I am trying to enhance my skills and do more 
     practice through the course from Udemy. I am learning the Web development via this project. 
    """
    st.info(content)
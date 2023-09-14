import pickle
import streamlit as st
import numpy as np
from main import recommend_book

st.title("BookMeABook")
model = pickle.load(open('models/model.pkl','rb'))
book_names = pickle.load(open('models/book_names.pkl','rb'))
final_rating = pickle.load(open('models/final_rating.pkl','rb'))
book_pivot = pickle.load(open('models/book_pivot.pkl','rb'))



book_selection = st.selectbox("Type or choose the book name from the list", book_names)

if st.button('Show Recommendation'):
    book_recomm, image_url = recommend_book(book_selection)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(book_recomm[1])
        st.image(image_url[1])
    
    with col2:
        st.text(book_recomm[2])
        st.image(image_url[2])

    with col3:
        st.text(book_recomm[3])
        st.image(image_url[3])

    with col4:
        st.text(book_recomm[4])
        st.image(image_url[4])

    with col5:
        st.text(book_recomm[5])
        st.image(image_url[5])     




st.subheader("", divider='rainbow')
st.markdown('_by Alper Gulcuoglu_') 

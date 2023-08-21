import streamlit as st
#We remove only from the cultivated_in table
from database import delete_plant

def remove():
    col1,col2=st.columns(2)
    with col1:
        plant=st.text_input("Plant id")
    with col2:
        garden_id=st.text_input("Garden_id")
    if st.button("Remove Plant"):
        delete_plant(plant,garden_id)
        st.success("Successfully removed")
    
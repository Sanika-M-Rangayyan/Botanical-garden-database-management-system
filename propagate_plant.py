import streamlit as st
from database import add_data
from database import add_parent_kid_data
def propagate():
    col1,col2=st.columns(2)
    with col1:
        baby_plant=st.text_input("Baby Plant id")
        baby_plant_garden_id=st.text_input("Baby Plant Garden id")
        baby_plant_sn=st.text_input("Baby Plant Scientific Name")
        baby_plant_ln=st.text_input("Baby Plant Local Name")
    with col2:
        mother_plant=st.text_input("Mother Plant id")
    if st.button("Add Plant"):
        add_data(baby_plant,baby_plant_sn,baby_plant_ln,baby_plant_garden_id)
        add_parent_kid_data(baby_plant,mother_plant)
        st.success("Successfully added")
    
import streamlit as st
from database import add_data
def new_plant():
	col1,col2=st.columns(2)
	with col1:
		plant_id=st.text_input("Plant id")
		scientific_name=st.text_input("scientific name")
	with col2:
		local_name =st.text_input("local name")
		garden_id=st.text_input("garden id")
	if st.button("Add Plant"):
		add_data(plant_id,scientific_name,local_name,garden_id)
		st.success("Successfully added")
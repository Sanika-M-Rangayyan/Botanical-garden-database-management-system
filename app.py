import streamlit as st

from add_new import new_plant
from propagate_plant import propagate
from remove_plant import remove
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
def main():
    add_bg_from_local('c.jpg')
    st.title("BOTANICAL GARDEN DATABASE")
    menu = ["New","Propagate","Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "New":
        st.subheader("Onboarding the new plant")
        new_plant()
    elif choice == "Propagate":
        st.subheader("Propagated plant")
        propagate()
    elif choice == "Remove":
        st.subheader("Removing Plant")
        remove()
    else:
        st.subheader("About tasks")
if __name__ == '__main__':
    main()

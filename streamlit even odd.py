import streamlit as st
st.title("EVEN OR ODD")
NUM1 = st.number_input("enter number",min_value=1,step=1)
if st.button("Even/odd"):
    if NUM1%2 == 0:
        st.success("EVEN NUMBER")
    else:
        st.error("ODD NUMBER")
import streamlit as st
import stramlit_analytics

with streamlit_analytics.track():
  st.text_input("Write your name")
  st.selectbox("Select your favourite",["guvi","data","science"])
  st.button("Click me")

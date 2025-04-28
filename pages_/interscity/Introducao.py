import streamlit as st
from utils.slide import get_slide


get_slide(markdown_path="./static/introducao.md")
if st.button(":blue-background[Saiba mais] sobre os microsserviços da plataforma InterSCity", type="tertiary", icon=":material/lightbulb:"):
    st.session_state.sidebar_state = 'expanded'
    st.rerun()
import streamlit as st
from utils.slide import get_slide
from utils.menu import render_menu


get_slide(markdown_path="./static/introducao.md")
st.button(
    ":blue-background[Experimente] cada microsserviço InterSCity pelo :blue-background[menu abaixo]",
    type="tertiary",
    icon=":material/lightbulb:",
)
render_menu()

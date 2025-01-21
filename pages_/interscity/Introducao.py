import streamlit as st
import reveal_slides as rs
from pathlib import Path


if st.button(":blue-background[Saiba mais] sobre os microsserviços da plataforma InterSCity", type="tertiary", icon=":material/lightbulb:"):
    st.session_state.sidebar_state = 'collapsed' if st.session_state.sidebar_state == 'expanded' else 'expanded'
    st.rerun()
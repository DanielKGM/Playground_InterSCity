import streamlit as st
import reveal_slides as rs
from pathlib import Path


st.header("InterSCity")
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

st.caption(r"""Pressione `F` para ler os slides em tela cheia""")
rs.slides(read_markdown_file("./static/catalog.md"), 
    height=500, 
    theme="moon", 
    config={
            "transition": "slide",
            "width": 900, 
            "height": 900, 
            "minScale": 0.1, 
            "center": True,
            "progress": False,
            "maxScale": 3, 
            "controlsLayout": 'bottom-right',
            "margin": 0.1, 
            "plugins": ["highlight"]
            }, 
    initial_state={
                    "indexh": 0, 
                    "indexv": 0, 
                    "indexf": -1, 
                    "paused": False, 
                    "overview": False
                    },
    markdown_props={"data-separator-vertical":"^--$"}, 
    key="foo")

if st.button(label=":blue-background[Saiba mais] sobre a plataforma", type="tertiary", icon=":material/lightbulb:"):
    st.session_state.sidebar_state = 'expanded' if st.session_state.sidebar_state == 'collapsed' else 'collapsed'
    st.rerun()
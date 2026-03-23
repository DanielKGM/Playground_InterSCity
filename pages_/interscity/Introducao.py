import streamlit as st
import reveal_slides as rs
from pathlib import Path
from utils.menu import render_menu
from datetime import date


def get_slide(markdown_path: str):
    try:
        return rs.slides(
            Path(markdown_path).read_text(encoding="UTF-8"),
            height=400,
            theme="moon",
            config={
                "transition": "slide",
                "width": 1000,
                "height": 1000,
                "minScale": 0.1,
                "center": True,
                "progress": False,
                "maxScale": 3,
                "controlsLayout": "bottom-right",
                "margin": 0,
                "plugins": ["highlight"],
            },
            markdown_props={"data-separator-vertical": "^--$"},
            key="foo",
            display_only=True,
        )
    except FileNotFoundError:
        return None


st.caption(r"""Clique no slide e pressione `F` para ler em tela cheia""")

get_slide(markdown_path="./static/introducao.md")

st.button(
    ":blue-background[Experimente] cada microsserviço InterSCity pelo :blue-background[menu abaixo]",
    type="tertiary",
    icon=":material/lightbulb:",
)

render_menu()

st.space("small")

st.caption(
    f"**Playground InterSCity** • Criado e mantido por [Daniel Galdez](https://github.com/DanielKGM/Playground_InterSCity) • 2025 - {date.today().year}"
)

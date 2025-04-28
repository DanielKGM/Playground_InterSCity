import streamlit as st
import validators
from config import get_base_url
from utils.menu import render_menu, pages_config


# transformação em st.Page para o st.navigation
pages = {}
for section, pg_list in pages_config.items():
    pages[section] = [
        st.Page(
            p["path"],
            title=p["title"],
            icon=p["icon"],
            default=p.get("default", False)
        )
        for p in pg_list
    ]

pg = st.navigation(pages, position="hidden")

with st.sidebar:
    render_menu()
    
    st.markdown("**API**", help="Endereço o qual as requisições da API serão feitas")

    url_input = st.sidebar.text_input(
        "URL Base da API",
        label_visibility="collapsed",
        value=get_base_url(),
        key="input_api"
    )

    if not validators.url(url_input):
        st.sidebar.error("URL inválida!")
    else:
        st.session_state["base_url"] = url_input

if pg.title != "Introdução":
    st.header(pg.title)

st.session_state.page = pg.title
st.logo(image="./static/icon.svg",size="large",link="https://interscity.org/software/interscity-platform/")
pg.run()

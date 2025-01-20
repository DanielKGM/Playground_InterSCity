import streamlit as st
from utils.fetch_cached_data import clear_cache
import reveal_slides as rs
from pathlib import Path


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

def generate_playground(service: any, title:str, markdown_path:str = None):
    st.header(title)

    if markdown_path:
        st.caption(r"""Pressione `F` para ler os slides em tela cheia""")
        rs.slides(read_markdown_file(markdown_path), 
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
    else:
        st.info("Apresentação indisponível!")
    
    col1, col2 = st.columns(vertical_alignment= "bottom", spec= [0.8,0.2])
    with col1:
        st.subheader("Formulário de Requisição")
    with col2:
        st.button("Limpar Cache", help="Pode ajudar a resolver problemas na aplicação", on_click= clear_cache,type= "tertiary", icon=":material/restart_alt:", use_container_width= True)

    response = service.form("playground")

    st.subheader("Resposta da API")
    if response is None:
        st.info("Aqui serão exibidos os resultados da sua requisição", icon= ":material/visibility:")
    elif response.get("error"):
        st.error(f'{response["error"]} ({response["status_code"]})', icon= ":material/sentiment_dissatisfied:")
    else:
        st.json(response)
import streamlit as st
from utils.fetch_cached_data import clear_cache
from utils.presentations import presentation


def generate_playground(service: any, presentation_key, titulo):
    st.header(titulo)
    if presentation(presentation_key) is None:
        st.info("Apresentação indisponível!", icon= ":material/scan_delete:")

    col1, col2 = st.columns(vertical_alignment= "bottom", spec= [0.8,0.2])
    with col1:
        st.header("Playground")
    with col2:
        st.button("Limpar Cache", help="Pode ajudar a resolver problemas na aplicação", on_click= clear_cache,type= "tertiary", icon=":material/restart_alt:", use_container_width= True)

    response = service.form("catalog_playground")

    st.header("Resposta")
    if response is None:
        st.info("Aqui serão exibidos os resultados da sua requisição", icon= ":material/visibility:")
    elif response.get("error"):
        st.error(f'{response["error"]} ({response["status_code"]})', icon= ":material/sentiment_dissatisfied:")
    else:
        st.json(response)
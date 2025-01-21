import streamlit as st
from utils.fetch_cached_data import clear_cache


def generate_playground(service: any):
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
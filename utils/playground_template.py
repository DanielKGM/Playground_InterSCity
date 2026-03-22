import streamlit as st
from utils.fetch_cached_data import clear_cache
from utils.http_container import http_container


def generate_playground(service: any):
    col1, col2 = st.columns(vertical_alignment="bottom", spec=[0.8, 0.2])
    with col1:
        st.subheader("Formulário de Requisição")
    with col2:
        st.button(
            "Limpar Cache",
            help="Pode ajudar a resolver problemas na aplicação",
            on_click=clear_cache,
            type="tertiary",
            icon=":material/restart_alt:",
            width="stretch",
        )

    request_info, response = service.form("playground")

    st.subheader(
        "Detalhes da Requisição",
        help="Exibe a estrutura exata da requisição HTTP que será enviada, incluindo o método, a rota e os dados (payload) ou parâmetros.",
    )
    if request_info:
        st.html(http_container(**request_info))
    else:
        st.info(
            "Aguardando formulário de requisição...", icon=":material/hourglass_empty:"
        )

    st.subheader(
        "Resposta da API",
        help="Mostra o retorno da API no formato JSON, exibindo os dados solicitados, confirmações ou mensagens de erro.",
    )
    if response is None:
        st.info(
            "Aqui serão exibidos os resultados da sua requisição",
            icon=":material/visibility:",
        )
    elif response.get("error"):
        st.error(
            f'{response["error"]} ({response["status_code"]})',
            icon=":material/sentiment_dissatisfied:",
        )
    else:
        st.json(response)

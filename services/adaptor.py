import streamlit as st
from utils.fetch_cached_data import request
from utils.fetch_cached_data import fetch_capabilities_from_resource
from config import get_base_url


class AdaptorService:
    def __init__(self, lista_capacidades: list = None, lista_recursos: list = None):
        self.lista_capacidades = lista_capacidades
        self.lista_recursos = lista_recursos

    def data_formater(self, data, unica: bool):
        if unica:
            return [
                {"value": item["Valor"], "timestamp": item["Timestamp"]}
                for item in data
                if item["Valor"] and item["Timestamp"]
            ]
        else:
            formatted_data = {}
            for item in data:
                capacidade = item.get("Capacidade")
                valor = item.get("Valor")
                timestamp = item.get("Timestamp")

                if capacidade and valor and timestamp:
                    if capacidade not in formatted_data:
                        formatted_data[capacidade] = []
                    formatted_data[capacidade].append(
                        {"value": valor, "timestamp": timestamp}
                    )

            return formatted_data

    def data_fields(self, resource_caps: list, unica: bool = False):
        columns = {"Capacidade": None, "Valor": None, "Timestamp": None}
        if unica:
            columns.pop("Capacidade", None)

        caps = st.data_editor(
            data=[columns],
            column_config={
                "Capacidade": st.column_config.SelectboxColumn(
                    options=resource_caps, required=True
                ),
                "Timestamp": st.column_config.DatetimeColumn(
                    required=True,
                    label="Timestamp",
                    help="Momento em que os dados foram capturados",
                ),
                "Valor": st.column_config.NumberColumn(format="%d", required=True),
            },
            num_rows="dynamic",
            width="stretch",
            hide_index=True,
        )

        return self.data_formater(caps, unica)

    def form(self, key: str):
        method = "POST"
        base_endpoint = "/adaptor/resources"
        capability = None

        if not self.lista_recursos:
            st.warning("Nenhum recurso encontrado no cache/API.")
            return None

        opcoes_uuid = (
            list(self.lista_recursos.keys())
            if isinstance(self.lista_recursos, dict)
            else self.lista_recursos
        )

        def formatador_seguro(x):
            if isinstance(self.lista_recursos, dict):
                valor = self.lista_recursos.get(x)
                return str(valor) if valor is not None else str(x)
            return str(x)

        uuid = st.selectbox(
            "Escolha um recurso para publicar os dados",
            options=opcoes_uuid,
            format_func=formatador_seguro,
        )

        if not uuid:
            return None, None

        resource_caps = fetch_capabilities_from_resource(uuid, base_url=get_base_url())

        if not resource_caps or resource_caps == []:
            st.info("O recurso selecionado não possui capacidades")
            return None, None

        unica = st.toggle(
            "Enviar para capacidade única",
            help="Envia todo contexto para uma única capacidade (contida no recurso informado)",
        )

        if unica:
            capability = st.selectbox(
                label="nome_capacidade",
                help="Nome da capacidade-alvo",
                options=resource_caps,
            )

        with st.form(key, border=False, enter_to_submit=False):
            data = {"data": self.data_fields(resource_caps, unica)}
            submitted = st.form_submit_button(
                label="Enviar",
                width="stretch",
                icon=":material/line_end_arrow_notch:",
                icon_position="right",
                type="secondary",
            )

        endpoint = f"{base_endpoint}/{uuid}/data"

        if unica and capability:
            endpoint = f"{endpoint}/{capability}"

        request_info = {"method": method, "endpoint": endpoint, "content": data}

        if submitted:
            st.toast("Comunicando-se com a API...", icon=":material/hourglass_empty:")
            response = request(method, endpoint, data=data, base_url=get_base_url())

            if response.get("error"):
                st.toast(
                    f'{response["error"]} ({response["status_code"]})',
                    icon=":material/sentiment_dissatisfied:",
                )
            else:
                st.toast(
                    "Requisição concluída com sucesso!",
                    icon=":material/sentiment_satisfied:",
                )

            return request_info, response

        return request_info, None

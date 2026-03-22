import streamlit as st
from utils.fetch_cached_data import request
from typing import Dict
from utils.fetch_cached_data import request
from config import get_base_url


class DiscoveryService:
    def __init__(self, lista_capacidades: list = None):
        self.lista_capacidades = lista_capacidades
        self.operacoes_map = {
            "=": "eq",
            "!=": "ne",
            ">": "gt",
            ">=": "gte",
            "<": "lt",
            "<=": "lte",
        }

    def remove_empty_fields(self, data: Dict) -> Dict:
        return {
            key: value
            for key, value in data.items()
            if value not in [0, None, "", [], {}]
        }

    def data_formater(self, data):
        query_params = {}
        query_params["capability"] = []

        for item in data:
            capability = item["Capacidade"]

            if not capability:
                continue

            if capability not in query_params["capability"]:
                query_params["capability"].append(capability)

            matcher = self.operacoes_map.get(item["Operação"], None)
            value = item["Valor"]
            key = f"{capability}.{matcher}"

            if matcher and value:
                if not query_params.get(key):
                    query_params[key] = value
            else:
                continue

        return query_params

    def search_fields(self):
        st.html(
            """<p style="margin-top:2px; margin-bottom:-10px; font-size:0.9rem;">Capacidades</p>"""
        )
        caps = st.data_editor(
            data=[{"Capacidade": None, "Operação": None, "Valor": None}],
            column_config={
                "Capacidade": st.column_config.SelectboxColumn(
                    options=self.lista_capacidades, help="Nome da capacidade"
                ),
                "Operação": st.column_config.SelectboxColumn(
                    options=self.operacoes_map.keys()
                ),
                "Valor": st.column_config.NumberColumn(format="%d"),
            },
            num_rows="dynamic",
            width="stretch",
            hide_index=True,
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            lat = st.number_input("Latitude", format="%.6f")

        with col2:
            lon = st.number_input("Longitude", format="%.6f")

        with col3:
            radius = st.number_input("Raio (em metros)", min_value=0)

        return self.remove_empty_fields(
            {
                **{
                    "lat": lat,
                    "lon": lon,
                    "radius": radius,
                },
                **self.data_formater(caps),
            }
        )

    def form(self, key: str):
        method = "GET"
        endpoint = "/discovery/resources"

        with st.form(key, border=False, enter_to_submit=False):
            params = self.search_fields()
            submitted = st.form_submit_button(
                label="Enviar",
                width="stretch",
                icon=":material/line_end_arrow_notch:",
                icon_position="right",
                type="secondary",
            )

        request_info = {"method": method, "endpoint": endpoint, "params": params}

        if submitted:
            st.toast("Comunicando-se com a API...", icon=":material/hourglass_empty:")

            response = request(method, endpoint, params=params, base_url=get_base_url())

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

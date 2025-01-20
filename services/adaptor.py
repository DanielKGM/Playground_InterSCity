import streamlit as st
from utils.fetch_cached_data import request
from utils.http_container import http_container
from utils.fetch_cached_data import fetch_capabilities_from_resource


class AdaptorService():
    def __init__(self, lista_capacidades: list = None, lista_recursos: list = None):
        self.lista_capacidades = lista_capacidades
        self.lista_recursos = lista_recursos

    def data_formater(self, data, unica: bool):
        if unica:
            return [{"value": item["Valor"], "timestamp": item["Timestamp"]} for item in data if item["Valor"] and item["Timestamp"]]
        else:
            formatted_data = {}
            for item in data:
                capacidade = item.get("Capacidade")
                valor = item.get("Valor")
                timestamp = item.get("Timestamp")

                if capacidade and valor and timestamp:
                    if capacidade not in formatted_data:
                        formatted_data[capacidade] = []
                    formatted_data[capacidade].append({"value": valor, "timestamp": timestamp})

            return formatted_data
    
    def data_fields(self, resource_caps: list, unica: bool = False):
        columns = {"Capacidade": None,"Valor": None, "Timestamp": None}
        if unica:
            columns.pop("Capacidade",None)
        
        caps = st.data_editor(
            data=[columns],
            column_config={
                "Capacidade": st.column_config.SelectboxColumn(options=resource_caps),
                "Timestamp": st.column_config.DatetimeColumn(),
                "Valor": st.column_config.TextColumn()
            },
            num_rows="dynamic",
            use_container_width=True,
            hide_index=True
        )
        
        return self.data_formater(caps, unica)

    def form(self, key: str):
        method = "POST"
        endpoint = "/adaptor/resources"
        http_cont = st.html(http_container(method, endpoint + "/{uuid_recurso}/data"))
        capability = None

        uuid = st.selectbox(
            "Escolha um recurso para publicar os dados",
            self.lista_recursos,
            format_func= lambda x: self.lista_recursos.get(x)
        )

        if not uuid:
            return None

        resource_caps = fetch_capabilities_from_resource(uuid)
        if resource_caps == []:
            st.info("O recurso selecionado não possui capacidades")
            return None

        unica = st.toggle("Enviar para capacidade única", help="Envia todo contexto para uma única capacidade (contida no recurso informado)")

        if unica:
            http_cont.html(http_container(method, endpoint + "/{uuid_recurso}/data/{nome_capacidade}"))
            capability = st.selectbox(label="nome_capacidade", 
                                      help="Nome da capacidade-alvo", 
                                      options=resource_caps)

        with st.form(key, border=False, enter_to_submit=False):
            data = {"data": self.data_fields(resource_caps, unica)}

            if st.form_submit_button("Enviar ╰┈➤", use_container_width=True):
                endpoint = f"{endpoint}/{uuid}/data"
                
                if unica and capability:
                    endpoint = f"{endpoint}/{capability}"

                st.toast("Comunicando-se com a API...", icon= ":material/hourglass_empty:")
                response = request(
                                method, 
                                endpoint, 
                                data= data
                            )
                http_cont.html(http_container(method,endpoint, content=data))
                if response.get("error"):
                    st.toast(f'{response["error"]} ({response["status_code"]})', icon=":material/sentiment_dissatisfied:")
                else:
                    st.toast("Requisição concluída com sucesso!", icon= ":material/sentiment_satisfied:")
                return response

        return None
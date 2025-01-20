import streamlit as st
from utils.fetch_cached_data import request
from typing import Dict
from utils.http_container import http_container
from utils.fetch_cached_data import request


class CollectorService():
    def __init__(self, lista_capacidades: list = None, lista_recursos: list = None):
        self.lista_capacidades = lista_capacidades
        self.lista_recursos = lista_recursos
        self.operacoes_map = {
            "=":"eq",
            "!=":"ne",
            ">":"gt",
            ">=":"gte",
            "<":"lt",
            "<=":"lte"
        }

    def remove_empty_fields(self, data: Dict) -> Dict:
        return {key: value for key, value in data.items() if value not in [0, None, "", [], {}]}
    
    def data_formater(self, data):
        query_params = {}
        query_params["capabilities"] = []
        query_params["matchers"] = {}

        for item in data:
            capability = item["Capacidade"]

            if not capability:
                continue

            if capability not in query_params["capabilities"]:
                query_params["capabilities"].append(capability)

            matcher = self.operacoes_map.get(item["Operação"], None)
            value = item["Valor"]
            key = f"{capability}.{matcher}"

            if matcher and value:
                if not query_params["matchers"].get(key):
                    query_params["matchers"][key] = value
            else:
                continue
        
        return query_params
    
    def data_fields(self, last: bool = False):
        start_date, end_date = None, None
        if not last:
            col1, col2 = st.columns(2)
            
            with col1:
                start_day = st.date_input("Início do intervalo",format="YYYY-MM-DD",value=None)
                start_hour = st.time_input("aa",label_visibility="collapsed", value= None)

            with col2:
                end_day = st.date_input("Fim do intervalo",format="YYYY-MM-DD", value = None)
                end_hour = st.time_input("aas",label_visibility="collapsed", value=None)
            
            if start_date and end_date and start_hour and end_hour:
                start_date, end_date = f"{start_day}T{start_hour}", f"{end_day}T{end_hour}"
        
        uuids = st.multiselect("Recursos (uuids)", 
                    self.lista_recursos,
                    format_func= lambda x: self.lista_recursos.get(x),
                    placeholder= "Escolha uma opção")
        
        st.html('''<p style="margin-top:2px; margin-bottom:-10px; font-size:0.9rem;">Capacidades</p>''')
        caps = st.data_editor(
                    data=[{"Capacidade":"","Operação":"","Valor":""}],
                    column_config={
                        "Capacidade": st.column_config.SelectboxColumn(
                            options=self.lista_capacidades,
                            help="Nome da capacidade"
                            ),
                        "Operação": st.column_config.SelectboxColumn(
                            options=self.operacoes_map.keys()
                            ),
                        "Valor": st.column_config.TextColumn()
                    },
                    num_rows="dynamic",
                    use_container_width= True,
                    hide_index=True
                    )
        
        return self.remove_empty_fields({**{
            "start_date": start_date,
            "end_date": end_date,
            "uuids": uuids,
        }, **self.data_formater(caps)})

    def form(self, key: str):
        method = "POST"
        endpoint = "/collector/resources/data"
        http_cont = st.html(http_container(method, f"{endpoint}/{{last}}"))
        last = st.toggle("Mais recente (last)")
        
        with st.form(key, border= False, enter_to_submit= False):
            data = self.data_fields(last)
            if st.form_submit_button("Enviar ╰┈➤",use_container_width= True):
                if last:
                    endpoint += "/last"

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
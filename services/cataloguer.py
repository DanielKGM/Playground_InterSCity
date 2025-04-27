import streamlit as st
from utils.fetch_cached_data import request
from typing import Dict
from utils.http_container import http_container
from config import get_base_url
import re


class CataloguerService():
    def __init__(self, lista_capacidades: list = None):
        self.lista_capacidades = lista_capacidades
        self.action_map = {
            "Criar um recurso": {
                "endpoint": "/catalog/resources",
                "method": "POST",
                "data": self.resource_fields,
            },
            "Obter um recurso": {
                "endpoint": "/catalog/resources/{uuid}",
                "method": "GET",
                "path_param": "{uuid} do recurso",
            },
            "Atualizar um recurso": {
                "endpoint": "/catalog/resources/{uuid}",
                "method": "PUT",
                "path_param": "{uuid} do recurso",
                "data": self.resource_fields
            },
            "Listar todos os recursos": {
                "endpoint": "/catalog/resources",
                "method": "GET",
            },
            "Listar recursos com sensores": {
                "endpoint": "/catalog/resources/sensors",
                "method": "GET",
            },
            "Listar recursos com atuadores": {
                "endpoint": "/catalog/resources/actuators",
                "method": "GET",
            },
            "Pesquisar recursos": {
                "endpoint": "/catalog/resources/search",
                "method": "GET",
                "params": self.search_fields,
            },
            "Criar uma capacidade": {
                "endpoint": "/catalog/capabilities",
                "method": "POST",
                "data": self.capability_fields
            },
            "Excluir uma capacidade": {
                "endpoint": "/catalog/capabilities/{nome}",
                "method": "DELETE",
                "path_param": "{nome} da capacidade",
            },
            "Obter uma capacidade": {
                "endpoint": "/catalog/capabilities/{nome}",
                "method": "GET",
                "path_param": "{nome} da capacidade",
            },
            "Atualizar uma capacidade": {
                "endpoint": "/catalog/capabilities/{nome}",
                "method": "PUT",
                "path_param": "{nome} da capacidade",
                "params": self.capability_fields
            },
            "Listar todas as capacidades": {
                "endpoint": "/catalog/capabilities",
                "method": "GET",
            }
        }


    def remove_empty_fields(self, data: Dict) -> Dict:
        return {key: value for key, value in data.items() if value not in [0, None, "", [], {}]}
    
    def capability_fields(self, edit: bool = False):
        return self.remove_empty_fields({
            "name": st.text_input("Nome", placeholder="Sensor de temperatura"),
            "capability_type": st.selectbox("Tipo", ['sensor', 'actuator'],help="Sensor: sente o ambiente; Actuador: modifica o ambiente", disabled= edit),
            "description": st.text_input("Descrição", placeholder= "Mede a temperatura da sala")
        })
    
    def resource_fields(self):
        col1, col2 = st.columns(2)

        with col1:
            description = st.text_input("Descrição", placeholder= "Estacionamento em São Luís", help= "Uma descrição curta do recurso")
            lat = st.number_input("Latitude", format="%.6f")
            collect_interval = st.number_input("Intervalo de Coleta (segundos)", min_value=0,help= "Valor numérico, em segundos, que corresponde ao intervalo de coleta de dados")

        with col2:
            status = st.selectbox("Status", ['active', 'inactive', None])
            lon = st.number_input("Longitude", format="%.6f")
            uri = st.text_input("URI", placeholder= "exemplo.com", help="Unified Resource Identifier")

        return {"data" : self.remove_empty_fields({
            "uri": uri,
            "lat": lat,
            "lon": lon,
            "status": status,
            "collect_interval": collect_interval,
            "description": description,
            "capabilities": st.multiselect("Capacidades", 
                                           self.lista_capacidades,
                                           placeholder= "Escolha uma opção")
        })}
    
    def search_fields(self):
        col1, col2 = st.columns(2)
        
        with col1:
            capability = st.multiselect("Capacidades", 
                        self.lista_capacidades,
                        placeholder= "Escolha uma opção")
            lat = st.number_input("Latitude", format="%.6f")
            postal_code = st.text_input("Código Postal", help="Formato: XXXXX-XXX", placeholder="XXXXX-XXX")
            neighborhood = st.text_input("Bairro")
        
        with col2:
            status = st.selectbox("Status", [None,'active', 'inactive'])
            lon = st.number_input("Longitude", format="%.6f")
            city = st.text_input("Cidade")
            radius = st.number_input("Raio (em metros)", min_value=0)

        return self.remove_empty_fields({
            "capability": capability,
            "status": status,
            "postal_code": postal_code,
            "neighborhood": neighborhood,
            "city": city,
            "lat": lat,
            "lon": lon,
            "radius": radius,
        })

    def form(self, key: str):
        action_name = st.selectbox(
            "Escolha um tipo de requisição",
            self.action_map.keys(),
        )

        action = self.action_map[action_name]
        endpoint = action["endpoint"]
        http_cont = st.html(http_container(action["method"],endpoint))

        with st.form(key, border= False, enter_to_submit= False):
            path_param = None
            if action.get("path_param"):
                path_param = st.text_input(action["path_param"])
            data = action["data"]() if action.get("data") else None
            params = action["params"]() if action.get("params") else None

            if st.form_submit_button("Enviar ╰┈➤",use_container_width= True):
                if path_param:
                    endpoint = re.sub(r"\{(\w+)\}", path_param, endpoint)
                st.toast("Comunicando-se com a API...", icon= ":material/hourglass_empty:")

                response = request(
                                method=action["method"],
                                endpoint=endpoint,
                                params=params, 
                                data=data,
                                headers={"Content-Type": "application/json"},
                                base_url=get_base_url()
                            )
                http_cont.html(http_container(action["method"],endpoint,data, params))
                
                if response.get("error"):
                    st.toast(f'{response["error"]} ({response["status_code"]})', icon=":material/sentiment_dissatisfied:")
                else:
                    st.toast("Requisição concluída com sucesso!", icon= ":material/sentiment_satisfied:")
                return response
        return None

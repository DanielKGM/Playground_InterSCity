from services.api_client import APIClient
from streamlit import cache_data
from typing import Dict, Optional, Any
import json


@cache_data(show_spinner="Buscando dados...")
def fetch_capabilities() -> list[str]:
    api = APIClient()
    res = api.request("GET", "/catalog/capabilities")
    content = res.get("response_content", {})
    
    if "capabilities" in content:
        capabilities = content["capabilities"] 
        names = [capability["name"] for capability in capabilities if "name" in capability]
        return names
    return []

@cache_data(
show_spinner="Buscando dados...",
hash_funcs={
    dict: lambda d: json.dumps(d, sort_keys=True)  # Serializa dicionários para uma string ordenada
})
def request(
    method: str, 
    endpoint:str, 
    path_param: str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = {"Content-Type": "application/json"}
):
    api = APIClient()
    return api.request(method, endpoint, path_param,params, data, headers)
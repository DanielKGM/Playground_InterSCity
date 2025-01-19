from services.api_client import APIClient
from streamlit import cache_data
from typing import Dict, Optional, Any
import json


def clear_cache():
    cache_data.clear()
    
@cache_data(show_spinner="Buscando dados...", max_entries=1)
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
    max_entries= 1,
    hash_funcs={
        dict: lambda d: json.dumps(d, sort_keys=True)  # Serializa dicionários para uma string ordenada
})
def request(
    method: str, 
    endpoint:str, 
    path_param: str = None,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None
):
    api = APIClient()
    return api.request(method, endpoint, path_param,params, data, headers)
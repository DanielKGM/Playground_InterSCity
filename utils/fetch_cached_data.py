from services.api_client import APIClient
from streamlit import cache_data, session_state
from typing import Dict, Optional, Any
import json
from config import get_base_url



def clear_cache():
    cache_data.clear()

def get_content(endpoint, base_url):
    api = APIClient(base_url)
    res = api.request("GET", endpoint)
    if res.get("error"):
        return []
    return res.get("response_content", {})
    
@cache_data(show_spinner="Buscando dados...", max_entries=1)
def fetch_capabilities(base_url: str = get_base_url()) -> list[str]:
    content = get_content("/catalog/capabilities", base_url)
    
    if "capabilities" in content:
        capabilities = content["capabilities"] 
        names = [capability["name"] for capability in capabilities]
        return names
    return []

@cache_data(show_spinner="Buscando dados...", max_entries=1)
def fetch_capabilities_from_resource(uuid:str, base_url: str = get_base_url()) -> list[str]:
    content = get_content("/catalog/resources/"+uuid, base_url)
    data = content["data"]

    if "capabilities" in data:
        names = data["capabilities"]
        return names
    return []

@cache_data(show_spinner="Buscando dados...", max_entries=1)
def fetch_all_resources(base_url: str = get_base_url()) -> dict | None:
    content = get_content("/catalog/resources", base_url)
    
    if "resources" in content:
        resources = content["resources"]
        uuids = {}
        for resource in resources:
            uuids[resource["uuid"]] = resource["description"]
        return uuids
    return None

@cache_data(
    show_spinner="Buscando dados...",
    max_entries= 1,
    hash_funcs={
        dict: lambda d: json.dumps(d, sort_keys=True)  # Serializa dicionários para uma string ordenada
})
def request(
    method: str, 
    endpoint:str,
    params: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    base_url: str = get_base_url()
):
    api = APIClient(base_url=base_url)
    return api.request(method, endpoint,params, data, headers)
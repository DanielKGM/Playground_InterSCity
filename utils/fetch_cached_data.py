from services.api_client import APIClient
from streamlit import cache_data
from typing import Dict, Optional, Any
import json


def clear_cache():
    cache_data.clear()

def get_content(endpoint):
    api = APIClient()
    res = api.request("GET", endpoint)
    if res.get("error"):
        return []
    return res.get("response_content", {})
    
@cache_data(show_spinner="Buscando dados...", max_entries=1)
def fetch_capabilities() -> list[str]:
    content = get_content("/catalog/capabilities")
    
    if "capabilities" in content:
        capabilities = content["capabilities"] 
        names = [capability["name"] for capability in capabilities]
        return names
    return []

@cache_data(show_spinner="Buscando dados...", max_entries=1)
def fetch_capabilities_from_resource(uuid:str) -> list[str]:
    content = get_content("/catalog/resources/"+uuid)
    data = content["data"]

    if "capabilities" in data:
        names = data["capabilities"]
        return names
    return []

@cache_data(show_spinner="Buscando dados...", max_entries=1)
def fetch_all_resources() -> dict | None:
    content = get_content("/catalog/resources")
    
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
    headers: Optional[Dict[str, str]] = None
):
    api = APIClient()
    return api.request(method, endpoint,params, data, headers)
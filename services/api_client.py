import requests
from typing import Any, Dict, Optional
from models.resource import Resource
from models.capability import Capability

class APIClient:
    def __init__(self, base_url: str = 'https://cidadesinteligentes.lsdi.ufma.br/interscity_lh'):
        self.base_url = base_url

    def request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = {"Content-Type": "application/json"},
        first: bool = False
    ) -> Any:
        
        url = f"{self.base_url}{endpoint}"
        response = requests.request(
            method=method,
            url=url,
            params=params,
            json= data,
            headers=headers
        )
        
        #try:
        response.raise_for_status()
        json_response = response.json()
        if first:
            return next(iter(json_response.values()), None)
        return json_response
        #except requests.exceptions.HTTPError as e:
        #    return {"error": str(e), "response": response.text}
        #except ValueError:  # Caso o JSON seja inválido
        #    return {"error": "Invalid JSON response", "response": response.text}

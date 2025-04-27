import requests
from typing import Any, Dict, Optional
from config import get_base_url



class APIClient:
    def __init__(self, base_url: str = get_base_url()):
        self.base_url = base_url

        self.error_messages = {
            400: "Solicitação inválida. Verifique os dados enviados e tente novamente",
            401: "Não autorizado (401)",
            403: "Acesso proibido. Você não tem permissão para esta ação ",
            404: "Recurso não encontrado ou indisponível",
            422: "O conteúdo da requisição não foi aceito pela API",
            500: "Erro interno no servidor. Tente novamente mais tarde",
            502: "Erro de gateway. O servidor está temporariamente inacessível",
            503: "Serviço indisponível. O servidor não está disponível no momento",
            504: "Tempo de espera esgotado. Aguardando resposta do servidor",
            "default": "Ocorreu um erro inesperado. Tente novamente mais tarde"
        }


    def request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Any:
        url = f'{self.base_url}{endpoint}'

        try:
            response = requests.request(
                method=method,
                url=url,
                params=params,
                json=data,
                headers=headers
            )

            # Se a resposta não for bem-sucedida, ela levanta uma exceção.
            response.raise_for_status()

            if response.headers.get('Content-Type', '').startswith('application/json'):
                json_data = response.json()
            else:
                json_data = response.text

            return {"status_code": response.status_code, "response_content": json_data}
        
        except requests.exceptions.HTTPError:
            # Obtém o código de status da resposta e mapeia para a mensagem personalizada
            status_code = response.status_code
            error_message = self.error_messages.get(status_code, self.error_messages["default"])
            return {
                "status_code": status_code,
                "error": error_message,
                "response_content": None
            }
        
        except requests.exceptions.RequestException as req_err:
            # Captura de outros erros de requisição (tempo de espera, DNS, etc.)
            return {
                "status_code": None,
                "error": f"Erro de requisição: {req_err}",
                "response_content": None
            }
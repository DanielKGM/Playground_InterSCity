from streamlit import session_state

# URL BASE PARA AS REQUISIÇÕES DA API
DEFAULT_BASE_URL = "https://192.168.10.104"

def get_base_url() -> str:
    return session_state.get("base_url", DEFAULT_BASE_URL)
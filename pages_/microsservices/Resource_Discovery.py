from services.discovery import DiscoveryService
from utils.fetch_cached_data import fetch_capabilities
from utils.playground_template import generate_playground
from config import get_base_url


discovery = DiscoveryService(lista_capacidades=fetch_capabilities(base_url=get_base_url()))
generate_playground(service=discovery)
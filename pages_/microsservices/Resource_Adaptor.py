from services.adaptor import AdaptorService
from utils.fetch_cached_data import fetch_capabilities
from utils.fetch_cached_data import fetch_all_resources
from utils.playground_template import generate_playground
from config import get_base_url


adaptor = AdaptorService(lista_capacidades=fetch_capabilities(base_url= get_base_url()), lista_recursos= fetch_all_resources(base_url= get_base_url()))
generate_playground(service=adaptor)
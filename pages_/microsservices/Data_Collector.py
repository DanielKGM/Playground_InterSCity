from services.data_collector import CollectorService
from utils.fetch_cached_data import fetch_capabilities
from utils.fetch_cached_data import fetch_all_resources
from utils.playground_template import generate_playground


collector = CollectorService(lista_capacidades=fetch_capabilities(), lista_recursos=fetch_all_resources())
generate_playground(service=collector)
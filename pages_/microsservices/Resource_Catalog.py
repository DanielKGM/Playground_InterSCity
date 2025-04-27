from services.cataloguer import CataloguerService
from utils.fetch_cached_data import fetch_capabilities
from utils.playground_template import generate_playground
from config import get_base_url


cataloguer = CataloguerService(lista_capacidades=fetch_capabilities(base_url= get_base_url()))
generate_playground(service=cataloguer)
from services.data_collector import CollectorService
from utils.fetch_cached_data import fetch_capabilities
from utils.fetch_cached_data import fetch_all_resources
from utils.playground_template import generate_playground
from config import get_base_url
from utils.html_components import hero_section


hero_section(
    icon="📈",
    description_html="Gerencia e <u>disponibiliza dados</u> sensoriais de contexto",
    doc_link="https://gitlab.com/interscity/interscity-platform/data-collector/-/wikis/home",
)

collector = CollectorService(
    lista_capacidades=fetch_capabilities(base_url=get_base_url()),
    lista_recursos=fetch_all_resources(base_url=get_base_url()),
)

generate_playground(service=collector)

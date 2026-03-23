from services.discovery import DiscoveryService
from utils.fetch_cached_data import fetch_capabilities
from utils.playground_template import generate_playground
from config import get_base_url
from utils.html_components import hero_section


hero_section(
    icon="🔎",
    description_html="Provê filtros para a <u>descoberta de recursos</u>",
    doc_link="https://gitlab.com/interscity/interscity-platform/resource-discoverer",
)

discovery = DiscoveryService(
    lista_capacidades=fetch_capabilities(base_url=get_base_url())
)

generate_playground(service=discovery)

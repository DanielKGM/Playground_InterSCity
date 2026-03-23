from services.cataloguer import CataloguerService
from utils.fetch_cached_data import fetch_capabilities
from utils.playground_template import generate_playground
from config import get_base_url
from utils.html_components import hero_section


hero_section(
    icon="🗃️",
    description_html="Mantém os <u>dados estáticos</u> dos recursos e das capacidades",
    doc_link="https://gitlab.com/interscity/interscity-platform/resource-cataloguer/-/wikis/home",
    curl_link="https://gitlab.com/interscity/interscity-platform/resource-cataloguer/-/blob/master/requests.md",
)

cataloguer = CataloguerService(
    lista_capacidades=fetch_capabilities(base_url=get_base_url())
)

generate_playground(service=cataloguer)

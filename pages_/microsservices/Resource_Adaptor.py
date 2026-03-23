from services.adaptor import AdaptorService
from utils.fetch_cached_data import fetch_capabilities
from utils.fetch_cached_data import fetch_all_resources
from utils.playground_template import generate_playground
from config import get_base_url
from utils.html_components import hero_section


hero_section(
    icon="🔁",
    description_html='Ponto único de contato para os Gateways IoT: <u>envio de dados sensoriais</u> ou assinatura de comandos<br><small style="font-size: 0.9rem; color: #888; display: block; margin-top: 0.5rem;">Assinatura de comandos ainda não disponível no playground</small>',
    doc_link="https://gitlab.com/interscity/interscity-platform/resource-adaptor/-/wikis/home",
    curl_link="https://gitlab.com/interscity/interscity-platform/resource-adaptor/-/blob/master/requests.md",
)

adaptor = AdaptorService(
    lista_capacidades=fetch_capabilities(base_url=get_base_url()),
    lista_recursos=fetch_all_resources(base_url=get_base_url()),
)

generate_playground(service=adaptor)

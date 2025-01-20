from services.adaptor import AdaptorService
from utils.fetch_cached_data import fetch_capabilities
from utils.fetch_cached_data import fetch_all_resources
from utils.playground_template import generate_playground


adaptor = AdaptorService(lista_capacidades=fetch_capabilities(), lista_recursos= fetch_all_resources())
generate_playground(service=adaptor, 
                    title="Resource Adaptor",
                    markdown_path= "./static/adaptor.md"
                    )
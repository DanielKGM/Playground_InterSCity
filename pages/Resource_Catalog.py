from services.cataloguer import CataloguerService
import streamlit as st
from utils.fetch_cached_data import fetch_capabilities
from utils.playground_template import generate_playground


cataloguer = CataloguerService(lista_capacidades=fetch_capabilities())
generate_playground(service=cataloguer, presentation_key="cataloguer",titulo="🗃️ Resource Catalog")
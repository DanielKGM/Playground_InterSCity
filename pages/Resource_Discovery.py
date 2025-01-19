from services.discovery import DiscoveryService
import streamlit as st
from utils.fetch_cached_data import fetch_capabilities
from utils.playground_template import generate_playground


discovery = DiscoveryService(lista_capacidades=fetch_capabilities())
generate_playground(service=discovery, presentation_key="discovery",titulo="🔎 Resource Discovery")
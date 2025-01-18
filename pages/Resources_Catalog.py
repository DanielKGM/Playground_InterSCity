from services.cataloguer import CataloguerService
import streamlit as st
from utils.fetch_cached_data import fetch_capabilities


st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
)

st.header("Resources Catalog")
st.markdown('''
                Texto coisa e tal
            ''')

st.header("Playground")
cataloguer = CataloguerService(lista_capacidades=fetch_capabilities())
response = cataloguer.form("catalog_playground")

st.header("Resposta")
if response is None:
    st.info("Aqui serão exibidos os resultados da sua requisição", icon= ":material/visibility:")
elif response.get("error"):
    st.error(f'{response["error"]} ({response["status_code"]})', icon= ":material/sentiment_dissatisfied:")
else:
    tab1, tab2 = st.tabs(["JSON", "Dataframe"])
    tab1.write(response)
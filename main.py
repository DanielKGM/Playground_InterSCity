import streamlit as st
import validators
from config import get_base_url


# Initialize a session state variable that tracks the sidebar state (either 'expanded' or 'collapsed').
if 'sidebar_state' not in st.session_state:
    st.session_state.sidebar_state = 'collapsed'

# Streamlit set_page_config method has a 'initial_sidebar_state' argument that controls sidebar state.
st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state)

pages = {
    "InterSCity": [
        st.Page("./pages_/interscity/Introducao.py", title="Introdução", icon="🌐", default=True)
    ],
    "Microsserviços": [
        st.Page("./pages_/microsservices/Resource_Catalog.py", title = "Resource Catalog", icon= "🗃️"),
        st.Page("./pages_/microsservices/Resource_Discovery.py", title = "Resource Discovery", icon= "🔎"),
        st.Page("./pages_/microsservices/Resource_Adaptor.py",title="Resource Adaptor", icon="🔁"),
        st.Page("./pages_/microsservices/Data_Collector.py", title = "Data Collector", icon= "📈")
    ]
}

pg = st.navigation(pages, position="hidden")

with st.sidebar:
    link_icon = ":material/arrow_outward:"
    st.markdown("**InterSCity**")
    for page in pages["InterSCity"]:
        st.page_link(page, icon= page.icon)
    
    st.markdown("**Microsserviços**")
    for page in pages["Microsserviços"]:
        st.page_link(page, icon= page.icon)

    st.markdown("**Links úteis**")
    st.page_link("https://cidadesinteligentes.lsdi.ufma.br/doku.php?id=slides",
                label="Aulas InterSCity",
                icon=link_icon)
    
    st.page_link("https://gitlab.com/interscity/interscity-platform/docs/-/blob/master/api/API.md",
                label="Documentação API",
                icon=link_icon)
    
    st.page_link("https://gitlab.com/interscity/interscity-platform/interscity-platform",
                label="Código-fonte",
                icon=link_icon)
    
    st.page_link("https://cidadesinteligentes.lsdi.ufma.br/doku.php?id=videos",
                label="Como subir uma cópia",
                icon=link_icon)
    
    st.page_link("https://colab.research.google.com/drive/1ztdIMDvVSyWk3VTKXAX7NL6ek7IUs6mc?usp=sharing#scrollTo=i9vY2kxt-kWq",
                label="Exemplo de uso",
                icon=link_icon)
    
    st.markdown("**API**", help="Endereço o qual as requisições da API serão feitas")

    url_input = st.sidebar.text_input(
        "URL Base da API",
        label_visibility="collapsed",
        value=get_base_url()
    )

    if not validators.url(url_input):
        st.sidebar.error("URL inválida!")
    else:
        st.session_state["base_url"] = url_input


if pg.title != "Introdução":
    st.header(pg.title)

st.session_state.page = pg.title
st.logo(image="./static/icon.svg",size="large",link="https://interscity.org/software/interscity-platform/")
pg.run()
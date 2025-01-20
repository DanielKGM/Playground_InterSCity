import streamlit as st


if 'sidebar_state' in st.session_state:
    st.set_page_config(initial_sidebar_state=st.session_state.sidebar_state)
else:
    st.set_page_config(initial_sidebar_state="collapsed")
    st.session_state.sidebar_state = 'collapsed'

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

st.logo(image="./static/icon.svg",size="large",link="https://interscity.org/software/interscity-platform/")

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

pg.run()
# utils/menu.py
pages_config = {
    "InterSCity": [
        {
            "path": "./pages_/interscity/Introducao.py",
            "title": "Introdução",
            "icon": "🌐",
            "default": True,
        }
    ],
    "Microsserviços": [
        {
            "path": "./pages_/microsservices/Resource_Catalog.py",
            "title": "Resource Catalog",
            "icon": "🗃️",
        },
        {
            "path": "./pages_/microsservices/Resource_Discovery.py",
            "title": "Resource Discovery",
            "icon": "🔎",
        },
        {
            "path": "./pages_/microsservices/Resource_Adaptor.py",
            "title": "Resource Adaptor",
            "icon": "🔁",
        },
        {
            "path": "./pages_/microsservices/Data_Collector.py",
            "title": "Data Collector",
            "icon": "📈",
        },
    ],
}

link_icon = ":material/arrow_outward:"


def render_menu():
    import streamlit as st

    for section, pages in pages_config.items():
        st.markdown(f"**{section}**")
        for page in pages:
            st.page_link(page["path"], label=page["title"], icon=page["icon"])

    st.markdown("**Links úteis**")
    st.page_link(
        "https://cidadesinteligentes.lsdi.ufma.br/doku.php?id=slides",
        label="Aulas Sobre o InterSCity",
        icon=link_icon,
    )
    st.page_link(
        "https://gitlab.com/interscity/interscity-platform/docs/-/blob/master/api/API.md",
        label="Documentação da API",
        icon=link_icon,
    )
    st.page_link(
        "https://interscity.org/software/interscity-platform/",
        label="Página do Projeto",
        icon=link_icon,
    )
    st.page_link(
        "https://github.com/DanielKGM/Playground_InterSCity",
        label="Repositório do Playground",
        icon=link_icon,
    )
    st.page_link(
        "https://colab.research.google.com/drive/1ztdIMDvVSyWk3VTKXAX7NL6ek7IUs6mc?usp=sharing#scrollTo=i9vY2kxt-kWq",
        label="Exemplo de uso (Colab)",
        icon=":material/code:",
    )

from streamlit import html


def hero_section(
    icon: str, description_html: str, doc_link: str = None, curl_link: str = None
):
    links_list = []
    link_style = "color: #007bff; text-decoration: none; font-weight: 500;"

    if doc_link:
        links_list.append(
            f'<a target="_blank" href="{doc_link}" style="{link_style}">Documentação Geral</a>'
        )

    if curl_link:
        links_list.append(
            f'<a target="_blank" href="{curl_link}" style="{link_style}">Exemplos com CURL</a>'
        )

    links_html = ""
    if links_list:
        separador = ' <span style="color: #6c757d; margin: 0 0.5rem;">&middot;</span> '
        links_html = (
            f'<div style="margin-top: 1rem;">{separador.join(links_list)}</div>'
        )

    html_code = f"""
    <div style="
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 3rem 0; /* Usa espaçamento em vez de altura fixa da tela */
        text-align: center;
        font-family: sans-serif;
    ">
        <div style="font-size: 4rem; margin-bottom: 1.5rem; line-height: 1;">
            {icon}
        </div>
        
        <div style="color: #6c757d; max-width: 800px;">
            {description_html}
        </div>
        
        {links_html}
    </div>
    """

    html(html_code)

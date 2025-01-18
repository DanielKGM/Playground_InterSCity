import streamlit as st
import json
from urllib.parse import urlencode  # Para gerar query strings


def http_container(method: str, endpoint: str, content: dict = None, params: dict = None):
    # Define cores para os métodos
    colors = {
        "GET": "#28a745",       # Verde
        "POST": "#007bff",      # Azul
        "PUT": "#fb8500",       # Laranja
        "DELETE": "#dc3545",    # Vermelho
    }

    main_color = colors.get(method.upper(), "#6c757d")
    background_opacity = "0.1"
    background_color = main_color + f"{int(float(background_opacity) * 255):02x}"

    # Gera a query string, se os parâmetros forem fornecidos
    query_string = ""
    if params:
        query_string = f"?{urlencode(params, doseq=True)}"
    
    # Renderiza o JSON como string formatada
    content_html = ""
    if content:
        formatted_json = json.dumps(content, indent=4, ensure_ascii=False)
        content_html = f"""
        <pre style="
            overflow-x: auto;
            margin: 15px 0 0 0;
        ">{formatted_json}</pre>
        """

    html_content = f"""
    <div style="
        font-family: monospace;
        display: flex; 
        flex-direction: column;
        align-items: flex-start; 
        background-color: {background_color};
        border: 2px solid {main_color};
        border-radius: 10px;
        padding: 15px;
    ">
        <div style="
            display: flex;
            align-items: center;
            width: 100%;
            overflow-x: auto;
            word-wrap: break-word;
            overflow-wrap: break-word;
        ">
            <div style="
                background-color: {main_color};
                padding: 5px 10px;
                border-radius: 5px;
                font-weight: bold;
                color: white;
                text-transform: uppercase;
                margin-right: 10px;
            ">
                {method}
            </div>
            <div>
                {endpoint}{query_string}
            </div>
        </div>
        {content_html}
    </div>
    """

    return html_content
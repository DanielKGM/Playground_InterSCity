import reveal_slides as rs
from pathlib import Path
from streamlit import caption


def get_slide(markdown_path:str):
    try:
        caption(r"""Pressione `F` para ler os slides em tela cheia""")
        return rs.slides(Path(markdown_path).read_text(encoding="UTF-8"), 
        height=500, 
        theme="moon",
        config={
                "transition": "slide",
                "width": 1000,
                "height": 1000, 
                "minScale": 0.1, 
                "center": True,
                "progress": False,
                "maxScale": 3, 
                "controlsLayout": 'bottom-right',
                "margin": 0, 
                "plugins": ["highlight"]
                },
        markdown_props={"data-separator-vertical":"^--$"},
        key="foo",
        display_only= True
        )
    except FileNotFoundError:
        return None
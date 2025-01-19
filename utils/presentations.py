from streamlit.components.v1 import iframe


SLIDES = {
    "cataloguer": "id.g3272a5b904d_0_0"
}

def presentation(key: str, height:int = 430):
    base_url = "https://docs.google.com/presentation/d/e/2PACX-1vRMlGrn7Aeyb2ykJw5FpmxrQXme987ZVd1XpTAo1hkV85cflTDtBX8aukLcarD7fJbLWWgGrj1ewnSo/embed?start=false&loop=false&delayms=3000&slide=id.g3272a5b904d_0_0&slide="
    idslide = SLIDES.get(key,None)
    if idslide:
        return iframe(base_url + idslide, height=height)
    return None
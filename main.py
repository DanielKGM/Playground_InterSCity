import streamlit as st


pages = {
    "Microsserviços": [
        st.Page("./pages/Resource_Catalog.py", title = "Resource Catalog", icon= "🗃️"),
        st.Page("./pages/Resource_Discovery.py", title = "Resource Discovery", icon= "🔎")
    ]
}

pg = st.navigation(pages)
with st.sidebar:
    st.subheader("Links Úteis")
    
pg.run()


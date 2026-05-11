import streamlit as st
from agentes.router import router

st.set_page_config(
    page_title="AEA001 - Rosinholi",
    page_icon="🚀",
    layout="wide"
)

st.sidebar.title("🧭 AEA Router")
st.sidebar.success("Repositório: rosinholi")

# Chama o router
router()

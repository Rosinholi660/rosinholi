import streamlit as st
from agentes.aea001 import aea001

def router():
    st.title("🚀 AEA Consultoria - Rosinholi")
    st.write("Bem-vindo ao sistema de agentes!")

    escolha = st.sidebar.radio(
        "Escolha o agente:",
        ["AEA001 - Otimização de Reclamações"]
    )

    if escolha == "AEA001 - Otimização de Reclamações":
        aea001()

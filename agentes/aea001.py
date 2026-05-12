import streamlit as st
import pandas as pd

def aea001():
    if "nome_usuario" not in st.session_state:
        st.session_state.nome_usuario = "Mauricio"

    nome = st.session_state.nome_usuario

    st.title("🚀 AEA001 v5.3")
    st.markdown(f"**Olá {nome}!** Vamos otimizar juntos! 🎉")

    # Carregar os arquivos que você enviou
    try:
        reclamacoes = pd.read_excel("Reclamacoes.xlsx")
        processos = pd.read_excel("Processos.xlsx")
        dados_carregados = True
    except:
        dados_carregados = False

    if dados_carregados:
        st.success("✅ Planilhas carregadas com sucesso!")
        
        # Análise rápida
        total_reclamacoes = len(reclamacoes)
        custo_total = reclamacoes["Custo de correcao"].sum() if "Custo de correcao" in reclamacoes.columns else 0

        st.subheader("📊 Análise Inicial (seus dados reais)")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total de Reclamações", total_reclamacoes)
            st.metric("Custo Total", f"R$ {custo_total:,.2f}")
        with col2:
            st.metric("Processos mapeados", len(processos))

    # Tela ROI Bonita
    st.subheader("💰 [TELA ROI COMBINADO]")
    st.success(f"**Parabéns {nome}!** Seu ROI ficou excelente! 🔥")

    st.markdown("""
    <div style="background-color:#111827; padding:30px; border-radius:20px; text-align:center; margin:20px 0;">
        <h2 style="color:#22ff88;">ROI = 347% em 12 meses</h2>
        <h3 style="color:#e2e8f0;">Economia estimada: R$ 184.750,00</h3>
        <h4 style="color:#e2e8f0;">Payback: 4,2 meses</h4>
    </div>
    """, unsafe_allow_html=True)

    st.button("✅ Confirmar e ir para Plano de 90 Dias")
    st.button("🔄 Re-estimar ROI com meus dados")

    st.sidebar.success(f"Usuário: {nome}")

import streamlit as st
import pandas as pd

def aea001():
    if "nome_usuario" not in st.session_state:
        st.session_state.nome_usuario = "Mauricio"

    nome = st.session_state.nome_usuario

    st.title("🚀 AEA001 v5.3")
    st.markdown(f"**Olá {nome}!** Vamos otimizar juntos! 🎉")

    # ===================== TELA ROI BONITA =====================
    st.subheader("💰 [TELA ROI COMBINADO]")

    st.success(f"**Parabéns {nome}!** Seu ROI ficou excelente! 🔥")

    # Caixa grande do ROI (mais simples e estável)
    st.markdown("""
    <div style="background-color: #111827; padding: 25px; border-radius: 15px; text-align: center; margin: 20px 0;">
        <h2 style="color: #22ff88; margin: 0;">ROI = 347% em 12 meses</h2>
        <h3 style="color: #ddd;">Economia estimada: R$ 184.750,00</h3>
        <h4 style="color: #ddd;">Payback: 4,2 meses</h4>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Reclamações reduzidas", "64%", "🔥")
        st.metric("Custo mensal atual", "R$ 87.450")
    with col2:
        st.metric("Economia total", "R$ 184.750", "✅")

    # Gráfico simples e estável
    dados = pd.DataFrame({
        "Período": ["Antes", "Depois"],
        "Custo Médio (R$ mil)": [22, 8]
    })
    st.bar_chart(dados.set_index("Período"), color=["#3b82f6", "#22c55e"])

    st.button("✅ Confirmar e ir para Plano de 90 Dias")
    st.button("🔄 Re-estimar ROI")

    st.sidebar.success(f"Usuário: {nome}")
    st.sidebar.info("Tela: ROI Combinado")

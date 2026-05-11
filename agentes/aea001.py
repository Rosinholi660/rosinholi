import streamlit as st
import pandas as pd

def aea001():
    if "nome_usuario" not in st.session_state:
        st.session_state.nome_usuario = "Mauricio"
    if "tela_atual" not in st.session_state:
        st.session_state.tela_atual = "ROI_COMBINADO"  # Começa direto na tela bonita

    nome = st.session_state.nome_usuario

    st.title("🚀 AEA001 v5.3")
    st.markdown(f"**Olá {nome}!** Vamos otimizar juntos! 🎉")

    if st.session_state.tela_atual == "ROI_COMBINADO":
        st.subheader("💰 [TELA ROI COMBINADO]")
        st.markdown("**Parabéns Mauricio!** Seu ROI ficou excelente! 🔥")

        # Caixa grande do ROI (igual à imagem)
        st.markdown("""
        <div style="background-color:#111827; padding:25px; border-radius:15px; text-align:center; margin:15px 0;">
            <h2 style="color:#22ff88; margin:0;">ROI = 347% em 12 meses</h2>
            <h3 style="color:#ddd;">Economia estimada: R$ 184.750,00</h3>
            <h4 style="color:#ddd;">Payback: 4,2 meses</h4>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Reclamações reduzidas", "64%", "🔥")
            st.metric("Custo mensal atual", "R$ 87.450")
        with col2:
            st.metric("Economia projetada", "R$ 184.750", "✅")

        # Gráfico
        dados = pd.DataFrame({
            "Período": ["Antes", "Depois"],
            "Custo Médio": [22, 8]
        })
        st.bar_chart(dados.set_index("Período"), color=["#3b82f6", "#22c55e"])

        st.button("✅ Confirmar e ir para Plano de 90 Dias", on_click=lambda: st.session_state.update({"tela_atual": "PLANO_90"}))
        st.button("Re-estimar ROI", on_click=lambda: st.session_state.update({"tela_atual": "ROI_COMBINADO"}))

    elif st.session_state.tela_atual == "PLANO_90":
        st.subheader("📅 Plano de Implementação - 90 Dias")
        st.success("Plano pronto para você, Mauricio!")
        st.button("Voltar ao ROI", on_click=lambda: st.session_state.update({"tela_atual": "ROI_COMBINADO"}))

    else:
        st.write("Estamos avançando! 🎉")

    st.sidebar.success(f"Usuário: {nome}")

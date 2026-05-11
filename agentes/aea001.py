import streamlit as st

def aea001():
    st.title("🚀 AEA001 v5.3 - Versão Limpa")
    st.success("**Mauricio, teste de limpeza feito com sucesso!** 🎉")

    st.write("Se você está vendo esta tela, o app atualizou corretamente.")
    st.balloons()

    st.markdown("---")
    st.write("**Agora vamos colocar a tela bonita do ROI.**")
    st.button("Ir para Tela ROI Bonita", on_click=lambda: st.session_state.update({"tela_atual": "ROI"}))

    if st.session_state.get("tela_atual") == "ROI":
        st.subheader("💰 [TELA ROI COMBINADO]")
        st.success("Parabéns Mauricio! Seu ROI ficou excelente! 🔥")

        st.markdown("""
        **ROI = 347% em 12 meses**  
        Economia estimada: **R$ 184.750,00**  
        Payback: **4,2 meses**
        """)

        st.button("Voltar")

    st.sidebar.success("Mauricio")

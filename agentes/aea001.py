import streamlit as st

def aea001():
    if "nome_usuario" not in st.session_state:
        st.session_state.nome_usuario = ""
    if "tela_atual" not in st.session_state:
        st.session_state.tela_atual = "INICIAL"

    def ir_para(tela):
        st.session_state.tela_atual = tela
        st.rerun()

    nome = st.session_state.nome_usuario or "Mauricio"

    # ===================== CABEÇALHO =====================
    st.title("🚀 AEA001 v5.3")
    st.markdown(f"**Olá {nome}!** Vamos otimizar juntos! 🎉")

    # ===================== TELAS BONITAS =====================
    if st.session_state.tela_atual == "INICIAL":
        st.success("Bem-vindo ao seu mentor de processos!")
        nome_input = st.text_input("Como você quer que eu te chame?", placeholder="Mauricio")
        if st.button("Confirmar nome"):
            if nome_input.strip():
                st.session_state.nome_usuario = nome_input.strip()
                ir_para("ESCOLHA_DADOS")
                st.balloons()

    elif st.session_state.tela_atual == "ESCOLHA_DADOS":
        st.write(f"Olá **{nome}**! Como você quer trabalhar hoje?")
        opcao = st.radio("Escolha:", 
            ["1. Usar dados simulados (mais rápido)",
             "2. Fazer upload de arquivos"], 
            key="op1")
        
        if st.button("Continuar"):
            ir_para("ANALISE_INICIAL")

    elif st.session_state.tela_atual == "ANALISE_INICIAL":
        st.subheader("📊 [TELA ANALISE INICIAL]")
        st.success(f"Parabéns {nome}! Estamos avançando muito bem! 🎉")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Reclamações analisadas", "247", "-18%")
            st.metric("Custo total atual", "R$ 87.450", "-23%")
        with col2:
            st.metric("Causa principal", "Retrab. Logístico", "🔴")
            st.metric("Lead time médio", "9,4 dias", "-2,1 dias")

        st.button("Ir para Mapa do Processo", on_click=lambda: ir_para("MAPA_PROCESSO"))

    elif st.session_state.tela_atual == "MAPA_PROCESSO":
        st.subheader("🗺️ [TELA MAPA PROCESSO]")
        st.write(f"Olá {nome}! Aqui está o fluxo reverso da reclamação.")
        st.button("Ir para Melhorias", on_click=lambda: ir_para("MELHORIAS"))

    elif st.session_state.tela_atual == "MELHORIAS":
        st.subheader("🔧 Melhorias Identificadas")
        st.button("Calcular ROI", on_click=lambda: ir_para("ROI_COMBINADO"))

    elif st.session_state.tela_atual == "ROI_COMBINADO":
        st.subheader("💰 [TELA ROI COMBINADO]")
        st.markdown("**Parabéns João!** Seu ROI ficou excelente! 🔥")
        
        st.markdown("""
        <div style="background-color:#0e1117; padding:20px; border-radius:10px; text-align:center;">
            <h2 style="color:#00ff00;">ROI = 347% em 12 meses</h2>
            <h3>Economia estimada: R$ 184.750,00</h3>
            <h4>Payback: 4,2 meses</h4>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.bar_chart({"Antes": [22], "Depois": [8]})
        with col2:
            st.success("Melhoria de 64% nos custos!")

        st.button("Ir para Plano de 90 Dias", on_click=lambda: ir_para("PLANO_90"))

    else:
        st.write(f"Olá **{nome}**! Estamos avançando! 🎉")
        st.button("Voltar ao Início", on_click=lambda: ir_para("INICIAL"))

    # Sidebar
    st.sidebar.success(f"Usuário: {nome}")
    st.sidebar.info(f"Tela: {st.session_state.tela_atual}")

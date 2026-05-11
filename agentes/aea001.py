import streamlit as st

def aea001():
    if "nome_usuario" not in st.session_state:
        st.session_state.nome_usuario = ""
    if "tela_atual" not in st.session_state:
        st.session_state.tela_atual = "INICIAL"

    def ir_para(tela):
        st.session_state.tela_atual = tela
        st.rerun()

    # ==================== TELAS ====================
    if st.session_state.tela_atual == "INICIAL":
        st.title("🚀 AEA001 v5.3 - Mentor de Otimização")
        st.write("Olá! Eu sou o **AEA001 v5.3**, seu mentor.")
        st.write("Vou te guiar bem devagarinho, celebrando cada vitória! 🎉")
        
        nome = st.text_input("Como você quer que eu te chame?", placeholder="Seu nome")
        
        if st.button("Confirmar nome"):
            if nome.strip():
                st.session_state.nome_usuario = nome.strip()
                ir_para("ESCOLHA_DADOS")
            else:
                st.warning("Por favor, digite um nome!")

    elif st.session_state.tela_atual == "ESCOLHA_DADOS":
        nome = st.session_state.nome_usuario
        st.title(f"[TELA ESCOLHA DADOS]")
        st.write(f"Olá **{nome}**! Para começar, escolha como vamos trabalhar:")
        
        opcao = st.radio("Escolha uma opção:", 
            ["1. Upload de arquivo único de reclamações (Excel/CSV)",
             "2. Usar dados simulados realistas",
             "3. Upload de cadastros detalhados (recomendado)"], 
            key="radio_escolha")

        if st.button("Continuar"):
            if "1" in opcao or "2" in opcao:
                ir_para("CAUSAS_SUBPROCESSOS")
            else:
                ir_para("CADASTROS_CLIENTES")
        
        st.write("Você entendeu as opções? Precisa de ajuda?")

    elif st.session_state.tela_atual == "CADASTROS_CLIENTES":
        nome = st.session_state.nome_usuario
        st.title(f"[TELA CADASTROS CLIENTES]")
        st.write(f"Olá **{nome}**! Vamos enriquecer a análise.")
        st.write("Faça upload dos cadastros:")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.file_uploader("Cadastro de Clientes", type=["csv", "xlsx"], key="clientes")
        with col2:
            st.file_uploader("Cadastro de Produtos", type=["csv", "xlsx"], key="produtos")
        with col3:
            st.file_uploader("Histórico de Vendas (opcional)", type=["csv", "xlsx"], key="vendas")

        if st.button("Confirmar uploads"):
            ir_para("CAUSAS_SUBPROCESSOS")
        
        st.write("Você entendeu claramente o que precisa enviar?")
        st.write("Precisa de exemplo de tabela?")

    elif st.session_state.tela_atual == "CAUSAS_SUBPROCESSOS":
        nome = st.session_state.nome_usuario
        st.title(f"[TELA CAUSAS SUBPROCESSOS]")
        st.write(f"Olá **{nome}**! Excelente.")
        st.write("Agora envie as tabelas de causas e subprocessos.")

        st.file_uploader("Tabela de Causas de Reclamações", type=["csv", "xlsx"], key="causas")
        st.file_uploader("Lista de Subprocessos", type=["csv", "xlsx"], key="subprocessos")

        if st.button("Continuar"):
            ir_para("CUSTOS_ATIVIDADES")
        
        st.write("Você entendeu o que precisa enviar?")

    else:
        st.title(f"[TELA {st.session_state.tela_atual}]")
        st.write(f"Olá **{nome}**! Estamos avançando muito bem! 🎉")

    st.sidebar.success(f"Usuário: {st.session_state.nome_usuario or 'Não definido'}")
    st.sidebar.info(f"Tela atual: {st.session_state.tela_atual}")

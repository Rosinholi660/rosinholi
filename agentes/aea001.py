import streamlit as st

def aea001():
    if "nome_usuario" not in st.session_state:
        st.session_state.nome_usuario = ""
    if "tela_atual" not in st.session_state:
        st.session_state.tela_atual = "INICIAL"
    if "opcao_escolhida" not in st.session_state:
        st.session_state.opcao_escolhida = None

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
            key="radio_opcao")

        if st.button("Continuar"):
            st.session_state.opcao_escolhida = opcao
            if "3" in opcao:
                ir_para("CADASTROS_CLIENTES")
            else:
                ir_para("CAUSAS_SUBPROCESSOS")
        
        st.write("Você entendeu as opções? Precisa de ajuda?")

    else:
        st.title(f"[TELA {st.session_state.tela_atual}]")
        st.write(f"Olá **{st.session_state.nome_usuario}**! Estamos avançando! 🎉")

    st.sidebar.success(f"Usuário: {st.session_state.nome_usuario or 'Não definido'}")

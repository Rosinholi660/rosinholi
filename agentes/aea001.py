import streamlit as st

def aea001():
    if "nome_usuario" not in st.session_state:
        st.session_state.nome_usuario = ""
    if "tela_atual" not in st.session_state:
        st.session_state.tela_atual = "INICIAL"

    def ir_para(tela):
        st.session_state.tela_atual = tela
        st.rerun()

    nome = st.session_state.nome_usuario

    # ==================== TELAS ====================
    if st.session_state.tela_atual == "INICIAL":
        st.title("🚀 AEA001 v5.3 - Mentor de Otimização")
        st.write("Olá! Eu sou o **AEA001 v5.3**, seu mentor.")
        st.write("Vou te guiar bem devagarinho, celebrando cada vitória! 🎉")
        
        nome_input = st.text_input("Como você quer que eu te chame?", placeholder="Seu nome")
        
        if st.button("Confirmar nome"):
            if nome_input.strip():
                st.session_state.nome_usuario = nome_input.strip()
                ir_para("ESCOLHA_DADOS")

    elif st.session_state.tela_atual == "ESCOLHA_DADOS":
        st.title(f"[TELA ESCOLHA DADOS]")
        st.write(f"Olá **{nome}**! Para começar, escolha como vamos trabalhar:")
        
        opcao = st.radio("Escolha uma opção:", 
            ["1. Upload de arquivo único de reclamações",
             "2. Usar dados simulados realistas",
             "3. Upload de cadastros detalhados (recomendado)"], 
            key="opcao_principal")

        if st.button("Continuar"):
            if "3" in opcao:
                ir_para("CADASTROS_CLIENTES")
            else:
                ir_para("CAUSAS_SUBPROCESSOS")

    elif st.session_state.tela_atual == "CADASTROS_CLIENTES":
        st.title(f"[TELA CADASTROS CLIENTES]")
        st.write(f"Olá **{nome}**! Vamos enriquecer a análise.")
        st.write("Faça upload dos cadastros:")

        st.file_uploader("Cadastro de Clientes", type=["csv", "xlsx"])
        st.file_uploader("Cadastro de Produtos/Serviços", type=["csv", "xlsx"])
        st.file_uploader("Histórico de Vendas (opcional)", type=["csv", "xlsx"])

        if st.button("Confirmar uploads e continuar"):
            ir_para("CAUSAS_SUBPROCESSOS")

    elif st.session_state.tela_atual == "CAUSAS_SUBPROCESSOS":
        st.title(f"[TELA CAUSAS SUBPROCESSOS]")
        st.write(f"Olá **{nome}**! Excelente.")
        st.write("Agora envie:")
        st.write("• Tabela de Causas de Reclamações")
        st.write("• Lista de Subprocessos")

        st.file_uploader("Tabela de Causas", type=["csv", "xlsx"])
        st.file_uploader("Subprocessos", type=["csv", "xlsx"])

        if st.button("Continuar para Custos"):
            ir_para("CUSTOS_ATIVIDADES")

    elif st.session_state.tela_atual == "CUSTOS_ATIVIDADES":
        st.title(f"[TELA CUSTOS ATIVIDADES]")
        st.write(f"Olá **{nome}**! Último cadastro.")
        st.write("Envie a tabela de custos por atividade.")

        st.file_uploader("Tabela de Custos", type=["csv", "xlsx"])
        st.warning("⚠️ Dados errados aqui podem afetar o ROI.")

        if st.button("Confirmar e ir para Análise"):
            ir_para("ANALISE_INICIAL")

    else:
        st.title(f"[TELA {st.session_state.tela_atual}]")
        st.write(f"Olá **{nome}**! Estamos avançando muito bem! 🎉")
        st.button("Voltar ao início", on_click=lambda: ir_para("INICIAL"))

    # Sidebar
    st.sidebar.success(f"Usuário: {nome or 'Não definido'}")
    st.sidebar.info(f"Tela: {st.session_state.tela_atual}")

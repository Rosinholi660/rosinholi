import streamlit as st
import pandas as pd

def aea001():
    if "nome_usuario" not in st.session_state:
        st.session_state.nome_usuario = ""
    if "tela_atual" not in st.session_state:
        st.session_state.tela_atual = "INICIAL"
    if "dossie" not in st.session_state:
        st.session_state.dossie = {}

    def ir_para(tela):
        st.session_state.tela_atual = tela
        st.rerun()

    nome = st.session_state.nome_usuario or "amigão"

    st.title("🚀 AEA001 v5.3 - Mentor de Otimização")

    # ==================== TELAS ====================
    if st.session_state.tela_atual == "INICIAL":
        st.write(f"Olá! Eu sou o **AEA001 v5.3**, seu mentor.")
        st.write(f"Vou te guiar passo a passo, bem devagarinho, {nome}!")
        
        nome_input = st.text_input("Como você quer que eu te chame?", placeholder="Mauricio")
        if st.button("Confirmar nome"):
            if nome_input.strip():
                st.session_state.nome_usuario = nome_input.strip()
                ir_para("ESCOLHA_DADOS")
                st.balloons()

    elif st.session_state.tela_atual == "ESCOLHA_DADOS":
        st.write(f"Olá **{nome}**! Para começar, escolha como vamos trabalhar:")
        
        opcao = st.radio("Opções:", 
            ["1. Upload de arquivo único de reclamações",
             "2. Usar dados simulados realistas",
             "3. Upload de cadastros detalhados (recomendado)"], 
            key="opcao1")

        if st.button("Continuar"):
            if "3" in opcao:
                ir_para("CADASTROS_CLIENTES")
            else:
                ir_para("CAUSAS_SUBPROCESSOS")

    elif st.session_state.tela_atual == "CADASTROS_CLIENTES":
        st.write(f"Olá **{nome}**! Vamos enriquecer a análise.")
        st.file_uploader("Cadastro de Clientes", type=["csv", "xlsx"])
        st.file_uploader("Cadastro de Produtos", type=["csv", "xlsx"])
        st.file_uploader("Histórico de Vendas", type=["csv", "xlsx"])

        if st.button("Confirmar uploads"):
            ir_para("CAUSAS_SUBPROCESSOS")

    elif st.session_state.tela_atual == "CAUSAS_SUBPROCESSOS":
        st.write(f"Olá **{nome}**! Excelente.")
        st.file_uploader("Tabela de Causas", type=["csv", "xlsx"])
        st.file_uploader("Subprocessos", type=["csv", "xlsx"])

        if st.button("Continuar"):
            ir_para("CUSTOS_ATIVIDADES")

    elif st.session_state.tela_atual == "CUSTOS_ATIVIDADES":
        st.write(f"Olá **{nome}**! Último cadastro.")
        st.file_uploader("Tabela de Custos por Atividade", type=["csv", "xlsx"])
        st.warning("⚠️ Dados errados aqui podem deixar o ROI errado.")

        if st.button("Confirmar e ir para Análise"):
            ir_para("ANALISE_INICIAL")

    elif st.session_state.tela_atual == "ANALISE_INICIAL":
        st.write(f"Olá **{nome}**! Aqui está a análise inicial enriquecida.")
        st.success("Parabéns! 🎉")
        if st.button("Ir para Mapa do Processo"):
            ir_para("MAPA_PROCESSO")

    elif st.session_state.tela_atual == "MAPA_PROCESSO":
        st.write(f"Olá **{nome}**! Vamos mapear o processo reverso.")
        if st.button("Ir para Melhorias"):
            ir_para("MELHORIAS_PROCESSO")

    elif st.session_state.tela_atual == "MELHORIAS_PROCESSO":
        st.write(f"Olá **{nome}**! Vamos identificar melhorias.")
        if st.button("Calcular ROI"):
            ir_para("ROI_COMBINADO")

    elif st.session_state.tela_atual == "ROI_COMBINADO":
        st.subheader(f"[TELA ROI COMBINADO]")
        st.write(f"**Parabéns {nome}!** 🎉 Seu ROI combinado ficou excelente!")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("ROI", "347% em 12 meses", "🔥")
            st.metric("Economia estimada", "R$ 184.750,00")
            st.metric("Payback", "4,2 meses")
        with col2:
            # Gráfico simples
            dados = pd.DataFrame({
                "Período": ["Antes", "Depois"],
                "Custo": [22, 12]
            })
            st.bar_chart(dados.set_index("Período"))

        st.button("Confirmar e ir para Plano 90 Dias", on_click=lambda: ir_para("PLANO_90_DIAS"))
        st.button("Re-estimar ROI", on_click=lambda: ir_para("REESTIMATIVA_ROI"))

    elif st.session_state.tela_atual == "PLANO_90_DIAS":
        st.write(f"Olá **{nome}**! Aqui está seu Plano de 90 dias.")
        st.success("Implementação faseada pronta!")

    else:
        st.write(f"Olá **{nome}**! Estamos avançando muito bem! 🎉")

    st.sidebar.success(f"Usuário: {nome}")

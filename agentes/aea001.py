import streamlit as st

def aea001():
    if "nome_usuario" not in st.session_state:
        st.session_state.nome_usuario = "Mauricio"
    if "historico" not in st.session_state:
        st.session_state.historico = []
    if "etapa" not in st.session_state:
        st.session_state.etapa = "INICIAL"

    nome = st.session_state.nome_usuario

    st.title("🚀 AEA001 v5.3 - Seu Mentor Conversacional")

    # Mostra histórico
    for msg in st.session_state.historico:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    prompt = st.chat_input("Digite aqui (ex: A, B, ACEITO, SEGUI...)")

    if prompt:
        st.session_state.historico.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        resposta = f"Olá **{nome}**! "

        # Controle de etapas com opções padronizadas
        if st.session_state.etapa == "INICIAL":
            resposta += "Que bom te ver por aqui! Vamos otimizar juntos?\n\n"
            resposta += "**Escolha uma opção:**\n"
            resposta += "A) Começar a análise de reclamações agora\n"
            resposta += "B) Explicar primeiro o que é custo de mão de obra e encargos\n"
            resposta += "C) Ver exemplo de ROI antes de começar\n"
            st.session_state.etapa = "MENU"

        elif "A" in prompt.upper() or "começar" in prompt.lower():
            resposta += "Ótima escolha! 🎉 Você escolheu começar a análise.\n\n"
            resposta += "**Próximo passo:** Quer usar seus arquivos reais ou dados simulados?\n"
            resposta += "A) Usar meus arquivos Reclamacoes.xlsx e Processos.xlsx\n"
            resposta += "B) Usar dados simulados (mais rápido)\n"
            st.session_state.etapa = "DADOS"

        elif "B" in prompt.upper() or "custo" in prompt.lower() or "encargos" in prompt.lower():
            resposta += "Vamos falar de custo de mão de obra bem devagar:\n\n"
            resposta += "• **Sem encargos** = só o salário bruto\n"
            resposta += "• **Com encargos** = salário + INSS Patronal (20%) + FGTS (8%) + 13º + Férias + outros\n"
            resposta += "No total, o custo real costuma ser **80% a 120% maior** que o salário.\n\n"
            resposta += "Entendeu? Digite **ACEITO** para continuar."

        else:
            resposta += "Entendi! Me diz com clareza: **A**, **B**, **ACEITO**, **SEGUI** ou o que você quer fazer agora?"

        st.session_state.historico.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.write(resposta)

    st.sidebar.success(f"Conversando com: {nome}")
    st.sidebar.info(f"Etapa: {st.session_state.etapa}")

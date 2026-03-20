import streamlit as st

# ---------------------------
# CONFIGURAÇÃO INICIAL
# ---------------------------
st.set_page_config(page_title="Quiz Mary Jackson")

# Estado inicial
if "pagina" not in st.session_state:
    st.session_state.pagina = "inicio"

if "pergunta_atual" not in st.session_state:
    st.session_state.pergunta_atual = 0

if "pontos" not in st.session_state:
    st.session_state.pontos = 0

if "tentativas" not in st.session_state:
    st.session_state.tentativas = 0

if "resposta_selecionada" not in st.session_state:
    st.session_state.resposta_selecionada = None


# ---------------------------
# DADOS DO QUIZ
# ---------------------------
perguntas = [
    {
        "pergunta": "Quem foi Mary Jackson? 👩🏽‍🚀",
        "opcoes": ["Cantora famosa", "Engenheira da NASA", "Atriz de cinema", "Jogadora de futebol"],
        "correta": 1
    },
    {
        "pergunta": "Por quantos anos Mary Jackson trabalhou na NASA? 🛰️",
        "opcoes": ["11 anos", "28 anos", "34 anos", "5 anos"],
        "correta": 2
    },
    {
        "pergunta": "Mary Jackson ficou conhecida por contribuir em qual área? 👩🏽‍🔬",
        "opcoes": ["Engenharia aeroespacial", "Medicina", "Direito", "Música"],
        "correta": 0
    },
    {
        "pergunta": "Mary Jackson foi a primeira mulher negra a se tornar o quê na NASA? ⚙️",
        "opcoes": ["Engenheira", "Pilota", "Diretora", "Médica"],
        "correta": 0
    },
    {
        "pergunta": "Qual filme retrata a história de Mary Jackson? 🌌",
        "opcoes": ["Interestelar", "Estrelas Além do Tempo", "Gravidade", "Titanic"],
        "correta": 1
    },
    {
        "pergunta": "Mary Jackson precisou lutar contra o quê para avançar na carreira? 💪🏽",
        "opcoes": ["Falta de estudos", "Problemas financeiros", "Preconceito racial e de gênero", "Falta de apoio familiar"],
        "correta": 2
    },
    {
        "pergunta": "Em qual estado dos EUA Mary Jackson nasceu? 📖",
        "opcoes": ["Califórnia", "Virgínia", "Flórida", "Texas"],
        "correta": 1
    },
    {
        "pergunta": "Para se tornar engenheira, Mary Jackson teve que frequentar aulas onde? 🎓",
        "opcoes": ["Universidade privada internacional", "Escola exclusiva da NASA", "Escola segregada para brancos", "Curso online"],
        "correta": 2
    },
    {
        "pergunta": "Qual era a principal área de trabalho de Mary Jackson na NASA? 🌠",
        "opcoes": ["Robótica", "Aerodinâmica", "Astronomia", "Programação"],
        "correta": 1
    },
    {
        "pergunta": "Antes de se tornar engenheira, Mary Jackson trabalhava como o quê na NASA? 🧠",
        "opcoes": ["Astronauta", "Professora", "Matemática (computadora humana)", "Médica"],
        "correta": 2
    }
]


# ---------------------------
# TELA INICIAL
# ---------------------------
if st.session_state.pagina == "inicio":
    st.title("INSERIR TÍTULO AQUI")
    st.write("Desafie sua mente com a história de Mary Jackson!")

    if st.button("Iniciar Quiz"):
        st.session_state.pagina = "quiz"
        st.rerun()


# ---------------------------
# TELA DO QUIZ
# ---------------------------
elif st.session_state.pagina == "quiz":

    i = st.session_state.pergunta_atual
    pergunta = perguntas[i]

    st.subheader(f"Pergunta {i+1}")
    st.write(pergunta["pergunta"])

    resposta = st.radio(
        "Escolha uma alternativa:",
        pergunta["opcoes"],
        index=None
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Responder"):
            if resposta is None:
                st.warning("Selecione uma resposta!")
            else:
                correta = pergunta["opcoes"][pergunta["correta"]]

                if resposta == correta:
                    if st.session_state.tentativas == 0:
                        st.session_state.pontos += 10
                        st.success("Incrível! +10 pontos 🚀")
                    elif st.session_state.tentativas == 1:
                        st.session_state.pontos += 5
                        st.success("Parabéns! +5 pontos")
                    else:
                        st.session_state.pontos += 2
                        st.success("Parabéns! +2 pontos")

                    st.session_state.tentativas = 0
                    st.session_state.resposta_selecionada = True

                else:
                    st.session_state.tentativas += 1
                    if st.session_state.tentativas < 3:
                        st.error("Errado! Tente novamente.")
                    else:
                        st.error("Errou todas as tentativas!")
                        st.session_state.tentativas = 0
                        st.session_state.resposta_selecionada = True

    with col2:
        if st.session_state.resposta_selecionada:
            if st.button("Próxima"):
                st.session_state.pergunta_atual += 1
                st.session_state.resposta_selecionada = False

                if st.session_state.pergunta_atual >= len(perguntas):
                    st.session_state.pagina = "final"

                st.rerun()

    st.write(f"Pontuação atual: {st.session_state.pontos}")


# ---------------------------
# TELA FINAL
# ---------------------------
elif st.session_state.pagina == "final":
    st.title("Resultado Final 🎉")
    st.write(f"Pontuação final: {st.session_state.pontos}")

    if st.session_state.pontos >= 30:
        st.success("Você chegou longe! Continue se inspirando em Mary Jackson!")
    else:
        st.info("Nunca pare de aprender e sonhar grande!")

    if st.button("Reiniciar Quiz"):
        st.session_state.pagina = "inicio"
        st.session_state.pergunta_atual = 0
        st.session_state.pontos = 0
        st.session_state.tentativas = 0
        st.rerun()

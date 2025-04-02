
# Importando as bibliotecas
import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-pro-exp-02-05")

# Função principal do agente
def agente_responde(prompt):
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            candidate_count=1,
            max_output_tokens=8000,
            temperature=1.0
        )
    )
    return response.text.strip()

# Agente Tradutor Técnico
def agente_tradutor(texto_ingles):
    prompt = (
        f"Você é um tradutor técnico experiente. Traduza o seguinte texto do inglês para o português, ajustando para que ele seja claro e compreensível para estudantes de programação iniciantes:\n\n"
        f"{texto_ingles}"
    )
    return agente_responde(prompt)

# Agente Educador
def agente_educador(texto):
    prompt = (
        f"Você é um educador experiente. Crie um conteúdo didático baseado no texto abaixo, utilizando linguagem simples e exemplos práticos para ajudar iniciantes a entenderem o conceito:\n\n"
        f"{texto}"
    )
    return agente_responde(prompt)

# Agente Avaliador (Criador de Exercícios)
def agente_exercicios(texto):
    prompt = (
        f"Você é um criador de conteúdo educacional. Crie três pequenos exercícios baseados no texto abaixo para ajudar iniciantes a praticarem o conceito:\n\n"
        f"{texto}"
    )
    return agente_responde(prompt)

# Interface do Streamlit
st.title("Agentes Educacionais para Programação")

texto_input = st.text_area("Insira o texto técnico em inglês:", "")
acao = st.selectbox(
    "Escolha a ação:",
    ["Traduzir Texto", "Criar Conteúdo Didático", "Gerar Exercícios"]
)

if st.button("Executar"):
    if texto_input.strip() == "":
        st.warning("Por favor, insira um texto para continuar.")
    else:
        if acao == "Traduzir Texto":
            st.subheader("Texto Traduzido:")
            texto_traduzido = agente_tradutor(texto_input)
            st.write(texto_traduzido)

        elif acao == "Criar Conteúdo Didático":
            st.subheader("Conteúdo Didático:")
            conteudo_didatico = agente_educador(texto_input)
            st.write(conteudo_didatico)

        elif acao == "Gerar Exercícios":
            st.subheader("Exercícios Criados:")
            exercicios = agente_exercicios(texto_input)
            st.write(exercicios)

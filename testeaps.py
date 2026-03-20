import streamlit as st
st.title("Meu script na web")
nome = st.text_input("Digite seu nome")
if st.button("Enviar"):
    st.success(f"Olá, {nome}!")


import os
import streamlit as st

# API Key Codes - Replace w. Streamlit Secrets
openaikey = st.secrets['OPENAI_API_KEY']
password = st.secrets['PASSWORD']

# Streamlit logic

st.title("Innovative Minds 🧠⭐")

st.subheader("Welcome to Innovative Minds!")

st.write("Innovative minds is a collection of examples of the AI powered tools that I want to develop to support Neurodiverse Entrepreneurs to run their own businesses.")

st.write("""You can access the following tools using the menu to your left:

- ✉️ **Easy Write**
- ⁉️ **Understood AI**
- 📋 **Problem Statement Canvas**

""")
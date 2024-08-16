import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import os
from dotenv import load_dotenv


st.title("🔎 LangChain - Chat with search")
"""
In this example, we're using `StreamlitCallbackHandler` to display the thoughts and actions of an agent in an interactive Streamlit app.
Try more LangChain 🤝 Streamlit Agent examples at [github.com/langchain-ai/streamlit-agent](https://github.com/langchain-ai/streamlit-agent).
"""

if "message" not in st.session_state:
    st.session_state["message"] = [
        {"role":"assisstant","content":"Hi,I'm a chatbot who can search the web. How can I help you?"}
    ]
for msg in st.session_state.message:
    st.chat_message(msg["role"]).write(msg['content'])

st.write(st.session_state)

if prompt := st.chat_input(placeholder="What is machine learning?"):
    st.session_state.message.append({"role":"user","content":prompt})
    st.chat_message("user").write(prompt)
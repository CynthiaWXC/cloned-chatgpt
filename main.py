import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response

st.title(" the Clone of ChatGPT")

with st.sidebar:
    openai_api_key = st.text_input("Please enter your OpenAI API Key: ", type="password")
    st.markdown("[ To Get the OpenAI API Key](https://platform.openai.com/api-keys)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "Hello, I am your AI assistant, is there anything I can help you with?"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("Please enter your OpenAI API Key")
        st.info()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI is thinking, please wait for a second..."):
        response = get_chat_response(prompt, st.session_state["memory"],
                                     openai_api_key)

    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)
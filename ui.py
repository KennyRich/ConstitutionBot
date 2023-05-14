import os
import streamlit as st
from utils import get_initial_message, update_chat, get_chatgpt_response
from streamlit_chat import message

from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(
    page_title="Streamlit Chat - Demo",
    page_icon=":robot:"
)


st.header("Nigerian Constitution AI 📚")
st.subheader("Ask me anything about the constitution")


if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))

query = st.text_input("Query: ", key="input")

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()

if query:
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(query)

        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)



    # with st.expander("Show Messages"):
    #     st.write(messages)
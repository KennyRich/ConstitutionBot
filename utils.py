from chatbot import DocQAChatbot
from typing import IO


def get_initial_message():
    messages = [
        {"role": "system", "content": "You are a helpful AI Tutor. Who answers brief questions about the Nigerian constitution."},
        {"role": "user", "content": "I want to learn more about the Nigerian Constitution"},
        {"role": "assistant", "content": "That's awesome, what do you want to know about AI"}
    ]
    return messages


def get_chatgpt_response(query):
    doc_qa = DocQAChatbot()
    return doc_qa.retrieve_answers(query=query)


def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

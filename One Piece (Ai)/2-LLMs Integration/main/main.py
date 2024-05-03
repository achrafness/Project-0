import streamlit as st
import ollama

st.title("🌌 Multiverse Chat")

def is_one_piece(input_text):
    one_piece_keywords = ["one piece", "luffy", "zoro", "nami", "sanji", "robin", "chopper", "franky", "brook", "jinbe", "mugiwara", "pirate king"]
    for keyword in one_piece_keywords:
        if keyword in input_text.lower():
            return True
    return False
def is_watch_dogs(input_text):
    watch_dogs_keywords = ["watch dogs", "aiden pearce", "dedsec", "ctos", "blume", "san francisco", "chicago", "london"]
    for keyword in watch_dogs_keywords:
        if keyword in input_text.lower():
            return True
    return False
def is_doctor_strange(input_text):
    doctor_strange_keywords = ["doctor strange", "stephen strange", "sorcerer supreme", "time stone", "sanctum sanctorum", "wong", "mordo", "baron mordo"]
    for keyword in doctor_strange_keywords:
        if keyword in input_text.lower():
            return True
    return False
def is_sherlock(input_text):
    sherlock_keywords = ["sherlock", "sherlock holmes", "john watson", "baker street", "irene adler", "moriarty", "the hound of the baskervilles"]
    for keyword in sherlock_keywords:
        if keyword in input_text.lower():
            return True
    return False
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

### Write Message History
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message(msg["role"], avatar="🧑‍💻").write(msg["content"])
    else:
        st.chat_message(msg["role"], avatar="🤖").write(msg["content"])

def generate_response():
    response = ollama.chat(model='llama2', stream=True, messages=st.session_state.messages)
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        st.session_state["full_message"] += token
        yield token

if prompt := st.chat_input():
    if  is_one_piece(prompt) or is_watch_dogs(prompt) or is_doctor_strange(prompt) or is_sherlock(prompt):
        if is_one_piece(prompt):
            st.warning("WELCOME TO ONE PIECE WORLD! 🏴‍☠️🌊🦜🏝")
        if is_watch_dogs(prompt):
            st.warning("WELCOME TO WATCH DOGS WORLD! 🎮🏙🔒💻")
        if is_doctor_strange(prompt):
            st.warning("WELCOME TO DOCTOR STRANGE WORLD! 🧙‍♂️🌀🔮🕰")
        if is_sherlock(prompt):
            st.warning("WELCOME TO SHERLOCK HOLMES WORLD! 🕵️‍♂️🔍🎻🔎")
    else :
        st.warning("the subject  is out of 4 universe")
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="🧑‍💻").write(prompt)
    st.session_state["full_message"] = ""
    st.chat_message("assistant", avatar="🤖").write_stream(generate_response)
    st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
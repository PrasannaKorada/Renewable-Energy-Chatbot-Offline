
import streamlit as st
import json

st.set_page_config(page_title="Renewable Energy Chatbot (Offline)", layout="centered")
st.title("🔋 Renewable Energy Awareness Chatbot")
st.markdown("Ask me about Renewable Energy Resources!")

# Load the full Q&A dataset from JSON file
with open("C:/Users/kittu/Downloads/renewable_energy_chatbot_offline.py/renewable_energy_qa_full.json", "r") as f:

    faq = json.load(f)

# Input from user
user_input = st.text_input("💬 Ask a question:")

if user_input:
    question = user_input.lower().strip()
    response = None
    for key in faq:
        if key in question or question in key:
            response = faq[key]
            break
    if response:
        st.success("Answer:")
        st.write(response)
    else:
        st.warning("Sorry, your que is wrong!!")
        
st.markdown("---")
st.caption("Offline chatbot demo for capstone presentation. No API required.")

import streamlit as st

st.title("AI Mid-Care Assistant (Preview Version)")

st.header("Chat with Assistant")
st.text_input("Enter your health query...")
st.button("Ask")

st.header("Log Symptoms")
st.text_input("Describe your symptom...")
st.button("Log Symptom")

st.header("Log Medical History")
st.text_input("Medical condition...")
st.button("Save History")

st.info("🔒 Full features will be added after final submission.")

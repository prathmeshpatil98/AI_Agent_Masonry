# app.py

import streamlit as st
from research_agent import research_agent

st.set_page_config(page_title="Web Research Agent", layout="centered")

st.title("🔎 Masonry Web Research Agent")
st.markdown(
    "This AI-powered agent will automatically search the web, extract data, analyze content "
    "and provide a comprehensive research report based on your User query."
)

query = st.text_input("🧠 Enter your research topic or question That you have :")

if query:
    with st.spinner("⏳ Researching the web... please wait."):
        try:
            report = research_agent(query)
            st.success("✅ Research Complete!")

            st.subheader("📄 Final Research Report")
            st.markdown(report, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Something went  wrong: {e}")
else:
    st.info("Please Enter a topic to begin research.")

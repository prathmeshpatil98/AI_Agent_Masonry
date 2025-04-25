# app.py

import streamlit as st
from research_agent import research_agent

# --------------------------------
# Page Configuration
# --------------------------------
st.set_page_config(
    page_title="Web Research Agent | Masonry AI",
    layout="centered",
    page_icon="🔎"
)

# --------------------------------
# Branding Header
# --------------------------------
st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 600;
            margin-bottom: 0.2em;
            color: #4B8BBE;
        }
        .subtitle {
            text-align: center;
            font-size: 1.1rem;
            color: #6c757d;
            margin-bottom: 2em;
        }
        .report-box {
            background-color: #f9f9f9;
            padding: 1.5em;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }
        .stTextInput > div > div > input {
            font-size: 16px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🔎 Masonry Web Research Agent</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">'
    'Let this intelligent agent search, extract and analyze web data for you  delivering a full and perfect report in seconds.'
    '</div>', unsafe_allow_html=True
)

# --------------------------------
# Input & Query Box
# --------------------------------
query = st.text_input("💬 Enter your research topic or question:")

# --------------------------------
# Trigger Agent on Input
# --------------------------------
if query:
    with st.spinner("⏳ Researching the web... please wait."):
        try:
            report = research_agent(query)
            st.success("✅ Research Complete!")

            st.subheader("📄 Final Research Report")
            st.markdown(f"<div class='report-box'>{report}</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
else:
    st.info("👆 Please enter a topic above to begin your research.")

# --------------------------------
# Footer (Optional)
# --------------------------------
st.markdown(
    """
    <hr style="margin-top:3em">
    <center style="color:gray; font-size: 0.85em;">
        Built with ❤️ by <b>Masonry AI</b> | Powered by Gemini + Open Web
    </center>
    """,
    unsafe_allow_html=True
)

import os
import logging
from dotenv import load_dotenv
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# -------------------------------
# Logging
# -------------------------------
logging.basicConfig(level=logging.INFO)

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()

if not os.getenv("LANGCHAIN_API_KEY"):
    logging.warning("LANGCHAIN_API_KEY not found")

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "Coding-Assistant")

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Coding Assistant",
    page_icon="💻",
    layout="centered"
)

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:
    st.header("⚙️ Settings")
    language = st.selectbox(
        "Preferred Domain",
        ["General", "Python", "SQL", "Machine Learning", "Data Science"]
    )
    st.markdown("---")
    st.markdown("💡 **Tip:** Ask clear coding questions")
    st.markdown("❌ No memory is stored")

# -------------------------------
# Main UI
# -------------------------------
st.title("💻 Coding Assistant")
st.caption("Stateless AI • Coding & Computer Science Only")
st.info(f"📌 Current Mode: {language} (No memory)")

st.markdown(
    """
    Ask questions related to:
    - Programming
    - Data Structures & Algorithms
    - SQL
    - Machine Learning
    - Computer Science concepts
    """
)

# -------------------------------
# Prompt
# -------------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a DOMAIN-LOCKED coding assistant.

SELECTED DOMAIN = {language}

Your job is to answer ONLY within this domain.
You must FIRST classify the user's question internally before answering.

======================
ALLOWED DOMAINS
======================

• SQL
- Queries (SELECT, JOIN, GROUP BY, WINDOW FUNCTIONS)
- Indexes, constraints, normalization
- Stored procedures, views
- Database concepts ONLY

• Python
- Python syntax, functions, OOP
- Algorithms implemented in Python
- Libraries like numpy, pandas, matplotlib

• Machine Learning
- ML algorithms, math intuition
- Model training, evaluation
- Scikit-learn, deep learning concepts

• Data Science
- EDA, statistics
- Feature engineering
- Data pipelines, visualization

• General
- Basic CS theory only
- No coding unless explicitly asked

======================
STRICT RULES
======================

1. If the question DOES NOT belong to the SELECTED DOMAIN,
respond with exactly:

"Please ask a question related to {language} only."

2. Do not provide partial hints outside the domain.
3. Be concise and correct.
4. Stateless behavior. No memory.
            """
        ),
        ("user", "{question}")
    ]
)

# -------------------------------
# LLM & chain
# -------------------------------
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser


# -------------------------------
# Helper functions
# -------------------------------

def is_valid_query(query: str) -> bool:
    if not query:
        return False
    if len(query.strip()) < 5:
        return False
    return True


def get_llm_response(question: str, language: str) -> str:
    try:
        logging.info("Query received | Domain=%s | Question=%s", language, question)

        response = chain.invoke(
            {
                "question": question,
                "language": language
            }
        )

        return response

    except Exception as e:
        logging.exception("LLM call failed")
        return "__LLM_ERROR__"


# -------------------------------
# Input Section
# -------------------------------
question = st.text_area(
    "🧠 Enter your coding question:",
    placeholder="e.g. Write a SQL query to find duplicate records",
    height=120
)

col1, col2 = st.columns([1, 1])

with col1:
    ask_btn = st.button("🚀 Ask")

with col2:
    clear_btn = st.button("🧹 Clear")

# -------------------------------
# Clear input
# -------------------------------
if clear_btn:
    st.rerun()

# -------------------------------
# Generate response
# -------------------------------
if ask_btn:

    if not is_valid_query(question):
        st.warning("Please enter a clearer and longer coding-related question.")
        st.stop()

    with st.spinner("Thinking... 🤔"):

        result = get_llm_response(question, language)

    if result == "__LLM_ERROR__":
        st.error(
            "LLM service is not available.\n\n"
            "Please make sure Ollama is running and the model is loaded."
        )
        st.stop()

    st.markdown("### ✅ Answer")
    st.markdown(result)

    with st.expander("📌 Why this answer?"):
        st.markdown(
            f"""
- Generated using a **stateless, domain-restricted coding assistant**
- Selected domain: **{language}**
"""
        )

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("⚡ Powered by Ollama • LangChain • Streamlit")

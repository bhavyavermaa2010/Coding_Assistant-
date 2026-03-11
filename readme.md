💻 AI Coding Assistant using LangChain, Ollama (LLaMA3) and Streamlit

A **stateless AI-powered coding assistant** built using **Ollama**, **LangChain**, and **Streamlit**.  
This assistant answers **only coding & computer science–related questions** and strictly follows the **selected domain**.

---

## 🚀 Features

- 🔒 **Domain-locked responses**
  - General CS
  - Python
  - SQL
  - Machine Learning
  - Data Science
- 🧠 Stateless behavior (no memory stored)
- ⚡ Powered by **local LLM (Ollama – LLaMA3)**
- 🎛️ Clean Streamlit UI with sidebar controls
- 🛑 Automatically rejects out-of-domain questions

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit**
- **LangChain**
- **Ollama (LLaMA3)**
- **LangSmith (Tracing & Monitoring)**
- **dotenv**

---

## 📂 Project Structure

├── Coding_Assistant_Ollama.py # Main Streamlit app
├── olla.ipynb # Experiment / testing notebook
├── requirements.txt # Project dependencies
├── .env # Environment variables (not pushed)
├── .gitignore
└── README.md




---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/coding-assistant-ollama.git
cd coding-assistant-ollama


2️⃣ Create virtual environment (recommended)
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Linux / macOS

source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup environment variables

Create a .env file:

LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_PROJECT=Coding-Assistant


⚠️ Never push .env to GitHub

5️⃣ Run Ollama (Required)

Make sure Ollama is installed and LLaMA3 model is pulled:

ollama pull llama3
ollama run llama3

6️⃣ Run the Streamlit app
streamlit run Coding_Assistant_Ollama.py



🧠 How It Works

User selects a domain from sidebar

Question is internally classified

If question ❌ does not belong to selected domain → rejected

If valid ✅ → answered using Ollama LLM

No chat history or memory is stored



📌 Example Use Cases

SQL queries & database concepts

Python coding problems

Machine Learning theory

Data Science workflows

Core Computer Science concepts



🔐 Limitations

No non-technical questions allowed

No cross-domain answers

No memory or personalization



## ⚠️ Deployment Note

This application uses a locally hosted LLM via Ollama and is intended for local execution only.
Cloud deployment is not supported in the current version.


👨‍💻 Author

Bhavya Verma
💡 AI / ML | Full Stack | Open Source Learner




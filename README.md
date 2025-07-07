# 🧠 AI-Powered Web Scraper & Summarizer with FAISS-Backed Q&A

This is a sleek, AI-driven Streamlit application that **scrapes content from any public website**, **stores it in a FAISS vector database**, and allows you to **ask intelligent questions** about the stored content using the **Mistral language model via LangChain + Ollama**.

> 🔍 Scrape → 💾 Store → 🤖 Ask → 🧠 Get Answers — All in one interactive interface! (Basic Python Codes Present Can imporve UI with interactive Frontend)

---

## 🚀 Features

- 🔎 **Smart Web Scraper**  
  Extracts visible text (`<p>` tags) from any given URL using `BeautifulSoup`.

- 🤖 **AI Summarization & Question Answering**  
  Uses the powerful **Mistral model** (via Ollama) for summarizing and answering queries intelligently.

- 💾 **FAISS Vector Storage**  
  Stores and indexes the webpage content in chunks for fast similarity search and contextual retrieval.

- 🧭 **Interactive Streamlit UI**  
  A smooth front-end interface for scraping, storing, and interacting with website knowledge.

- 💥 **Robust Error Handling**  
  Handles broken URLs, failed requests, and empty pages gracefully.

---

## 🧰 Tech Stack

| Tech | Role |
|------|------|
| [Streamlit](https://streamlit.io/) | UI Framework |
| [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) | Web Scraping |
| [LangChain](https://www.langchain.com/) | LLM Orchestration |
| [Ollama](https://ollama.com/) | Local Model Execution |
| [Mistral](https://mistral.ai/) | Language Model |
| [FAISS](https://github.com/facebookresearch/faiss) | Vector Search Index |
| [HuggingFace Transformers](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) | Embeddings |
| Python 3.8+ | Core Language |

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/ashdyl17/aiwebscraper.git
cd ai-webscraper
```
### 2. Ensure there is ollama installed
```bash
ollama pull mistral
```
### 3. Launch the app
```bash
streamlit run aiwebscraper.py
```

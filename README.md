# 🧠 AI-Powered Web Scraper & Summarizer

This is a sleek, Streamlit application that scrapes content from any public website and generates a concise summary using the **Mistral language model** via `Langchain + Ollama`.

---

## 🚀 Features

- 🔎 **Smart Web Scraper**: Extracts visible text content (`<p>` tags) from any URL.
- 🤖 **AI Summarization**: Uses Mistral via LangChain and Ollama to summarize the scraped content in 3–5 sentences.
- 🧭 **Interactive Instructions**: Clear step-by-step usage guidance built into the app.
- 💥 **Robust Error Handling**: Friendly error messages for bad URLs or failure

---

## 🧰 Tech Stack

- [Streamlit](https://streamlit.io/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [LangChain](https://www.langchain.com/)
- [Ollama](https://ollama.com/) + [Mistral](https://mistral.ai/)
- [Python 3.8+](https://www.python.org/)

---

## 🛠️ Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```
### 2. Ensure there is ollama installed
```bash
ollama pull mistral
```
### 3. Launch the app
```bash
streamlit run aiwebscraper.py
```

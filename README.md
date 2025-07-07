# 🧠 AI-Powered Web Scraper & Summarizer with FAISS-Backed Q&A

This is a sleek, AI-driven Streamlit application that **scrapes content from any public website**, **stores it in a FAISS vector database**, and allows you to **ask intelligent questions** about the stored content using the **Mistral language model via LangChain + Ollama**.

> 🔍 Scrape → 💾 Store → 🤖 Ask → 🧠 Get Answers — All in one interactive interface!

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
![Output Sample](https://github.com/user-attachments/assets/88ad4326-7b5f-495e-be67-c4486b3aa387)

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

### 1. Clone the Repository
```bash
git clone https://github.com/ashdyl17/aiwebscraper.git
cd ai-webscraper
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Then, install the required packages:
```bash
pip install -r requirements.txt
```

### 3. Install and Configure Ollama
Install Ollama and pull the Mistral model:
```bash
ollama pull mistral
```

### 4. Launch the Application
Run the Streamlit app:
```bash
streamlit run aiwebscraper.py
```

### 5. Access the App
Open your browser and navigate to `http://localhost:8501` to use the interactive UI.

---

## 📝 Usage

1. **Enter a URL**: Input the URL of a public website in the text box.
2. **Scrape Content**: The app will scrape the text content (from `<p>` tags) and store it in a FAISS vector database.
3. **Ask Questions**: Enter a question related to the scraped content, and the Mistral model will provide an intelligent answer based on the stored data.

---

## ⚠️ Notes

- Ensure you have a stable internet connection for web scraping and model downloads.
- The app limits scraped content to 5,000 characters to avoid overloading. Adjust this limit in the code if needed.
- Ollama must be running locally to use the Mistral model.
- FAISS requires sufficient memory for indexing large datasets.


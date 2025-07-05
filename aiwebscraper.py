import requests
from bs4 import BeautifulSoup
import streamlit as st
from langchain_ollama import OllamaLLM

# Initialize the language model
llm = OllamaLLM(model="mistral")

# Function to scrape website content
def scrape_website(url):
    try:
        with st.spinner("Scraping website..."):
            headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                return f"Failed to fetch {url}. Status code: {response.status_code}"
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            text = " ".join([p.get_text(strip=True) for p in paragraphs])
            return text[:2000] if text else "No content found."
    except Exception as e:
        return f"Error: {str(e)}"

# Function to summarize content
def summarize_content(content):
    with st.spinner("Generating summary..."):
        try:
            summary = llm.invoke(f"Summarize the following content in 3-5 sentences: \n\n{content[:1000]}")
            return summary
        except Exception as e:
            return f"Error summarizing content: {str(e)}"

# Custom CSS for Apple-inspired UI with light/dark theme support
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    body {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    @media (prefers-color-scheme: dark) {
        body {
            background: linear-gradient(135deg, #1e1e1e 0%, #2c2c2c 100%);
        }
        .stApp {
            background: rgba(34, 34, 34, 0.95);
            color: #ffffff;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .stTitle {
            color: #ffffff;
        }
        .stMarkdown p {
            color: #dddddd;
        }
        .summary-box {
            background: #2a2a2a;
            color: #ffffff;
            border: 1px solid #444;
        }
        .error-box {
            background: #3a1a1a;
            border: 1px solid #b33a3a;
            color: #ffcccc;
        }
        .instructions-box {
            background: rgba(255, 255, 255, 0.05);
            color: #dddddd;
            padding: 1rem 1.5rem;
            border-left: 4px solid #007aff;
            border-radius: 8px;
            margin-top: 1rem;
            margin-bottom: 2rem;
            font-size: 0.95rem;
            line-height: 1.6;
        }
    }

    @media (prefers-color-scheme: light) {
        body {
            background: linear-gradient(135deg, #f5f7fa 0%, #e4e7eb 100%);
        }
        .stApp {
            background: rgba(255, 255, 255, 0.95);
            color: #1a1a1a;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .stTitle {
            color: #1a1a1a;
        }
        .stMarkdown p {
            color: #333;
        }
        .summary-box {
            background: #f9f9f9;
            color: #000;
            border: 1px solid #e1e1e1;
        }
        .error-box {
            background: #ffe5e5;
            border: 1px solid #ff9999;
            color: #d32f2f;
        }
        .instructions-box {
            background: #e6f0ff;
            color: #003366;
            border-left: 4px solid #005bb5;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            margin-top: 1rem;
            margin-bottom: 2rem;
            font-size: 0.95rem;
            line-height: 1.6;
        }
    }

    .stApp {
        width: 100vw;
        min-height: 100vh;
        padding: 4rem 5%;
        border-radius: 0;
        box-shadow: none;
        background-size: cover;
        background-attachment: fixed;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
    }

    .stTitle {
        font-size: 2.5rem;
        font-weight: 600;
        text-align: center;
        margin-bottom: 0.5rem;
    }

    .stMarkdown p {
        font-size: 1.1rem;
        line-height: 1.6;
        text-align: center;
    }

    .stTextInput > div > div > input {
        border: 1px solid #d1d1d1;
        border-radius: 12px;
        padding: 12px 16px;
        font-size: 1rem;
        color-scheme: dark;
        color: #ffffff;
        background: #2a2a2a;
        transition: all 0.3s ease;
    }

    @media (prefers-color-scheme: light) {
        .stTextInput > div > div > input {
            color: #000000;
            background: #ffffff;
        }
    }

    .stTextInput > div > div > input:focus {
        border-color: #007aff;
        box-shadow: 0 0 0 3px rgba(0, 122, 255, 0.2);
        background: rgba(34, 34, 34, 0.8);
        color: #ffffff;
    }

    @media (prefers-color-scheme: light) {
        .stTextInput > div > div > input:focus {
            background: rgba(44, 44, 44, 0.9);
            color: #ffffff;
        }
    }

    .stButton > button {
        background: linear-gradient(135deg, #007aff 0%, #005bb5 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 1rem;
        font-weight: 500;
        width: 100%;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #005bb5 0%, #003087 100%);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }

    .stSpinner {
        color: #007aff;
    }

    .summary-box {
        max-width: 100%;
        font-size: 1.05rem;
        line-height: 1.7;
        padding: 2rem;
        margin-top: 2rem;
        border-radius: 16px;
        box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
    }

    .error-box {
        border-radius: 12px;
        padding: 1rem;
        margin-top: 1rem;
    }

    @media (max-width: 600px) {
        .stApp {
            padding: 1rem;
        }
        .stTitle {
            font-size: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("AI-Powered Web Scraper")
st.markdown("Enter a website URL to get a beautifully summarized version, powered by AI.")

st.markdown("""
<div class="instructions-box">
    <strong>How to use:</strong><br>
    1. Enter a full website URL (including http/https).<br>
    2. Click <em>Scrape & Summarize</em> to extract and summarize the main content.<br>
    3. Wait for the results to appear below.
</div>
""", unsafe_allow_html=True)

# Input form
with st.form(key="scraper_form"):
    url = st.text_input("Enter Website URL", placeholder="https://example.com")
    submit_button = st.form_submit_button(label="Scrape & Summarize")

# Process the input
if submit_button and url:
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    content = scrape_website(url)
    if "Failed" in content or "Error" in content:
        st.markdown(f'<div class="error-box">{content}</div>', unsafe_allow_html=True)
    else:
        summary = summarize_content(content)
        st.subheader("Website Summary")
        st.markdown(f'<div class="summary-box">{summary}</div>', unsafe_allow_html=True)

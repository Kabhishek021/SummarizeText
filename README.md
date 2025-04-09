# SummarizeText
# PDF Summarization App (Map-Reduce)
![image alt](https://github.com/Kabhishek021/SummarizeText/blob/main/Summarize_image.png)
## 📌 Overview
This is a **Streamlit-based PDF Summarization App** that utilizes **LangChain's Map-Reduce strategy** to summarize uploaded PDF documents. The app leverages **Groq LLM** and **HuggingFace embeddings** for accurate text processing and summarization.

## 🚀 Features
- Upload a **PDF file** for summarization.
- Uses **LangChain's Map-Reduce** strategy for structured summarization.
- Supports **HuggingFace embeddings** for better text representation.
- Requires a **Groq API Key** (entered in the UI) to process the text.
- Interactive and user-friendly **Streamlit interface**.

## 🛠️ Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-repo/pdf-summarization-app.git
   cd pdf-summarization-app
   ```

2. **Create a virtual environment (optional but recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

## 🔑 Setting Up the Groq API Key
Since API keys are sensitive, they should not be exposed in the code. Instead, enter your API key in the **Streamlit UI** when prompted.

Alternatively, you can create a `.env` file and add:
   ```sh
   GROQ_API_KEY=your_api_key_here
   ```

## 📌 Running the App
To start the Streamlit app, run:
   ```sh
   streamlit run app.py
   ```

## 📄 How It Works
1. **User uploads a PDF file**.
2. **Text is extracted** from the PDF using `PyPDF2`.
3. **Text is split** into smaller chunks using `RecursiveCharacterTextSplitter`.
4. **Summarization chain (Map-Reduce)** is applied using LangChain and Groq LLM.
5. **Summarized text** is displayed on the UI.

## 📝 Requirements
Ensure the following dependencies are installed (**already included in `requirements.txt`**):
   ```sh
   streamlit
   python-dotenv
   PyPDF2
   langchain
   langchain-community
   langchain-groq
   sentence-transformers
   ```

## 📌 Contributing
Feel free to open issues and submit PRs if you'd like to contribute!

## 🛠️ License
This project is open-source and available under the **MIT License**.


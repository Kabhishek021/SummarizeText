import streamlit as st
import os
from dotenv import load_dotenv
import PyPDF2
load_dotenv()

from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.schema import Document

# Streamlit UI
st.set_page_config(layout="wide")
st.title("📝 PDF Summarization App (Map-Reduce)")
st.write("Upload a PDF, and we'll summarize it using LangChain!")

# Create two columns
col1, col2 = st.columns([1, 3])

with col1:
    # Input for Groq API Key
    groq_api_key = st.text_input("Enter your Groq API Key:", type="password")

with col2:
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if groq_api_key and uploaded_file:
        os.environ['GROQ_API_KEY'] = groq_api_key
        
        # Initialize components
        llm = ChatGroq(model_name="mixtral-8x7b-32768")  # Using a Groq LLM
        embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        
        # Extract text from PDF
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        
        if text.strip():
            # Split text into smaller chunks
            texts = text_splitter.split_text(text)
            docs = [Document(page_content=t) for t in texts]
            
            if st.button("Summarize"):
                # Load summarization chain with Map-Reduce strategy
                summarization_chain = load_summarize_chain(
                    llm, chain_type="map_reduce"
                )
                
                # Generate summary
                summary = summarization_chain.run(docs)
                
                st.subheader("📌 Summary:")
                st.write(summary)
        else:
            st.warning("The uploaded PDF contains no extractable text.")
    elif not groq_api_key:
        st.warning("Please enter your Groq API Key to proceed.")
    elif not uploaded_file:
        st.warning("Please upload a PDF file.")


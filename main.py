import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Function to extract text from PDFs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Function to get a conversational chain for Q&A
def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, 
    if the answer is not in the provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n
    Answer:
    """
    
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return prompt

# Function to generate the response based on user input and the context from the PDF
def user_input(user_question, context):
    prompt = get_conversational_chain()
    formatted_prompt = prompt.format(context=context, question=user_question)

    # Use the correct method for generating responses from the model
    model = genai.GenerativeModel(model_name="gemini-pro")  # Updated to use GenerativeModel
    response = model.generate_content(formatted_prompt)  # generate_content is the correct method

    return response.text.strip()

# Streamlit main app function
def main():
    st.set_page_config("Chat With Documents", page_icon="📚", layout="wide")

    # Custom CSS to style the app
    st.markdown("""
    <style>
    /* Body and general layout */
    .stApp {
        background-color: #f7f7f7;
        font-family: 'Arial', sans-serif;
    }

    /* Header style */
    .header {
        font-size: 50px;
        font-weight: bold;
        color: #1A73E8;
        text-align: center;
        padding: 30px;
        background-color: #f1f1f1;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }

    /* Sidebar title style */
    .sidebar-title {
        font-size: 24px;
        font-weight: bold;
        color: #333;
    }

    /* Input field style */
    .stTextInput input {
        font-size: 18px;
        padding: 15px;
        border-radius: 10px;
        border: 2px solid #1A73E8;
        width: 100%;
        box-sizing: border-box;
    }

    /* Compact Upload button style (acute) */
    .stButton button {
        background-color: #1A73E8;
        color: white;
        font-weight: bold;
        padding: 10px 20px;  /* Reduced padding for compact button */
        border-radius: 8px;  /* Slightly smaller rounded corners */
        width: auto;  /* Let the button width adjust to the content */
        transition: background-color 0.3s;
    }

    .stButton button:hover {
        background-color: #0f59c6;
    }

    /* Cards for text areas */
    .card {
        padding: 20px;
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }

    /* Response text style */
    .response-card {
        background-color: #e8f5e9;
        border-left: 5px solid #66bb6a;
    }

    /* Warning text style */
    .warning-text {
        color: #f44336;
        font-size: 18px;
    }

    </style>
    """, unsafe_allow_html=True)

    # Main header with title
    st.markdown('<h1 class="header">Chat With Documents 📄📚</h1>', unsafe_allow_html=True)

    # User question input in a card (Placed at the top)
    user_question = st.text_input("Ask a Question from the PDF Files", placeholder="Type your question here...")

    # Check if a question is provided
    if user_question:
        if "pdf_text" in st.session_state:
            with st.spinner("Getting response..."):
                response = user_input(user_question, st.session_state.pdf_text)
                
                # Store the question and response history in session state
                if "history" not in st.session_state:
                    st.session_state.history = []

                # Append the new question and response to history
                st.session_state.history.append({"question": user_question, "answer": response})

                # Display the new response in a styled card
                st.markdown(f'<div class="card response-card"><h3>Reply:</h3><p>{response}</p></div>', unsafe_allow_html=True)

        else:
            st.markdown('<p class="warning-text">Please upload a PDF first.</p>', unsafe_allow_html=True)

    # Sidebar for PDF upload and processing
    with st.sidebar:
        st.markdown('<h2 class="sidebar-title">Menu:</h2>', unsafe_allow_html=True)

        # File uploader for PDF documents inside a card
        pdf_docs = st.file_uploader("Upload your PDF Files", accept_multiple_files=True)

        # Button to process PDFs
        if st.button("Process PDFs"):
            if pdf_docs:
                with st.spinner("Processing PDFs..."):
                    raw_text = get_pdf_text(pdf_docs)
                    st.session_state.pdf_text = raw_text  # Store text in session state
                    st.success("PDF processed successfully!")
            else:
                st.warning("Please upload a PDF file.")

    # Display history at the bottom
    if "history" in st.session_state and st.session_state.history:
        st.markdown('<div class="card"><h3>Previous Q&A:</h3>', unsafe_allow_html=True)
        for entry in st.session_state.history:
            st.markdown(f'<strong>Q:</strong> {entry["question"]}<br><strong>A:</strong> {entry["answer"]}<br><br>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()

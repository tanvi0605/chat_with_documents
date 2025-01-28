# Chat_with_documents
Project Title: Chat with PDF using Gemini 💬📄
Project Overview
This project allows you to interact with a PDF document using an AI-powered conversational interface. By uploading your PDF, you can ask questions, and the model will extract the information from the document to provide relevant answers.

This is built using Streamlit, LangChain, Google Generative AI, and Sentence Transformers.

Key Features:
Upload multiple PDF files.
Automatically extracts and splits text from PDF into chunks.
Uses embedding models to process the text.
Allows users to ask questions and get answers based on the content of the PDF.

Technologies Used 💻🔧
Python 3.x – Programming language
Streamlit – Framework for creating the web interface
LangChain – For chaining language model operations
Google Generative AI – For using embeddings and language models
Sentence-Transformers – For text embeddings
FAISS – For storing and querying embeddings efficiently
PyPDF2 – For reading and extracting text from PDF files


How to Use the Chatbot 💬
Upload your PDF: In the sidebar, click on "Upload your PDF Files". Select one or multiple PDF files to upload.

Process the PDFs: Click the "Submit & Process" button. The text from the PDF will be extracted and indexed.

Ask Questions: Once processing is done, type a question in the input box. The model will respond based on the content of your uploaded PDF.

Example:
Question: "What is the main topic of the document?"
Answer: The model will provide the best possible answer by processing the text in the document.
Project Structure 📁
Here’s the structure of the project files:





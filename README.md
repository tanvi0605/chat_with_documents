# **Chat with Documents** 📚💬

## **Transform Your PDFs into Conversational Powerhouses!** 🌟

### 🚀 **Overview**
Welcome to the *Chat with PDF using Gemini* project! Imagine being able to chat with a document as if it were a knowledgeable assistant. Upload your PDF files, ask questions, and **watch the magic happen** as the AI processes the content and gives you accurate, context-based answers. 

Built with **Streamlit**, **LangChain**, **Google Generative AI**, and **Sentence Transformers**, this app lets you turn static PDF files into dynamic conversations. 🤖💬

### ✨ **Key Features:**
- **Multiple PDF Uploads**: Upload one or more PDFs in seconds. 📄
- **Smart Text Processing**: Automatically extracts and splits text from PDFs into manageable chunks. 📑
- **Embedding Magic**: Utilizes advanced embedding models to make sense of the text. 🔮
- **Interactive Q&A**: Ask anything, and get responses based on the content of your uploaded documents! 🔍❓

---

## 💻 **Technologies Used** 🔧
This project uses some of the coolest tools in AI and data processing:
- **Python 3.x** – The backbone of this app. 🐍
- **Streamlit** – For creating a sleek and responsive web interface. 🎨
- **LangChain** – For chaining multiple AI models into one powerful tool. 🔗
- **Google Generative AI** – To generate embeddings and connect dots in the document. 🌐
- **Sentence-Transformers** – For making text embeddings smarter and faster. ⚡
- **FAISS** – To store and search embeddings like a pro. 🔎
- **PyPDF2** – The magic wand for extracting text from PDFs. ✨

---

## 🌟 **How to Use the Chatbot** 💬

Get ready to interact with your PDFs in a whole new way! Here's how to start:

### 1. **Upload Your PDF** 📝
Head to the sidebar and click on "**Upload your PDF Files**". You can select one or more PDFs to upload. It's super easy! 👇

### 2. **Process the PDFs** 🔄
Once you've uploaded your files, click **"Submit & Process"** to extract and index the text. Your documents will be ready for intelligent questioning. 📂➡️🔍

### 3. **Ask Your Questions** 🤔
After processing is complete, simply type your questions in the input box. Based on the content in your PDFs, the model will generate thoughtful answers. Ask away! 🗨️💡

#### **Example:**
- **Question**: "What is the main topic of the document?"
- **Answer**: The model will provide the most relevant answer based on the document’s content. 🎯

---

## 🏗️ **Project Structure** 📂

Here's what the project looks like under the hood:

```bash
your-repository-name/
│
├── app.py                 # The magic code that powers the Streamlit app
├── requirements.txt       # List of Python dependencies (for non-conda users)
├── .env                   # Your secret environment variables (API keys)
├── README.md              # This file - your guide to the project!
└── faiss_index/           # Where the FAISS vector store is saved (for efficient querying)

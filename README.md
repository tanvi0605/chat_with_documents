# **Chat with Documents** 📚💬

## **Transform Your PDFs into Conversational Powerhouses!** 🌟

### 🚀 **Overview**
Welcome to the *Chat with PDF using Gemini* project! Imagine being able to chat with a document as if it were a knowledgeable assistant. Upload your PDF files, ask questions, and **watch the magic happen** as the AI processes the content and gives you accurate, context-based answers.

Built with **LangChain**, **Streamlit**, and **Google Generative AI**, this app lets you turn static PDF files into dynamic conversations. 🤖💬

### ✨ **Key Features:**
- **Single PDF Upload**: Upload a PDF in seconds and start interacting with it. 📄
- **Interactive Q&A**: Ask anything, and get responses based on the content of your uploaded document! 🔍
- **History Preservation**: Keep track of all your previous questions and answers. 📝
- **Download History**: Download your entire conversation history in a neat CSV file for reference or further analysis. 📥
- **Customizable Answer Length**: Get brief, medium, or detailed responses based on your preference. 📄
- **Text Preview**: Preview the content of the uploaded document before interacting. 📑

---

## **Technologies Used** 💻 
This project uses some of the coolest tools in AI and data processing:
- **LangChain** – For chaining multiple AI models into one powerful tool. 🔗
- **Google Generative AI** – For generating responses based on document context and user queries. 🌐
- **Streamlit** – For creating a sleek and responsive web interface. 🎨
- **PyPDF2** – For extracting text from PDF files. 📄

---

## **How to Use the Chatbot** 💬

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

## 🖼️ **Result & History Preservation**

- **Sample Result:**
  ![Image](https://github.com/user-attachments/assets/d1ab5363-87c9-49aa-a586-8feb29f0cb0f)
  *Above is an example of how the model generates responses based on the document content.*

- **History Preservation & Download:**
  All your questions and answers are stored in history for easy reference. You can **download** the conversation history in a CSV format by clicking the **"Download History"** button, making it easy to save or analyze your interactions. 🗂️💾

  ![Image](https://github.com/user-attachments/assets/e64322f8-9423-4676-a670-404068ad33ad)
  *This feature preserves your previous interactions, allowing you to revisit your questions and answers anytime and download the history if needed!*

---

## 🏗️ **Project Structure** 📂

Here's what the project looks like under the hood:

```bash
Chat_with_documents/
│
├── main.py                      # Core app logic
├── .env                          # Environment variables (API keys, etc.)
├── README.md                     # You're looking at it! 😉



# 📊 **CSV Data Explorer with Crew AI**

Welcome to the **CSV Data Explorer** repository! 🚀 This project showcases the use of **Crew AI**, a framework for building and managing intelligent agents, to analyze and extract insights from CSV files interactively. The system leverages advanced language models to understand and respond to user queries, providing a seamless way to explore your data.

---
![Image](https://github.com/user-attachments/assets/16fe712e-fe54-48cd-802c-cda21db6ac4d)

## 🧠 **About Crew AI**

Crew AI is a framework for creating intelligent agents capable of performing specific tasks with predefined goals. Each **Agent** can:
- Perform autonomous actions or collaborate with other agents in a **Crew**.
- Process tasks sequentially or in parallel.
- Utilize knowledge sources (like CSV files) to make informed decisions.

This repository leverages Crew AI to build an interactive agent designed to analyze and answer questions about CSV files.

---


## ✨ **Features**

- 🤖 **AI-Powered Insights**: Uses **Crew AI** agents and powerful language models to process and analyze CSV data.
- 📂 **CSV Knowledge Integration**: Automatically parses and understands the structure of uploaded CSV files.
- 🔍 **Interactive Q&A**: Ask detailed questions about your CSV file and receive intelligent answers.
- 🔐 **Secure API Access**: Implements environment-based API key management for secure interaction with AI services.
- 🛠️ **Highly Configurable**: Easy-to-modify agents, tasks, and workflows to suit your use case.

---

## 🛠️ **Setup and Installation**

### 2️⃣ Install Required Libraries
Make sure Python 3.8+ is installed. Install the dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Keys
Create a `.env` file in the root directory with your API keys:
```bash
touch .env
```
Add the following environment variables to the `.env` file:
```bash
GOOGLE_API_KEY=your-google-api-key
GROQ_API_KEY=your-groq-api-key
OPENROUTER_API_KEY=your-openrouter-api-key
```

### 4️⃣ Run the Project
Launch the interactive Q&A system:
```bash
python app.py
```

---

## 🚀 **How to Use**

1. Place your CSV file (e.g., `Employees.csv`) in the root directory.
2. Start the application and follow the prompts to ask questions about your data.
3. Type your queries into the terminal. For example:
   - "What is the average salary in the dataset?"
   - "List all employees in the IT department."
4. Type `exit` to close the program.

---

## 📄 **Project Structure**

- **`app.py`**: Main application script for initializing agents and handling user interaction.
- **`.env`**: Environment file for storing API keys securely.
- **`requirements.txt`**: List of required Python libraries.

---



## 🌟 **Acknowledgements**

- **Crew AI Framework** for enabling intelligent agent design.
- **LangChain and ChatGroq** for language model integration.
- **OpenAI** for providing API support for advanced LLMs.


# Demo 📽

Below is a demonstration of how the application works:

![Demo of the Application](https://github.com/Abdelrahman-Amen/CSV_Insights_with_Crew-AI/blob/main/Demo.gif)


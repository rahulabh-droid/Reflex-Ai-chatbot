# REFLECT AI Chatbot

A multi-model AI chatbot built using:
- Streamlit
- Gemini API
- Ollama
- Python

Features:
- Cloud LLM support
- Offline local LLM support
- Multi-model switching
- Modern futuristic UI
- Session chat memory

Models:
- Gemini 2.5 Flash
- Phi3 (Ollama)

Tech Stack:
- Python
- Streamlit
- Ollama
- Google Generative AI

## What AI System Did I Build?

Built a multi-model AI chatbot that supports both cloud and local LLMs using Gemini API and Ollama. The system allows users to switch between models, maintain session-based chat memory, and interact through a modern Streamlit interface. Designed to demonstrate practical LLM integration, API handling, and local AI deployment workflows.

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/rahulabh-droid/Reflex-Ai-chatbot
cd Reflex-AI-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

### 5. Add API Key

Create a `.env` file and add:

```env
GEMINI_API_KEY=your_api_key_here
```

### 6. Run Ollama (Optional for Local LLM)

Start Ollama locally:

```bash
ollama run phi3
```

### 7. Start the Application

```bash
streamlit run app.py
```

### 8. Open in Browser

```txt
http://localhost:8501
```

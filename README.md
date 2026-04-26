# 🤖 AI Engineering Journey — LLMs · LangChain · RAG · Agents · Deployment

> From Python fundamentals to production-deployed LLM applications — a structured 6-phase self-study roadmap.

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-latest-green)](https://python.langchain.com)
[![Groq](https://img.shields.io/badge/LLM-Groq%20%7C%20Llama3-orange)](https://groq.com)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-teal)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Deploy-Docker%20%7C%20Railway-blueviolet)](https://railway.app)

---

## 🚀 Live Project

**RAG PDF Chatbot** — Ask questions about any PDF using Llama 3 via Groq, deployed on Railway.

🔗 **[Live Demo](https://rag-pdf-chatbot-production-e417.up.railway.app/docs)** · **[Source Code](https://github.com/MinahilFatima123/rag-pdf-chatbot)** ← *(update link)*

---

## 📁 Repository Structure

```
ai-engineering/
│
├── phase-1-python-fundamentals/
│   └── project.py             # JSON config + API call + file output
│
├── phase-2-llm-basics/
│   └── chatbot.py            # Raw Groq API CLI chatbot (no frameworks)
│
├── phase-3-langchain-core/
│   └── project.py         # LangChain chatbot with conversation memory
│
├── phase-4-rag/
│   └── [→ Separate Repo]         # RAG PDF Chatbot (FastAPI + Docker + Railway)
│
├── phase-5-agentic-ai/
│   └── state_management.py    files etc          # ReAct agent with tools (LangGraph)
│
└── phase-6-production/
    └── [→ Separate Repo]         # Deployment covered in RAG chatbot repo
```

---

## ✅ Progress

| Phase | Topic | Status | Key Project |
|-------|-------|--------|-------------|
| 1 | Python Fundamentals | ✅ Complete | API script with JSON + file handling |
| 2 | LLM Basics | ✅ Complete | CLI chatbot via Groq API (no frameworks) |
| 3 | LangChain Core | ✅ Complete | Memory chatbot with ChatPromptTemplate + LCEL |
| 4 | RAG — Retrieval Augmented Generation | ✅ Complete | [RAG PDF Chatbot →](https://github.com/MinahilFatima123/rag-pdf-chatbot) |
| 5 | Agentic AI | ✅ Complete | LangGraph agent with tools |
| 6 | Production & Deployment | ✅ Complete | FastAPI + Docker + Railway + LangSmith |

---

## 🛠️ Tech Stack

**LLMs & AI**
- Groq API (Llama 3) — primary LLM provider
- LangChain — chains, memory, LCEL, RAG
- LangSmith — tracing and evaluation
- ChromaDB — vector store for embeddings
- HuggingFace — embedding models

**Backend & Deployment**
- FastAPI — REST API wrapper
- Docker — containerization
- Railway — cloud deployment
- Python-dotenv — secure key management

---

## 📌 Highlighted Projects

### 1. CLI LLM Chatbot (`phase-2-llm-basics/`)
A framework-free command-line chatbot built directly on the Groq API.
- Direct Llama 3 API calls with no LangChain
- Full multi-turn conversation memory (system / user / assistant roles)
- Secure `.env` key management

### 2. LangChain Memory Chatbot (`phase-3-langchain-core/`)
Conversational chatbot built with LangChain primitives.
- `ChatPromptTemplate` + `ChatGroq` + LCEL pipe syntax
- `ConversationBufferMemory` for multi-turn context
- Clean separation of prompt, model, and output parsing

### 3. RAG PDF Chatbot *(Separate Repo)*
Production-grade RAG pipeline — the flagship project.
- Full pipeline: Load → Chunk → Embed → Store → Retrieve → Answer
- FastAPI REST service with `/upload` and `/ask` endpoints
- Containerised with Docker, deployed live on Railway
- LangSmith integrated for chain tracing and eval

🔗 [View Repo](https://github.com/MinahilFatima123/rag-pdf-chatbot) · [Live API Docs](https://rag-pdf-chatbot-production-e417.up.railway.app/docs)

---

## 📚 Resources Used

- [LangChain Docs](https://python.langchain.com)
- [DeepLearning.ai RAG Course](https://deeplearning.ai) (free)
- [LangSmith Docs](https://docs.smith.langchain.com)
- [FastAPI Docs](https://fastapi.tiangolo.com)
- [Groq API Docs](https://console.groq.com/docs)

---



[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com) ← *(add your link)*
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?logo=github)](https://github.com) ← *(add your link)*

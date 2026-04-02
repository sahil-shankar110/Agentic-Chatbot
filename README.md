# 🤖 Agentic AI Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.55%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1.2%2B-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A production-ready, full-stack Agentic AI Chatbot with real-time web search capability, powered by Groq (Llama 3.3) and Google Gemini — built with FastAPI, LangChain, and Streamlit.**

[🚀 Live Demo](https://agentic-chatbot-280p.onrender.com) · [📖 API Docs](https://agentic-chatbot-280p.onrender.com/docs) · [🐛 Report Bug](https://github.com/sahil-shankar110/Agentic-Chatbot/issues) · [✨ Request Feature](https://github.com/sahil-shankar110/Agentic-Chatbot/issues)

</div>

---

## 📋 Table of Contents

- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Running the Application](#running-the-application)
- [API Reference](#-api-reference)
- [Usage](#-usage)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🧠 About the Project

The **Agentic AI Chatbot** is a full-stack conversational AI application that goes beyond simple chat — it gives users the power to configure a custom AI agent on the fly, choosing from state-of-the-art large language models (LLMs), defining their own system prompts, and optionally enabling live web search to ground responses in real-time information.

The backend is a high-performance **FastAPI** REST API deployed on **Render**, while the frontend is an interactive **Streamlit** application that communicates with the backend over HTTP. The agent core is built with **LangChain** and supports two leading LLM providers — **Groq** (Llama 3.3 70B) and **Google Gemini** (2.5 Flash Lite) — with optional web search via **Tavily**.

---

## ✨ Key Features

- 🧩 **Dual LLM Provider Support** — Switch seamlessly between Groq's Llama 3.3 70B and Google's Gemini 2.5 Flash Lite
- 🌐 **Agentic Web Search** — Toggle Tavily-powered live web search to enrich responses with up-to-date information
- 🛠️ **Custom System Prompts** — Define your agent's persona, role, and behavior at runtime
- 💬 **Conversation History** — Sidebar that stores and displays the last 5 queries for quick reuse
- ⚡ **FastAPI Backend** — Blazing-fast, async-ready REST API with full Swagger/OpenAPI documentation
- 🎨 **Streamlit Frontend** — Clean, wide-layout UI with responsive controls and spinner feedback
- 🔒 **CORS-Enabled API** — Configured to accept requests from any origin for easy integration
- ☁️ **Cloud Deployed** — Backend live on Render with environment-based port binding
- 📦 **Modern Dependency Management** — Uses `uv` for fast, reproducible installs via `pyproject.toml` and `uv.lock`

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Agent Core** | LangChain, LangGraph | AI agent orchestration & tool use |
| **LLM — Option 1** | Groq (`llama-3.3-70b-versatile`) | Ultra-fast Llama 3.3 inference |
| **LLM — Option 2** | Google Gemini (`gemini-2.5-flash-lite`) | Lightweight Google Gemini model |
| **Web Search** | Tavily | Real-time web search for agents |
| **Backend API** | FastAPI + Uvicorn | High-performance Python REST API |
| **Frontend UI** | Streamlit | Rapid Python-based web UI |
| **Data Validation** | Pydantic v2 | Request/response schema validation |
| **Config Management** | python-dotenv | Secure environment variable loading |
| **Deployment** | Render | Cloud hosting for the API backend |
| **Package Manager** | uv | Fast Python package & project manager |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│                   USER BROWSER                  │
│                                                 │
│         ┌──────────────────────────┐            │
│         │   Streamlit Frontend     │            │
│         │     (frontend.py)        │            │
│         │                          │            │
│         │  • Model selector        │            │
│         │  • System prompt input   │            │
│         │  • Search toggle         │            │
│         │  • Query input           │            │
│         │  • Conversation history  │            │
│         └────────────┬─────────────┘            │
└──────────────────────┼──────────────────────────┘
                       │ HTTP POST /chat
                       │ (JSON payload)
                       ▼
┌──────────────────────────────────────────────────┐
│         FastAPI Backend (backend.py)             │
│              [Deployed on Render]                │
│                                                  │
│  POST /chat ──► RequestModel validation          │
│                      │                          │
│                      ▼                          │
│           get_agent_response()                   │
│                 (agent.py)                       │
│                      │                          │
│         ┌────────────┴───────────────┐          │
│         ▼                           ▼           │
│   ChatGroq (Llama)        ChatGoogleGenerativeAI │
│    + TavilySearch              + TavilySearch    │
│     (optional)                  (optional)       │
│         │                           │           │
│         └─────────────┬─────────────┘           │
│                       ▼                         │
│              LangChain Agent                    │
│           (create_agent + invoke)               │
│                       │                         │
│                  AI Response                    │
└──────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
Agentic-Chatbot/
│
├── agent.py            # 🧠 Core agent logic — LLM setup, tool binding, agent invocation
├── backend.py          # ⚡ FastAPI REST API — /chat endpoint, CORS, request validation
├── frontend.py         # 🎨 Streamlit UI — model selector, chat input, history sidebar
├── main.py             # 🚀 Application entry point
│
├── pyproject.toml      # 📦 Project metadata & dependencies (uv/pip compatible)
├── uv.lock             # 🔒 Locked dependency versions for reproducible builds
├── render.yaml         # ☁️  Render deployment configuration
├── .python-version     # 🐍 Python version pin (3.12+)
├── .gitignore          # 🙈 Git ignore rules
└── README.md           # 📖 Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed on your system:

- **Python 3.12+** — [Download here](https://www.python.org/downloads/)
- **uv** (recommended) — [Install uv](https://docs.astral.sh/uv/getting-started/installation/) or use `pip`
- **API Keys** for the following services:
  - [Groq API Key](https://console.groq.com/) — for Llama 3.3 models
  - [Google AI API Key](https://aistudio.google.com/app/apikey) — for Gemini models
  - [Tavily API Key](https://app.tavily.com/) — for web search capability

---

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/sahil-shankar110/Agentic-Chatbot.git
cd Agentic-Chatbot
```

**2. Install dependencies**

Using `uv` (recommended — faster and reproducible):

```bash
pip install uv
uv sync --frozen
```

Or using standard `pip`:

```bash
pip install -r requirements.txt
```

> **Note:** If you don't have a `requirements.txt`, export one from `pyproject.toml` with:
> ```bash
> uv pip compile pyproject.toml -o requirements.txt
> ```

---

### Environment Variables

Create a `.env` file in the root directory of the project:

```bash
touch .env
```

Add the following keys:

```env
# LLM Providers
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here

# Web Search
TAVILY_API_KEY=your_tavily_api_key_here
```

> ⚠️ **Never commit your `.env` file.** It is already included in `.gitignore`.

---

### Running the Application

The application consists of two separate services — the **backend API** and the **frontend UI**. You need to run both simultaneously (in separate terminals).

**Terminal 1 — Start the Backend API**

```bash
uvicorn backend:app --host 127.0.0.1 --port 8000 --reload
```

The API will be available at: `http://127.0.0.1:8000`
Interactive API docs (Swagger UI): `http://127.0.0.1:8000/docs`

**Terminal 2 — Start the Frontend UI**

```bash
streamlit run frontend.py
```

The Streamlit app will open automatically at: `http://localhost:8501`

> **Important:** If running locally, update the `URL_BACKEND` variable in `frontend.py` from the production Render URL to your local backend:
> ```python
> URL_BACKEND = "http://127.0.0.1:8000/chat"
> ```

---

## 📡 API Reference

### Base URL

```
Production: https://agentic-chatbot-280p.onrender.com
Local:      http://127.0.0.1:8000
```

---

### `GET /`

Health check — confirms the API is running.

**Response:**
```json
{
  "Status": "Welcome to the Agentic AI Chatbot API. Use the /chat endpoint to interact with the agent."
}
```

---

### `POST /chat`

Send a message to the AI agent and receive a response.

**Request Body:**

```json
{
  "model_name": "llama-3.3-70b-versatile",
  "model_provider": "llama",
  "system_prompt": "You are a helpful assistant that answers questions concisely.",
  "messages": ["What is the capital of France?"],
  "search_allow": false
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `model_name` | `string` | ✅ | One of the allowed model IDs (see below) |
| `model_provider` | `string` | ✅ | `"llama"` for Groq or `"gemini"` for Google |
| `system_prompt` | `string` | ✅ | Defines the agent's role and behavior |
| `messages` | `list[string]` | ✅ | List of user messages in the conversation |
| `search_allow` | `boolean` | ✅ | `true` to enable Tavily web search |

**Allowed Models:**

| `model_name` | `model_provider` | Provider |
|-------------|-----------------|---------|
| `llama-3.3-70b-versatile` | `llama` | Groq |
| `gemini-2.5-flash-lite` | `gemini` | Google |

**Success Response (200):**
```
"Paris is the capital of France."
```

**Error Response:**
```json
{
  "error": "Model not allowed"
}
```

---

## 💡 Usage

Once both services are running, open the Streamlit app in your browser and follow these steps:

1. **Define Your Agent** — Enter a system prompt in the top text area to set your agent's role (e.g., *"You are a Python expert. Answer all questions with code examples."*)

2. **Select a Model** — Choose between:
   - **Gemini** → `gemini-2.5-flash-lite`
   - **Llama** → `llama-3.3-70b-versatile`

3. **Enable Web Search** (optional) — Check *"Allow Search Capability"* to let the agent search the web via Tavily for real-time information.

4. **Enter Your Query** — Type your question in the query text area.

5. **Submit** — Click the **Search** button and wait for the agent's response.

6. **Conversation History** — Your last 5 queries are saved in the sidebar. Click any past query to instantly re-use it in a new request.

---

## ☁️ Deployment

This project is configured for one-click deployment to **Render** using the included `render.yaml`.

### Deploy to Render

1. Push your code to GitHub (already done ✅)
2. Go to [Render Dashboard](https://dashboard.render.com/) → **New** → **Web Service**
3. Connect your GitHub repository: `sahil-shankar110/Agentic-Chatbot`
4. Render will auto-detect the `render.yaml` configuration
5. Add the required environment variables in the Render dashboard:
   - `GROQ_API_KEY`
   - `TAVILY_API_KEY`
   - `GOOGLE_API_KEY` *(if using Gemini)*
6. Click **Deploy** — Render handles the build and startup automatically

**Render Build Command:**
```bash
pip install uv && uv sync --frozen && uv cache prune --ci
```

**Render Start Command:**
```bash
uvicorn backend:app --host 0.0.0.0 --port $PORT
```

> The backend auto-reads the `$PORT` environment variable provided by Render.

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. **Fork** the repository
2. **Create** your feature branch:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** your changes:
   ```bash
   git commit -m "feat: Add AmazingFeature"
   ```
4. **Push** to the branch:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open** a Pull Request

Please make sure your code follows clean, readable Python conventions and that all environment variables remain in `.env` (never committed).

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

## 📬 Contact

**Sahil Shankar**

- GitHub: [@sahil-shankar110](https://github.com/sahil-shankar110)
- Repository: [https://github.com/sahil-shankar110/Agentic-Chatbot](https://github.com/sahil-shankar110/Agentic-Chatbot)

---

<div align="center">

⭐ **If you found this project useful, please consider giving it a star!** ⭐

Made with ❤️ using Python, LangChain, FastAPI & Streamlit

</div>

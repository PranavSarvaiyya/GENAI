# 📧 OutreachAI — AI-Powered Cold Email Generator

OutreachAI is an intelligent cold email writing tool that generates **hyper-personalized, professional cold emails** in seconds. It uses **Mistral AI** (via LangChain) to craft emails that feel natural, mention recipient-specific details, and drive action — all through a clean **Streamlit** web interface.

---

## 🚀 What Does This Project Do?

You provide three simple inputs:

| Input | Description |
| :--- | :--- |
| **Recipient Profile** | Who are you emailing? (e.g., "Founder of an AI startup, recently raised Series A") |
| **Sender Information** | Who are you? (e.g., "AI/ML student with 3 GenAI projects") |
| **Goal** | What do you want? (e.g., "Get an internship interview") |

The AI then generates a **complete cold email** with:
- ✅ A compelling **subject line**
- ✅ A personalized **email body** (under 150 words)
- ✅ Natural tone — not spammy or fake

---

## 🧠 How Does It Work?

The project uses a modern **Generative AI pipeline** built with the following architecture:

```
User Input → LangChain Prompt Template → Mistral AI LLM → Pydantic Output Parser → Structured Email Output
```

### Step-by-step flow:

1. **User enters** recipient profile, sender info, and goal via the Streamlit UI.
2. **LangChain `ChatPromptTemplate`** formats the input into a structured system + user prompt.
3. **Mistral AI (`mistral-small-2506`)** receives the prompt and generates a cold email.
4. **`PydanticOutputParser`** parses the raw AI response into a clean structured format (`subject` + `body`).
5. **Streamlit** renders the output as an email preview card with a **copy-to-clipboard** button.

---

## 🛠️ Tech Stack — What Is Used & Why?

| Technology | What It Is | Why It Is Used |
| :--- | :--- | :--- |
| **[Mistral AI](https://mistral.ai/)** | Large Language Model (LLM) | Generates high-quality, natural cold emails. `mistral-small-2506` is fast, cheap, and great for structured outputs. |
| **[LangChain](https://www.langchain.com/)** | LLM Application Framework | Provides prompt templates, model wrappers, and output parsers to build a clean AI pipeline. |
| **[Pydantic](https://docs.pydantic.dev/)** | Data Validation Library | Ensures the AI output is parsed into a strict schema (`subject` + `body`) instead of raw text. |
| **[Streamlit](https://streamlit.io/)** | Python Web UI Framework | Builds an interactive web app with minimal code — perfect for AI demos and internal tools. |
| **[python-dotenv](https://pypi.org/project/python-dotenv/)** | Environment Variable Loader | Loads the `MISTRAL_API_KEY` securely from a `.env` file instead of hardcoding it. |
| **[st-copy-to-clipboard](https://pypi.org/project/st-copy-to-clipboard/)** | Streamlit Component | Adds a one-click "Copy Email" button so users can quickly copy the generated email. |

---

## 📁 Project Structure

```
OutreachAI/
├── main.py          # CLI version — generates cold emails via terminal input/output
├── app.py           # Streamlit UI version — interactive web interface
└── README.md        # Project documentation (this file)
```

| File | Description |
| :--- | :--- |
| `main.py` | The original command-line script. Takes input via `input()`, prints the generated email to the console. Good for quick testing. |
| `app.py` | The Streamlit web app. Has a left panel for inputs, right panel for output preview, copy button, and JSON view. Production-ready UI. |

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/PranavSarvaiyya/GENAI.git
cd GENAI
git checkout outreach-feature
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat

# Linux / macOS
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r reqirement.txt
pip install st-copy-to-clipboard
```

### 4. Set up environment variables

Create a `.env` file in the project root (`GenAI/`) with your Mistral API key:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

> 🔑 Get your free API key from [https://console.mistral.ai/](https://console.mistral.ai/)

### 5. Run the app

**Streamlit Web UI:**
```bash
cd OutreachAI
streamlit run app.py
```

**CLI Version:**
```bash
cd OutreachAI
python main.py
```

---

## 🖥️ App Features

- **Left-Right Layout** — Inputs on the left, email preview on the right
- **Email Preview Card** — Read-only styled card showing the generated email
- **📋 Copy Button** — One-click copy to clipboard
- **📄 JSON Tab** — View the raw structured output (subject + body)
- **Error Handling** — Shows raw AI response if parsing fails
- **Wide Layout** — Uses full screen width for better readability

---

## 🔧 Model Configuration

The Mistral model is configured with these parameters:

| Parameter | Value | Purpose |
| :--- | :--- | :--- |
| `model` | `mistral-small-2506` | Fast, cost-effective model optimized for instruction following |
| `temperature` | `0.4` | Low creativity — keeps emails professional and focused |
| `top_p` | `0.70` | Nucleus sampling — balances diversity with coherence |
| `max_completion_tokens` | `1000` | Limits response length to avoid overly long outputs |

---

## 📌 Key Concepts Used

- **Prompt Engineering** — System + User message pattern for guiding LLM behavior
- **Structured Output Parsing** — Using Pydantic schemas to extract clean data from LLM responses
- **LangChain LCEL** — LangChain Expression Language for chaining prompts and models
- **Environment Variable Management** — Secure API key handling with `.env` files

---

## 👤 Author

**Pranav Sarvaiyya**

- GitHub: [@PranavSarvaiyya](https://github.com/PranavSarvaiyya)

---

## 📄 License

This project is for educational and personal use.

# 🤖 Gemini 3.1 AI Chatbot

A high-performance chatbot interface built using **Python**, **Streamlit**, and **Google Gemini 3.1 Flash-Lite**.
This application provides a clean chat UI, fast responses, and persistent session memory for a smooth conversational experience.

---

# 🚀 Features

* **Gemini 3.1 Integration**
  Uses Google's `gemini-3.1-flash-lite-preview` model for fast AI responses.

* **Persistent Chat Memory**
  Streamlit `session_state` keeps conversation context.

* **Modern Chat Interface**
  Clean chat bubble layout with role-based formatting.

* **Secure API Handling**
  Uses `.env` file to protect API keys.

---

# 🛠️ Installation

## 1️⃣ Clone the Repository

```bash
https://github.com/kishanth29/portfolio-projects.git
cd gemini-chat-bot
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
.\venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install streamlit python-dotenv google-generativeai
```

Or install using requirements file:

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure API Key

Create a `.env` file in the project root.

```
GEMINI_API_KEY=your_actual_api_key_here
```

Get your API key from:
https://aistudio.google.com/app/apikey

---

# 💻 Running the Application

Run the Streamlit app using:

```bash
python -m streamlit run app.py
```

The application will open in your browser automatically.

---

# 📁 Project Structure

```
gemini-chat-bot
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── venv/
```

| File               | Description                |
| ------------------ | -------------------------- |
| `app.py`           | Main Streamlit application |
| `.env`             | Stores API key             |
| `requirements.txt` | Python dependencies        |
| `README.md`        | Project documentation      |

---

# 🔧 Troubleshooting

### ModuleNotFoundError

Make sure the **virtual environment is activated** before installing packages.

### API Error 404

Ensure you are using the correct model:

```
gemini-3.1-flash-lite-preview
```

### Blank Screen

Check the following:

* `.env` file exists
* API key is correct
* Streamlit installed properly

---

# 📌 Technologies Used

* Python
* Streamlit
* Google Gemini API
* python-dotenv

---

# 📜 License

This project is open-source and available under the **MIT License**.

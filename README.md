# Advisor Chatbot

Advisor Chatbot is an AI-powered assistant designed to help users with coding queries, project advice, and GitHub repository recommendations. It leverages Google Gemini for natural language understanding and Supabase for persistent chat history. The project consists of a React frontend and a Flask-based Python backend.

---

## Features

- **Conversational AI**: Uses Google Gemini 2.0 Flash for generating intelligent responses.
- **Persistent Memory**: Stores chat history and context per user using Supabase.
- **GitHub Integration**: Recommends repositories with good first issues based on programming language.
- **Embeddings**: Uses Gemini embeddings for semantic memory and context retrieval.
- **Modern UI**: Built with React and Vite for a fast, responsive user experience.
- **API Security**: Sensitive keys are managed via environment variables and not exposed in the codebase.

---

## Project Structure

```
Advisor_chatbot/
├── chatbot-backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── routes/
│   │   └── chat.py
│   └── services/
│       ├── gemini.py
│       ├── github_api.py
│       └── memory.py
├── chatbot-ui/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── index.css
│   │   └── App.css
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   └── README.md
└── README.md
```

---

## Prerequisites

- Node.js (v18+ recommended)
- Python 3.9+
- pip
- Git
- Supabase account (for database)
- Google Gemini API access
- GitHub personal access token

---

## Backend Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Mithun017/Advisor_CB.git
   cd Advisor_chatbot/chatbot-backend
   ```

2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Copy `.env.example` to `.env` and fill in your actual keys:

   ```env
   GEMINI_API_KEY=your_gemini_api_key
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   GITHUB_TOKEN=your_github_token
   ```

5. **Run the backend server**

   ```bash
   python app.py
   ```

   Backend will run on: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Frontend Setup

1. **Navigate to the frontend directory**

   ```bash
   cd ../chatbot-ui
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Start the development server**

   ```bash
   npm run dev
   ```

   Frontend will run on: [http://localhost:5173](http://localhost:5173)

---

## Environment Variables

### Backend (`chatbot-backend/.env`):

- `GEMINI_API_KEY` – Your Google Gemini API key  
- `SUPABASE_URL` – Your Supabase project URL  
- `SUPABASE_KEY` – Your Supabase service role key  
- `GITHUB_TOKEN` – Your GitHub personal access token  

### Frontend:

- No sensitive environment variables required by default.

---

## API Endpoints

### Chat

- **POST /chat**

  **Request:**
  ```json
  {
    "user_id": "string",
    "query": "string"
  }
  ```

  **Response:**
  ```json
  {
    "response": "string"
  }
  ```

### Chat History

- **GET /history?user_id=string**

  **Response:**
  ```json
  {
    "history": [
      { "query": "...", "response": "..." }
    ]
  }
  ```

- **DELETE /history?user_id=string**

  **Response:**
  ```json
  {
    "status": "cleared",
    "details": "..."
  }
  ```

---

## Usage

1. Start both backend and frontend servers.
2. Open the frontend in your browser.
3. Enter your query and interact with the chatbot.
4. View or clear your chat history as needed.

---

## Security

- Do NOT commit your `.env` file or real keys to version control.
- `.gitignore` is already configured to exclude sensitive files.

---

## Contributing

1. Fork the repo
2. Create a new branch:  
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit changes:  
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to GitHub:  
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request

---

## License

This project is licensed under the **MIT License**.

---

## Acknowledgements

- Google Gemini
- Supabase
- React
- Vite
- GitHub REST API

---

## Contact

For questions or support, please open an issue on the [GitHub repository](https://github.com/Mithun017/Advisor_CB).

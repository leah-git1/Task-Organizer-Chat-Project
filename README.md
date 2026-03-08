# TaskOrganizer

AI-powered task management chatbot with React frontend and FastAPI backend.

## Project Structure

```
TaskOrganizer/
├── client/          # React frontend
└── server/          # FastAPI backend
```

## Setup

### Backend

```bash
cd server
pip install -r requirements.txt
```

Create `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_key_here
```

Run server:
```bash
uvicorn main:app --reload
```

### Frontend

```bash
cd client
npm install
npm start
```

## Features

- AI chatbot for task organization
- Real-time chat interface
- RESTful API backend

## Tech Stack

- Frontend: React 19
- Backend: FastAPI, OpenAI
- HTTP Client: Axios

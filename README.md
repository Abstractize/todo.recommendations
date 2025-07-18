# TODO.Recommender-Service

This is the **Task Recommendation Microservice** for the TODO application. It provides basic, mock-based task suggestions to enhance user productivity and engagement.

---

## ⚙️ Tech Stack

- [Python 3.13+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/) — Web framework for building APIs
- [Uvicorn](https://www.uvicorn.org/) — ASGI server for running FastAPI
- [Pydantic](https://docs.pydantic.dev/) — Data validation

---

## 📁 Project Structure

```
todo_recommender/
├── app/
│   ├── api/                   # FastAPI endpoints
│   ├── core/                  # Settings and config
│   ├── models/                # Pydantic models
│   ├── services/              # Recommendation logic
│   └── main.py                # App entrypoint
├── tests/                     # Unit tests (optional)
├── Dockerfile                 # Docker image definition
├── requirements.txt           # Pip dependencies
└── README.md                  # Project documentation
```

---

## 🚀 Running Locally

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:  
📍 `http://localhost:8000`

---

## 🧪 Sample Endpoint

### `GET /recommendations`

Returns a mocked list of basic task recommendations.

**Query Parameters:**

- `user_id` (UUID) — required

```bash
curl "http://localhost:8000/recommendations?user_id=<uuid>"
```

---

## 🐳 Docker

Build and run with Docker:

```bash
docker build -t todo-recommender .
docker run -p 8000:8000 todo-recommender
```

---

## 🔒 Authentication

Currently no authentication is enforced. In future versions, JWT + Zero Trust integration is planned.

---

## 📝 License

MIT — see `LICENSE` file.
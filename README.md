# 💰 HisabKeep

HisabKeep is a backend API for managing personal expenses.

The project is being built as a practical backend-learning project to understand how a real API works from request → validation → database → response.

## 🚧 Project Status

**In Development**

Currently, the API includes basic expense management operations using FastAPI and PostgreSQL.

## 🎯 Goals

The main goal of HisabKeep is to learn and practice:

* REST API development
* FastAPI
* Pydantic validation
* SQLAlchemy ORM
* PostgreSQL
* CRUD operations
* HTTP status codes and error handling
* Database relationships
* Authentication and authorization
* API testing
* Clean backend architecture

## 🛠️ Tech Stack

* **Python**
* **FastAPI**
* **Pydantic**
* **SQLAlchemy**
* **PostgreSQL**
* **Uvicorn**

## 📌 Current Features

### Expense Management

* Create an expense
* View an expense by ID
* Update an expense
* Delete an expense
* Handle non-existent expenses with `404 Not Found`

## 📂 Project Structure

```text
HisabKeep/
│
├── src/
│   ├── models/
│   ├── schemas/
│   ├── routers/
│   ├── database/
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔄 API Flow

HisabKeep follows a simple backend flow:

```text
Client
  ↓
FastAPI Route
  ↓
Pydantic Schema
  ↓
SQLAlchemy
  ↓
PostgreSQL
  ↓
Response
```

## 🚀 Running Locally

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd HisabKeep
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file and add your PostgreSQL database configuration.

Example:

```env
DATABASE_URL=your_database_url
```

### 5. Run the API

```bash
uvicorn src.main:app --reload
```

## 🧪 Testing

The API can currently be tested using FastAPI's interactive Swagger documentation.

Future development will include automated tests for:

* Successful requests
* Validation errors
* Missing resources
* Database operations
* Authentication and authorization

## 🗺️ Roadmap

* [x] FastAPI project setup
* [x] PostgreSQL connection
* [x] SQLAlchemy models
* [x] Pydantic schemas
* [x] Create expense
* [x] Read expense
* [x] Update expense
* [x] Delete expense
* [ ] Input validation improvements
* [ ] Pagination
* [ ] Expense filtering
* [ ] User authentication
* [ ] Authorization
* [ ] Automated testing
* [ ] API documentation improvements
* [ ] Deployment

## 📚 What I'm Learning

HisabKeep is not just a CRUD project. I am using it to understand the fundamentals behind backend development rather than simply generating code with AI.

The project is being developed incrementally, with each feature used to understand the underlying concepts before moving to the next one.

## 📄 License

This project is currently for learning and development purposes.

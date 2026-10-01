# 💰 HisabKeep

# Expense Management REST API

# Python • FastAPI • PostgreSQL • SQLAlchemy • JWT Authentication • Pytest

## 1. Problem Statement

HisabKeep is a backend REST API for personal expense management. It provides authenticated users with a secure way to create, view, update, and delete their own expense records. The project focuses on building a clean, maintainable backend with authentication, authorization, validation, database persistence, and automated testing.

## 2. 🚧 Architecture

The application follows a layered backend architecture:

- Client → FastAPI API → Service/Business Logic → SQLAlchemy → PostgreSQL

- Authentication → JWT access token → protected API endpoints

- Automated tests → isolated test database/session overrides → API verification

## 3. ⚙️ Tech Stack

- Python — primary programming language

- FastAPI — REST API framework

- PostgreSQL — relational database

- SQLAlchemy — ORM and database interaction

- Pydantic — request/response validation and schemas

- JWT — stateless access-token authentication

- Pytest — automated testing

- Git & GitHub — version control and project history

## 4. ✨ Key Features

- User registration

- Password hashing and password verification

- User login with JWT access tokens

- Protected API endpoints

- User-specific expense authorization

- Create, read, update, and delete expenses

- Request and response validation with Pydantic

- Pagination for expense listing

- HTTP Exception handling for missing resources

- Automated API and authorization tests

## 5. 🔑 Security & Authorization

HisabKeep does not treat authentication as sufficient authorization. After a user is authenticated, expense queries and modifications are scoped to the authenticated user's identity. This prevents one account from reading or modifying another user's expense records.

Passwords are stored as hashes rather than plaintext values, and JWT access tokens are used to protect authenticated endpoints.

## 6. 🧮 Validation & Error Handling

- Pydantic schemas validate incoming request data and outgoing responses.

- Invalid or missing resources return appropriate HTTP errors.

- Protected endpoints reject unauthenticated requests.

- Authorization checks prevent cross-user access to expense data.

- Database operations are handled through the application's database session.

## 7. 🔥 Testing

The project includes automated tests covering the main authentication, expense, validation, and authorization flows. Tests use a controlled database/session setup so test data does not need to be written to the production database.

- User registration

- User login and authentication

- Protected endpoints

- Expense creation

- Expense retrieval

- Expense update

- Expense deletion

- Invalid/non-existent expense IDs

- User isolation — one user cannot access another user's expenses

## 8. 💻 Running Locally

Clone the repository and create a virtual environment:

```bash
git clone <YOUR_REPOSITORY_URL>
cd HisabKeep
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure the required environment variables in a local .env file, including the PostgreSQL connection details and JWT configuration.

- see the file .env.example which has database connection details and JWT configuration.

Start the development server:

```bash
uvicorn src.main:app --reload
```

Once running, the interactive API documentation is available through FastAPI's Swagger UI at /docs.

## 9. 🚀 Running Tests

Run the complete test suite with:

```bash
pytest
```

- conftest_example.py file add your credential of database and than run test.

- Tests should use the project's test database/session configuration rather than the main application database.

## 10. 🏗️ Design Decisions

- PostgreSQL was selected for reliable relational data storage and strong SQL support.

- SQLAlchemy provides a clear ORM layer between application code and PostgreSQL.

- Pydantic schemas keep API contracts separate from database models.

- JWT authentication provides a stateless mechanism for protecting API endpoints.

- User ownership checks are enforced at the backend rather than relying on the client.

- Automated tests were added before considering the backend complete.

## 11. 🧠 Challenges & Lessons Learned

- Understanding the difference between authentication and authorization.

- Ensuring that authenticated users can access only their own records.

- Handling update operations correctly instead of accidentally creating new records.

- Designing test database/session overrides so tests remain isolated from real data.

- Using validation and explicit HTTP errors to make API behavior predictable.

- Refactoring code after the initial CRUD implementation to improve maintainability.

## 12. 🎯 Future Improvements

- Containerize the application with Docker.

- Run FastAPI and PostgreSQL with Docker Compose.

- Add production deployment and environment-specific configuration.

- Build a web frontend and integrate it with the API.

- Add refresh-token/session management if the application requires longer-lived authentication.

- Add more advanced filtering, sorting, and reporting for expenses.

- Add CI checks to automatically run tests on every push or pull request.

## 13. Project Status

The core backend is implemented and tested. Authentication, authorization, expense CRUD operations, validation, and automated tests are in place. The next engineering phase is containerization, deployment, and frontend integration.

## 📜 License

Copyright (c) 2026 Sohail Ahmad. All rights reserved.

This repository is publicly available for viewing and educational/
portfolio purposes. No permission is granted to copy, modify,
distribute, sublicense, or use this software or substantial portions
of it for other projects without prior written permission from the
copyright holder.

For permission to use this project, please contact the author.

## 14. ✒️ Author

Sohail Ahmad

GitHub: (https://github.com/thesohailahmad)

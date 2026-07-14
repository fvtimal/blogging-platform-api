# 📝 Blogging Platform API

A RESTful Blogging Platform API built with **FastAPI** and **MongoDB**. The project provides secure user authentication using JWT, complete CRUD operations for blog posts, a comment system, category and tag management, search functionality, pagination, and interactive API documentation through Swagger UI.

---

## 🚀 Features

* User Registration & Login with JWT Authentication
* Secure Password Hashing using Bcrypt
* CRUD Operations for Blog Posts
* Comment System
* Category Management
* Tag Management
* Search Posts by Title and Content
* Pagination for Posts
* Protected Routes using JWT
* Automatic Swagger/OpenAPI Documentation
* MongoDB Database Integration

---

## 🛠️ Tech Stack

* Python 3
* FastAPI
* MongoDB
* Motor (Async MongoDB Driver)
* Pydantic
* JWT (python-jose)
* Passlib (Bcrypt)
* Uvicorn
* Docker
* Pytest

---

## 📁 Project Structure

```text
blogging-platform/
│
├── routers/
│   ├── users.py
│   ├── posts.py
│   ├── comments.py
│   ├── categories.py
│   └── tags.py
│
├── auth.py
├── database.py
├── dependencies.py
├── schemas.py
├── utils.py
├── main.py
│
├── tests/
│   ├── test_users.py
│   ├── test_posts.py
│   └── test_comments.py
│
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/blogging-platform.git
cd blogging-platform
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=blogging_db

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## ▶️ Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Application:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```
http://127.0.0.1:8000/redoc
```

---

## 📌 API Endpoints

### Authentication

| Method | Endpoint          | Description                 |
| ------ | ----------------- | --------------------------- |
| POST   | `/users/register` | Register a new user         |
| POST   | `/users/login`    | Login and receive JWT token |

---

### Blog Posts

| Method | Endpoint                  | Description                         |
| ------ | ------------------------- | ----------------------------------- |
| POST   | `/posts`                  | Create a post                       |
| GET    | `/posts`                  | Get all posts (supports pagination) |
| GET    | `/posts/{post_id}`        | Get a single post                   |
| PUT    | `/posts/{post_id}`        | Update a post                       |
| DELETE | `/posts/{post_id}`        | Delete a post                       |
| GET    | `/posts/search?q=keyword` | Search posts                        |

---

### Comments

| Method | Endpoint                   | Description             |
| ------ | -------------------------- | ----------------------- |
| POST   | `/comments`                | Create a comment        |
| GET    | `/comments/post/{post_id}` | Get comments for a post |
| PUT    | `/comments/{comment_id}`   | Update a comment        |
| DELETE | `/comments/{comment_id}`   | Delete a comment        |

---

### Categories

| Method | Endpoint      | Description        |
| ------ | ------------- | ------------------ |
| POST   | `/categories` | Create a category  |
| GET    | `/categories` | Get all categories |

---

### Tags

| Method | Endpoint | Description  |
| ------ | -------- | ------------ |
| POST   | `/tags`  | Create a tag |
| GET    | `/tags`  | Get all tags |

---

## 🔒 Authentication

Protected endpoints require a JWT access token.

Include the token in the request header:

```http
Authorization: Bearer <your_access_token>
```

---

## 🔍 Search

Search blog posts by title or content.

Example:

```
GET /posts/search?q=fastapi
```

---

## 📄 Pagination

Retrieve posts page by page.

Example:

```
GET /posts?page=1&limit=10
```

Response:

```json
{
  "page": 1,
  "limit": 10,
  "posts": [
    ...
  ]
}
```

---

## 🧪 Running Tests

Run all tests:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

---

## 🐳 Docker

Build the Docker image:

```bash
docker build -t blogging-api .
```

Run the container:

```bash
docker run -p 8000:8000 blogging-api
```

---

## 📚 Key Concepts Implemented

* RESTful API Design
* JWT Authentication
* Password Hashing
* FastAPI Dependency Injection
* MongoDB Relationships using ObjectId
* CRUD Operations
* Input Validation with Pydantic
* Authorization
* Pagination
* Search using MongoDB Regex
* Cascade Deletion of Comments
* Docker Containerization
* API Testing with Pytest

---

## 🚀 Future Improvements

* User Roles (Admin/User)
* Image Uploads
* Like & Reaction System
* Bookmark Posts
* Rich Text Editor Support
* MongoDB Text Index Search
* CI/CD Pipeline
* Cloud Deployment (Render, Railway, Azure, AWS)

---

## 👨‍💻 Author

Developed as a backend learning project using **FastAPI** and **MongoDB** to demonstrate modern REST API development practices including authentication, authorization, CRUD operations, search, pagination, testing, and Docker deployment.

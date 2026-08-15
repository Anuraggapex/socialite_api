# socialite-api

A high-performance, asynchronous REST API designed to power modern, scalable social networking applications. Built using **FastAPI** and architected for high throughput, robust security, and reliable data persistence.

## 🚀 Key Features

* **Asynchronous Architecture:** Leverages Python’s `async/await` ecosystem for non-blocking I/O operations and optimized database connections.
* **Granular Authentication:** Secure user registration and login flows protected by OAuth2 with JWT (JSON Web Tokens) bearer authentication.
* **Relational Data Modeling:** Implements full CRUD operations for Users, Posts, and Votes (Likes) using SQLAlchemy ORM.
* **Auto-Generated Documentation:** Interactive API exploration and testing available out-of-the-box via Swagger UI and ReDoc.
* **Strict Data Validation:** Utilizes Pydantic schemas to enforce data type safety, sanitisation, and explicit request/response schemas.

## 🛠️ Tech Stack

* **Framework:** FastAPI
* **Database ORM:** SQLAlchemy
* **Data Validation:** Pydantic v2
* **Security:** Passlib (Bcrypt hashing), PyJWT
* **Server:** Uvicorn

## 🛠️ Local Setup Guide

Follow these steps to run the API locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com
cd socialite_api
```

### 2. Set Up a Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
uvicorn main:app --reload
```
The server will start at `http://127.0.0.1:8000`.

## 📖 API Documentation

Once the server is running, you can explore, test, and view the fully interactive API documentation at:
* **Swagger UI:** `http://127.0.0`
* **ReDoc:** `http://127.0.0`

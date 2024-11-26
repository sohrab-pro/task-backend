# Django Task Management API

A robust RESTful API built with Django REST Framework that enables users to manage their tasks efficiently. The system provides secure authentication and comprehensive task management capabilities.

## Features

-   User Authentication (Login/Signup) with Token-based security
-   Complete CRUD operations for tasks
-   User-specific task isolation
-   Automatic task creation timestamp tracking
-   Ordered task listing (newest first)

## Prerequisites

-   Python 3.8+
-   Django 3.2+
-   Django REST Framework

## Installation

1. Clone the repository:

```bash
git clone https://github.com/sohrab-pro/task-backend.git
cd task-backend
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

## API Documentation

### Authentication Endpoints

#### Sign Up

-   **URL:** `/api/signup/`
-   **Method:** `POST`
-   **Data Params:**
    ```json
    {
    	"username": "string",
    	"email": "string",
    	"password": "string"
    }
    ```
-   **Success Response:**
    -   Code: 201
    -   Content: `{"message": "User created successfully!", "token": "your-auth-token"}`
-   **Error Response:**
    -   Code: 400
    -   Content:
        ```json
        {
          "error": "Username already exists!" |
                   "Email already exists!" |
                   "Password should be at least 8 characters long!"
        }
        ```

#### Login

-   **URL:** `/api/login/`
-   **Method:** `POST`
-   **Data Params:**
    ```json
    {
    	"username": "string",
    	"password": "string"
    }
    ```
-   **Success Response:**
    -   Code: 200
    -   Content: `{"message": "Logged in Successfully!", "token": "your-auth-token"}`
-   **Error Response:**
    -   Code: 401
    -   Content: `{"error": "Invalid credentials"}`

### Task Endpoints

All task endpoints require authentication. Include the token in the header:

```
Authorization: Token your-auth-token
```

#### List Tasks

-   **URL:** `/api/tasks/`
-   **Method:** `GET`
-   **Success Response:**
    -   Code: 200
    -   Content: Array of task objects

#### Create Task

-   **URL:** `/api/tasks/`
-   **Method:** `POST`
-   **Data Params:**
    ```json
    {
    	"title": "string",
    	"description": "string",
    	"status": "string"
    }
    ```
-   **Success Response:**
    -   Code: 201
    -   Content: Created task object

#### Retrieve Task

-   **URL:** `/api/tasks/{id}/`
-   **Method:** `GET`
-   **Success Response:**
    -   Code: 200
    -   Content: Task object

#### Update Task

-   **URL:** `/api/tasks/{id}/`
-   **Method:** `PUT`
-   **Data Params:**
    ```json
    {
    	"title": "string",
    	"description": "string",
    	"status": "string"
    }
    ```
-   **Success Response:**
    -   Code: 200
    -   Content: Updated task object

#### Delete Task

-   **URL:** `/api/tasks/{id}/`
-   **Method:** `DELETE`
-   **Success Response:**
    -   Code: 204
    -   Content: `{"status": "success", "message": "Task deleted successfully!"}`

## Security Features

-   Token-based authentication using Django REST Framework's TokenAuthentication
-   Password length validation (minimum 8 characters)
-   User-specific task isolation
-   Prevention of duplicate usernames and emails
-   Authentication required for all task operations

## Error Handling

The API includes comprehensive error handling for:

-   Invalid credentials
-   Duplicate user registration attempts
-   Invalid task operations
-   Authentication failures

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

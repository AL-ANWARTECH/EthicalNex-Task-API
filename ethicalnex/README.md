
Task Management API
Overview
The Task Management API helps users efficiently manage their tasks. It provides functionality to create, update, delete, and organize tasks. Ideal for to-do lists or productivity tools, this API is secured with JWT authentication and deployed on PythonAnywhere.

Features
User Authentication: Secure login with JWT (JSON Web Token).

Task Management: Create, update, delete, and view tasks with due dates and status.

Task Filtering: Filter tasks by completion status or due date.

API Documentation: Available via Swagger or DRF Docs.

Deployment: Hosted on PythonAnywhere.

Project Structure

/task_management_api
│── manage.py             # Django management script
│── README.md             # Project documentation
│── requirements.txt      # List of dependencies
│── users/                # User authentication app
│── tasks/                # Task management app
│── my_project/           # Main Django settings
│── ...
Database Model

from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
API Endpoints
Method	Endpoint	Purpose
POST	/register/	Register a new user
POST	/login/	Authenticate and get a JWT token
GET	/tasks/	Retrieve all tasks
POST	/tasks/	Create a new task
GET	/tasks/{id}/	Retrieve a specific task
PUT	/tasks/{id}/	Update an existing task
PATCH	/tasks/{id}/complete/	Mark task as complete or incomplete
DELETE	/tasks/{id}/	Delete a task
Database Configuration (MySQL)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Ethicalnex_db',
        'USER': 'root',
        'PASSWORD': 'My_Password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Project Timeline (5 Weeks)
Week	Task Summary
Week 1	Set up Django, MySQL, and authentication
Week 2	Define models and implement authentication
Week 3	Build API endpoints and CRUD functionality
Week 4	Add filtering, documentation, and testing
Week 5	Deploy and finalize the project
Deployment (PythonAnywhere)
Prepare the application:

Set DEBUG = False in settings.py.

Add PythonAnywhere domain to ALLOWED_HOSTS.

Collect static files using python manage.py collectstatic.

Set up PythonAnywhere:

Create a virtual environment and install dependencies.

Configure WSGI and project settings.

Upload the code:

Clone the repository or upload manually.

Configure static and media files:

Set up static and media URL paths.

Monitor and debug:

Use PythonAnywhere's error logs for troubleshooting.

Testing with Postman
To test the Task Management API using Postman, follow the steps below:

1. Register a New User
Request Type: POST

Endpoint: /register/

Body (JSON):


{
    "username": "testuser",
    "password": "password123"
}
2. Login to Get JWT Token
Request Type: POST

Endpoint: /login/

Body (JSON):


{
    "username": "testuser",
    "password": "password123"
}
Response (Example):


{
    "access": "your_jwt_token"
}
Copy the access token from the response. You will use this token for authenticated requests.

3. Create a New Task
Request Type: POST

Endpoint: /tasks/

Headers:

Authorization: Bearer <your_jwt_token>

Body (JSON):


{
    "title": "New Task",
    "description": "Description for new task",
    "completed": false,
    "due_date": "2025-04-12T12:00:00Z"
}
Response (Example):


{
    "id": 1,
    "user": 1,
    "title": "New Task",
    "description": "Description for new task",
    "completed": false,
    "due_date": "2025-04-12T12:00:00Z",
    "created_at": "2025-04-06T10:00:00Z",
    "updated_at": "2025-04-06T10:00:00Z"
}
4. Get All Tasks
Request Type: GET

Endpoint: /tasks/

Headers:

Authorization: Bearer <your_jwt_token>

Response (Example):


[
    {
        "id": 1,
        "user": 1,
        "title": "New Task",
        "description": "Description for new task",
        "completed": false,
        "due_date": "2025-04-12T12:00:00Z",
        "created_at": "2025-04-06T10:00:00Z",
        "updated_at": "2025-04-06T10:00:00Z"
    }
]
5. Update a Task
Request Type: PUT

Endpoint: /tasks/{id}/

Headers:

Authorization: Bearer <your_jwt_token>

Body (JSON):


{
    "title": "Updated Task",
    "completed": true
}
Response (Example):


{
    "id": 1,
    "user": 1,
    "title": "Updated Task",
    "description": "Description for new task",
    "completed": true,
    "due_date": "2025-04-12T12:00:00Z",
    "created_at": "2025-04-06T10:00:00Z",
    "updated_at": "2025-04-06T10:15:00Z"
}
6. Delete a Task
Request Type: DELETE

Endpoint: /tasks/{id}/

Headers:

Authorization: Bearer <your_jwt_token>

Response (Example):


{
    "message": "Task deleted successfully"
}
7. Filter Tasks by Completion Status
Request Type: GET

Endpoint: /tasks/?completed=true

Headers:

Authorization: Bearer <your_jwt_token>

Response (Example):


[
    {
        "id": 2,
        "user": 1,
        "title": "Completed Task",
        "description": "Task is completed",
        "completed": true,
        "due_date": "2025-04-10T12:00:00Z",
        "created_at": "2025-04-05T09:00:00Z",
        "updated_at": "2025-04-05T09:15:00Z"
    }
]
Tests
You can test the API using the above steps in Postman, and these requests will help verify that the system is working as expected.

Additional Notes
Security: Uses JWT for user authentication (djangorestframework-simplejwt).

API Documentation: Available through Swagger or DRF Docs.

Hosting: Deployed on PythonAnywhere.
https://alanwartech.pythonanywhere.com/

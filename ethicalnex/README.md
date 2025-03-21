# Task Management API

## Overview
This API is designed to help users manage their tasks efficiently. It allows users to create, update, delete, and organize tasks, making it ideal for to-do lists and productivity tools.

## Features
- **User Authentication** – Users can register, log in, and use JWT for secure access.
- **Task Management** – Users can add, update, delete, and view their tasks.
- **Task Status Updates** – Tasks can be marked as complete or incomplete.
- **Task Filtering** – Users can filter tasks by due date or completion status.
- **Timestamps** – Each task has automatic timestamps for creation and updates.
- **API Documentation** – Built with Swagger or DRF Docs for easy reference.
- **Deployment** – The API will be hosted on Heroku or PythonAnywhere.

## Project Structure
```
/task_management_api
│── manage.py
│── README.md
│── requirements.txt
│── users/  # Handles authentication
│── tasks/  # Manages tasks
│── my_project/  # Main Django settings
│── ...
```

## Database Model
```python
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

## API Endpoints

 Method  Endpoint                 Purpose                              
 POST    `/register/`             Register a new user                 
 POST    `/login/`                Authenticate and get a JWT token    
 GET     `/tasks/`                Retrieve all tasks                  
 POST    `/tasks/`                Create a new task                   
 GET     `/tasks/{id}/`           Retrieve a specific task            
 PUT     `/tasks/{id}/`           Update an existing task             
 PATCH   `/tasks/{id}/complete/`  Change task status (complete/incomplete) 
 DELETE  `/tasks/{id}/`           Delete a task                       

## Database Configuration (MySQL)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'anwar',
        'USER': 'root',
        'PASSWORD': 'My_Password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## Project Timeline (5 Weeks)

 Week   Task Summary 
 Week 1  Set up Django, MySQL, and authentication   
 Week 2  Define models and implement authentication 
 Week 3  Build API endpoints and CRUD functionality 
 Week 4  Add filtering, documentation, and testing  
 Week 5  Deploy and finalize the project           

### Week 1 Objectives
✔️ Install Django, Django REST Framework, and MySQL  
✔️ Create authentication and task management apps  
✔️ Implement JWT-based authentication  
✔️ Set up Git for version control  
✔️ Test the API setup  
✔️ Research best practices for structuring models and serializers  

## Additional Notes
- **Security** – JWT (djangorestframework-simplejwt) for authentication.
- **API Documentation** – Available via Swagger or DRF Docs.
- **Hosting** – The API will be deployed on Heroku or PythonAnywhere.

This README will guide me through the project. 🚀


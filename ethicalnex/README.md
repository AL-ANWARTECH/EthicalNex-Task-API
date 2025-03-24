# Task Management API

## Overview
This API helps users manage their tasks efficiently. It allows users to create, update, delete, and organize tasks, making it ideal for to-do lists and productivity tools.

## Features
- **User Authentication** – Users can register, log in, and use JWT for secure access.
- **Task Management** – Users can add, update, delete, and view their tasks.
- **Task Status Updates** – Tasks can be marked as complete or incomplete.
- **Task Filtering** – Users can filter tasks by due date or completion status.
- **Timestamps** – Each task has automatic timestamps for creation and updates.
- **API Documentation** – Built with Swagger or DRF Docs for easy reference.
- **Deployment** – The API will be hosted on **Heroku** or **PythonAnywhere**.

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
    updated_at = models.DateTimeField(auto_now=True)
```

## API Endpoints

 Method  | Endpoint                 | Purpose                              
---------|--------------------------|--------------------------------------
 POST    | `/register/`             | Register a new user                 
 POST    | `/login/`                | Authenticate and get a JWT token    
 GET     | `/tasks/`                | Retrieve all tasks                  
 POST    | `/tasks/`                | Create a new task                   
 GET     | `/tasks/{id}/`            Retrieve a specific task            
 PUT     | `/tasks/{id}/`            Update an existing task             
 PATCH   | `/tasks/{id}/complete/`   Change task status (complete/incomplete) 
 DELETE  | `/tasks/{id}/`            Delete a task                       

## Database Configuration (MySQL)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ANWAR',
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

### Week 1 Accomplishments
✔️ Installed Django, Django REST Framework, and MySQL  
✔️ Created authentication and task management apps  
✔️ Implemented JWT-based authentication  
✔️ Set up Git for version control  
✔️ Tested the API setup  
✔️ Researched best practices for structuring models and serializers  

## Challenges Faced & Solutions
- **Understanding Django Documentation**: Initially found it difficult to navigate.
  - **Solution**: Used external resources like YouTube, DRF documentation, and community forums.
- **Database Connectivity Issues**: Encountered MySQL configuration errors.
  - **Solution**: Adjusted MySQL settings, ensured the correct database URL, and resolved authentication errors.
- **JWT Authentication Complexity**: Implementation was challenging.
  - **Solution**: Followed official DRF SimpleJWT documentation and tested step by step.
- **Task Filtering Logic**: Had trouble with dynamic filtering.
  - **Solution**: Used DRF filters and Django ORM queries to refine filtering.
- **CRUD Functionality Bugs**: Faced issues with updating and deleting tasks.
  - **Solution**: Debugged serializers and views to ensure proper data handling.

## Additional Notes
- **Security** – JWT (djangorestframework-simplejwt) for authentication.
- **API Documentation** – Available via Swagger or DRF Docs.
- **Hosting** – The API will be deployed on **Heroku** or **PythonAnywhere**.

This README will guide me through the project. 🚀


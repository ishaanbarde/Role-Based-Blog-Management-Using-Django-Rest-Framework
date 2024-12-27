#Role-Based-Blog-Management-Using-Django-REST-Framework

This project is a simple Django-based web application for managing articles with Role-Based Access Control (RBAC). It includes functionality for creating, updating, deleting, and listing articles, as well as managing user roles (Owner, Admin, and Member).

## Features

- **Role-Based Access Control**: Users can have different roles: Owner, Admin, and Member.
- **Article Management**: Admins can create, update, delete, and view articles.
- **User Management**: Owners can create new Admin and Member users and manage roles.
- **Comment System**: Authenticated users can add comments to articles.

## Technologies Used

- Python 3.8+
- Django 4.x
- Django Rest Framework (DRF)
- SQLite (for development)
- Git for version control
- Docker (optional for containerization)

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone https://github.com/ishaanbarde/Django-Article-Management-With-RBAC.git
cd Django-Article-Management-With-RBAC
```

## API Endpoints

### Authentication Endpoints
- `POST /api/register/`: Register a new user.
- `POST /api/login/`: User login.

### User Management (Owner and Admin only)
- `POST /api/owner/createUser/`: Create a new user (Admin or Member) (Owner only).
- `GET /api/userlist/`: List all users (Admin only).
- `POST /api/owner/<int:user_id>/updateRole/`: Update the role of a user (Owner only).

### Article Management (Admin and Owner only)
- `POST /api/create/`: Create a new article (Admin only).
- `GET /api/<int:article_id>/`: View an article.
- `PUT /api/<int:article_id>/update/`: Update an article (Admin only).
- `DELETE /api/<int:article_id>/delete/`: Delete an article (Admin only).

### Comment Management (Authenticated users)
- `POST /api/comments/<int:article_id>/add/`: Add a comment to an article (Authenticated users only).
- `GET /api/comments/<int:article_id>/`: List all comments on an article.

## Running Tests

To run the tests for the application, use the following command:

```bash
python manage.py test
```

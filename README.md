# Article-Management-With-RBAC-Using-REST-Framework

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

# RBAC
This is a Role Based Access Control System

# VRV Security RBAC System

This project implements a Role-Based Access Control (RBAC) system for a security platform, VRV Security. The system is built using Flask and utilizes JWT (JSON Web Tokens) for secure user authentication and authorization. The application allows users to register, log in, and access resources based on their assigned role (User, Moderator, Admin).

## Features

- **User Registration and Login**: Allows users to register and log in using their credentials.
- **Role-Based Access Control (RBAC)**: Supports multiple roles (`user`, `moderator`, `admin`) with different levels of access to resources.
- **JWT Authentication**: Secure login and token-based authorization using JWT.
- **User Profile**: Each user has a profile that they can access after logging in.
- **Admin Dashboard**: Only accessible by users with an admin role, providing access to system management features.
- **Moderator Dashboard**: Only accessible by users with an admin role or Moderator role, providing access relevent features.
- **Logout**: Users can log out, which invalidates their current session.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **Flask-SQLAlchemy**: A Flask extension for working with SQL databases.
- **JWT (JSON Web Tokens)**: Used for securing API endpoints and handling user authentication.
- **Werkzeug**: A comprehensive WSGI web application library for password hashing.
- **Flask-JWT-Extended**: An extension that simplifies JWT handling in Flask.
- **Python 3.x**: The programming language used for the backend logic.

## Installation

### Prerequisites

1. Install **Python 3.x** and **pip** (Python's package installer).
2. Clone the repository:

    ```bash
    git clone https://github.com/Sak21sin/RBAC.git
    cd RBAC
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Set up the database (using Flask-Migrate or manually):

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

### Configuration

The project uses a configuration file (`config.py`) to manage application settings such as the secret key for JWT.

Make sure to set the following environment variables:

- `FLASK_APP=app.py`
- `FLASK_ENV=development`
- `SECRET_KEY=your_secret_key` 

## Usage

### Running the Application

To start the Flask application, use the following command:

```bash
python app.py

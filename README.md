# Little Lemon - A Django REST Framework Project (Meta Back-End Developer Certification Capstone Project)

**Little Lemon** is a sample restaurant reservation and menu management system, demonstrating best practices with **Django**, **Django REST Framework**, **Token Authentication**, and **Djoser** for user authentication. This project is part of the **Meta Back-End Developer Certification Program (Coursera)**, showcasing how to build a secure, scalable back-end for a fictional restaurant.

---

## Key Features

1. **Reservations & Bookings**  
   - Create, view, and manage bookings using a Django `Booking` model (`reservation_date`, `name`, `num_guests`, etc.).  
   - Supports real-time reservation checks to avoid booking conflicts.

2. **Menu Management**  
   - Maintain a list of menu items (`title`, `price`, `inventory`), with both **HTML page rendering** and **RESTful API** endpoints.  
   - Users can add new menu items via an API POST request or view existing items from a browser.

3. **API Authentication**  
   - Integrated **Django REST Framework** & **Token Authentication** for secure endpoints.  
   - **Djoser** provides a convenient way to create and manage user accounts (`api-token-auth/` endpoints).

4. **Throttling & Permissions**  
   - DRF’s built-in throttles limit requests from anonymous and authenticated users.  
   - Certain endpoints require user authentication (e.g., to create new menu items).

5. **Front-End Templates**  
   - Basic HTML templates (`base.html`, `index.html`, `menu.html`, etc.) using **Django Templates**.  
   - AJAX-based booking form (`book.html`) to dynamically fetch and post reservation data.

---

## Tech Stack

- **Django 5.0+**: Core framework for routing, templating, and ORM.  
- **Django REST Framework**: RESTful API creation and token-based authentication.  
- **SQLite** (default) or **MySQL** (configurable): Database storing bookings, menu items, and user data.  
- **Djoser**: Simplifies authentication endpoints (login, logout, token generation).  
- **HTML/CSS/JavaScript**: Simple front-end templates for demonstration.  
- **Python 3.12** (or above).

---

## Setup Instructions

    Clone the Repository
```bash
git clone https://github.com/<user>/littlelemon.git
cd littlelemon
```
## Create & Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# Windows: .venv\Scripts\activate
```
## Install Dependencies

pip install -r requirements.txt

(Alternatively, use pip install django djangorestframework djoser mysqlclient ... if no requirements.txt is provided.)

Configure the Database

    By default, the project uses db.sqlite3.
    For MySQL or Postgres, update DATABASES in littlelemon/settings.py.

Run Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```
Create a Superuser
```bash
python3 manage.py createsuperuser
```
Start the Development Server
```bash
    python3 manage.py runserver
```
    Visit http://127.0.0.1:8000/ to see the homepage.

## Usage

    Home Page
        / or http://127.0.0.1:8000/ serves index.html.

    Menu Items
        Browser: /menu/ displays an HTML page for menu items.
        API POST: POST to /menu/ (JSON body) to add a new item (requires authentication).

    Bookings
        Browser: /book/ includes a reservation form.
        API: POST to /bookings with JSON data creates new bookings, while GET can retrieve existing bookings (by date).

    User Authentication
        Djoser endpoints at /auth/ handle user creation, login, logout, token management.
        Token: Obtain via /api-token-auth/ or with Djoser’s /auth/token/login.

    Admin Panel
        /admin/ for managing data (requires superuser account).

## Endpoints Overview

    /menu/ (GET): Renders the menu page.
    /menu/ (POST): Creates a new Menu record (JSON).
    /menu/<int:pk>/: View or edit a single menu item.
    /book/: A page to make reservations via a form.
    /bookings: GET (list bookings by date), POST (create booking).
    /auth/: Djoser-based user and token endpoints.
    /api-token-auth/: Alternative token authentication with DRF’s obtain_auth_token.

## Notes & Highlights

    CSRF: For HTML forms (book.html), Django’s CSRF protection is in place. AJAX calls include X-CSRFToken in headers if needed.
    Throttling: Configured in settings.py (anon: 10/min, user: 100/min).
    Search & Ordering: DRF filters are enabled. You can add ?search= or ?ordering= in query params for relevant endpoints.

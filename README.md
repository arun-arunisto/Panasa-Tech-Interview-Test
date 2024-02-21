# Test for Python Backend Role @ Panasa Technolgy

- [Tech Stack](#tech-stack) : Python, Django, Postgres.

## Book Management

1. Table to store authors (with a field for storing total rating).
2. Table to Store details of book with author relation (with a field for storing
total rating),
3. Single table to store reviews about author and books (with a field for
storing total rating).

## APIs (With authentication)
1. For Creating and listing authors (author object must contain number of
books written by the author.)
2. For updating and listing books
3. For reviewing author and books (with rating) (creating a rating must add
the total rating of author or book and store the average rating in the
respective table.)
4. For listing reviews of a particular author.

## Installation

Clone the repository:

```bash
   git clone https://github.com/arun-arunisto/Panasa-Tech-Interview-Test.git
   cd Panasa-Tech-Interview-Test
```
Create a virtual environment and install dependencies:

```bash
   python -m venv venv
   venv\Scripts\activate #for windows
   pip install -r requirements.txt 
```
Set up the database:

```bash
   #change the settings.py for postgres
   DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "panas_interview_test",
        "USER": "postgres",
        "PASSWORD":"arunisto",
        "HOST":"localhost",
        "PORT":"5433",
    },
    'test': {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "test_database",
        "USER": "postgres",
        "PASSWORD":"arunisto",
        "HOST":"localhost",
        "PORT":"5433",
    },
} 
```
After database configure make migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
Create a superuser account:
```bash
python manage.py createsuperuser
```
To run the tests
```bash
python manage.py test
```
Run the development server:
```bash
python manage.py runserver
```

## API Endpoints
- `/authors/`: Create and list authors
- `/books/`: Create and list books
- `/book/<int:pk>/`: Update and retrieve a specific book
- `/reviews/`: Create and list reviews
- `/author/<int:author_id>/reviews/`: List reviews for a specific author










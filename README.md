# OpenShop Django

A backend e-commerce RESTful API service built with Django, featuring product management and HATEOAS (Hypermedia As The Engine Of Application State) support.

## Tech Stack

* **Language:** Python 3.10
* **Framework:** Django
* **Database:** SQLite (Default for development)
* **Dependency Management:** Pipenv / Pip

---

## Project Structure

```text
openshop-django/
├── openshop/              # Django project settings and configurations
├── products/              # Core app for product management and HATEOAS endpoints
├── OpenShopAPITestCollectionAndEnvironment/ # API testing collection & environment files
├── Pipfile                # Pipenv dependency definitions
├── requirements.txt       # Flat dependency list
└── manage.py              # Django command-line utility

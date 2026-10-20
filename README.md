# OpenShop Django

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-REST-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

OpenShop Django is an e-commerce backend RESTful API service built using Django. The project focuses on product management and the implementation of HATEOAS (Hypermedia As The Engine Of Application State) principles to ensure dynamic and standardized API navigation.

---

## Table of Contents

* [About the Project](#about-the-project)
* [Key Features](#key-features)
* [Tech Stack](#tech-stack)
* [Directory Structure](#directory-structure)
* [Installation Guide](#installation-guide)
* [Running the Application](#running-the-application)
* [API Documentation and Testing](#api-documentation-and-testing)
* [Contributing](#contributing)
* [License](#license)

---

## About the Project

This service is designed to provide a clean and modular e-commerce backend foundation. By implementing the HATEOAS approach, clients consuming this API can dynamically navigate related resources through hypermedia links included directly within the response payload, reducing client dependency on hardcoded endpoint URLs.

---

## Key Features

* **Product Management**: Basic CRUD (Create, Read, Update, Delete) operations for managing e-commerce product data.
* **HATEOAS Support**: Every API response includes relational links so clients can discover available subsequent actions dynamically.
* **API Testing Collection**: Provides environment configuration files and ready-to-use test collections to simplify endpoint validation.

---

## Tech Stack

* **Programming Language**: Python 3.10
* **Framework**: Django
* **Database**: SQLite (Default for local development)
* **Dependency Management**: Pipenv / Pip

---

## Directory Structure

The project directory structure is organized as follows:

```text
openshop-django/
├── openshop/                              # Main Django project configuration and settings
├── products/                              # Core application for product management and HATEOAS endpoints
├── OpenShopAPITestCollectionAndEnvironment/ # API test collections and environment configurations
├── Pipfile                                # Dependency definitions using Pipenv
├── Pipfile.lock                           # Pipenv dependency lockfile
├── requirements.txt                       # Flat dependency list
├── db.sqlite3                             # Development SQLite database
└── manage.py                              # Django command-line utility

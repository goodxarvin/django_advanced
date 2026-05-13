# Django Advanced REST Framework Project

A demonstration project showcasing Django REST Framework skills and best practices. This project was created as a learning assessment to validate proficiency with Django REST Framework concepts and implementation patterns.

## 📚 Project Overview

This repository contains a comprehensive test project that demonstrates understanding and practical implementation of Django REST Framework fundamentals and advanced concepts. It was developed to showcase RESTful API development skills for evaluation purposes.

## 🎯 Purpose

This project serves as a portfolio piece demonstrating:
- Django REST Framework mastery
- RESTful API design principles
- Model design and relationships
- Serialization and deserialization
- Authentication and permissions
- Viewsets and routers
- Filtering, searching, and pagination

## 🛠️ Tech Stack

- **Django**: Web framework
- **Django REST Framework**: REST API toolkit
- **Python**: Programming language

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- virtualenv (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/goodxarvin/django_advanced.git
   cd django_advanced
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

## 📖 API Documentation

The API endpoints and documentation can be accessed at:
- **Blog API Root**: `http://localhost:8000/blog/api/v1/`
- **Account API Root**: `http://localhost:8000/accounts/api/v1/`
- **Swagger**: `http://localhost:8000/swagger/`
- **Browsable API**: Available through Django REST Framework's interface

## 💡 Key Features

- Well-structured models with relationships
- Comprehensive serializers for data validation
- Customized viewsets with appropriate permissions
- RESTful endpoint design
- Proper error handling and status codes

## 📝 Project Structure

```
django_advanced/
├── manage.py
├── requirements.txt
├── README.md
└── [app directories]/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── ...
```

## 🔐 Authentication & Permissions

The project implements Django REST Framework's authentication and permission system to ensure secure API access and proper authorization controls.

## 📦 Dependencies

Core dependencies are listed in `requirements.txt`. Key packages include:
- Django
- djangorestframework

## 🤝 About This Project

This was a learning project created to demonstrate proficiency with Django REST Framework for evaluation purposes. It showcases practical implementation of RESTful API concepts and best practices in Django development.

## 📄 License

This project was created as an educational assessment and demonstration project.

---

**Created**: 2026  
**Purpose**: Django REST Framework proficiency assessment  
**Author**: goodxarvin

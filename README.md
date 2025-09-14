# ERISA Recovery Dev Challenge 2025

A Django web application for managing healthcare claims, built as part of the ERISA Recovery development challenge.

## Features

- **Claims Management**: View, search, and filter healthcare claims
- **Interactive Table**: Paginated claims table with search functionality
- **Claim Details**: Detailed view of individual claims with notes and flags
- **Notes & Flags**: Add notes and flags to claims for review and tracking
- **Responsive Design**: Modern UI with dropdown menus and modals

## Prerequisites

- Python 3.8+ 
- pip (Python package installer)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/ChowMeins/ERISA-Recovery-Dev-Challenge-2025.git
cd ERISA-Recovery-Dev-Challenge-2025
```

### 2. Install Dependencies

Before installing dependencies, setting up a virtual environment is recommended.

Install Django in one of two ways:

**Option A: Install Django directly**
```bash
pip install django
```

**Option B: Install from requirements file (recommended)**
```bash
pip install -r requirements.txt
```

### 4. Database Setup

Navigate to the Django project directory and create and apply database migrations:
```bash
cd erisa_claims
python manage.py makemigrations
python manage.py migrate
```

### 5. Load Sample Data

Load the provided JSON data files into the database:
```bash
python manage.py load_claims ./claims/claim_list_data.json ./claims/claim_detail_data.json
```

This command will populate your database with sample healthcare claims data from the provided JSON files.

### 6. Run the Development Server

Start the Django development server:
```bash
python manage.py runserver
```

---

## Project Structure

```
├── claims/                 # Main Django app
├── templates/             # HTML templates
├── static/               # CSS, JS, and other static files
├── data/                 # JSON data files
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Technologies Used

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, CSS, Alpine.js, HTMX


## Things not implemented

- Admin Dashboard
- Settings
- Seeing your flags/notes
- Log Out feature

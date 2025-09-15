# ERISA Recovery Dev Challenge 2025

This is my submission to the ERISA Recovery Dev Challenge 2025.

More information about this can be found here: https://www.erisachallenge.dev/requirements

This project was started roughly 5 days before the submission date since I had only found out about it then, however,
given the time I had, I did the best I could to implement as many requirements and any additional features as I can.

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

### 2. Set Up Virtual Environment (Recommended)

Before installing dependencies, setting up a virtual environment is recommended.

Create and activate a virtual environment to isolate project dependencies:

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python -m venv venv
source venv/Scripts/activate
```

### 3. Install Dependencies

You can install Django and other dependencies in one of two ways:

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
python manage.py load_claims ./claims/data/claim_list_data.json ./claims/data/claim_detail_data.json
```

This command will populate your database with sample healthcare claims data from the provided JSON files.

### 6. Run the Development Server

Start the Django development server:
```bash
python manage.py runserver
```

## Usage

1. **Claims Table**: Navigate to the main page to view all claims in a paginated table
2. **Search & Filter**: Use the search bar to find claims by ID, patient name, or insurer
3. **View Details**: Click the ellipsis (⋯) button on any claim row to access the dropdown menu
4. **Add Notes**: Select "Add Note" to attach notes to a specific claim
5. **Flag for Review**: Select "Flag for Review" to mark claims that need attention

## Technologies Used

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, CSS, Alpine.js, HTMX


## Things not implemented
- Admin Dashboard
- A UI to view flags/notes (other than clicking the view details button)
- Settings Page

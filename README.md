# Magazine Publication CLI App

A command-line magazine management system built with Python, SQLAlchemy, and Rich.

## Features

- 📝 Manage users, magazines, issues, articles, and subscriptions
- 📊 Rich terminal formatting for better readability
- 🗄️ SQLite database with SQLAlchemy ORM
- 🔄 Full CRUD operations for all entities
- 🌱 Database seeding with sample data

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd magazine-publication-app



2. Set up the virtual environment and install dependencies:

bash
pip install pipenv
pipenv install
pipenv shell

Setup 

Initialize the database:

bash
python -m lib.cli init



Usage

Run the CLI:

bash
python -m lib.cli


Development 


File Structure

magazine-publication-app/
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib/
    ├── __init__.py
    ├── models/
    │   ├── __init__.py
    │   └── models.py
    ├── cli.py         # Command line interface
    ├── debug.py       # Development testing
    ├── helpers.py     # CRUD operations
    └── seed.py        # Database seeding

    Useful Development Commands

Run tests during development:

bash
python -m lib.debug


Reset and reseed the database:

bash
rm magazine.db && python -m lib.cli init && python -m lib.seed


Dependencies

Python 3.9+

SQLAlchemy (ORM)

Click (CLI framework)

Rich (Terminal formatting)

Faker (Test data generation)

python-dotenv (Environment variables)

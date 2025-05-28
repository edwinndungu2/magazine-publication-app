markdown
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
Set up the virtual environment and install dependencies:

bash
pip install pipenv
pipenv install
pipenv shell
Setup
Initialize the database:

bash
python -m lib.cli init
(Optional) Seed with sample data:

bash
python -m lib.seed
Usage
Run the CLI:

bash
python -m lib.cli
Available Commands
Command	Description	Example Usage
init	Initialize the database	python -m lib.cli init
user create	Create a new user	python -m lib.cli user create --username johndoe --email john@example.com
user list	List all users	python -m lib.cli user list
magazine create	Create a new magazine	python -m lib.cli magazine create --title "Tech Today" --description "Tech news"
magazine list	List all magazines	python -m lib.cli magazine list
issue create	Create a new issue	python -m lib.cli issue create --title "Jan 2024" --magazine-id 1
issue list	List issues (optionally by magazine)	python -m lib.cli issue list --magazine-id 1
article create	Create a new article	python -m lib.cli article create --title "Python Tips" --content "..." --author-id 1 --issue-id 1
article list	List articles (filter by author/issue)	python -m lib.cli article list --author-id 1
subscription create	Create a new subscription	python -m lib.cli subscription create --user-id 1 --magazine-id 1 --duration 6
subscription list	List subscriptions (filter by user/magazine)	python -m lib.cli subscription list --user-id 1
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

# Customer Management System

A web-based Customer Relationship Management (CRM) application built with **Django**. This system allows businesses to manage customer records, track projects, and handle account information from a centralized dashboard.

---

## Features

- Customer record creation, viewing, updating, and deletion (CRUD)
- User authentication and account management
- Project tracking linked to customer profiles
- Clean, responsive web interface
- Environment-based configuration for secure deployments

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python / Django 4.1 |
| Database | SQLite (default) |
| Frontend | HTML, CSS |
| Auth | Django built-in authentication |
| Config | python-decouple |

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/joyinola/Customer-Management-System.git
cd Customer-Management-System
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

5. **Run migrations**

```bash
python manage.py migrate
```

6. **Create a superuser (admin)**

```bash
python manage.py createsuperuser
```

7. **Start the development server**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## Project Structure

```
Customer-Management-System/
├── accounts/           # User authentication and account management
├── projects/           # Project tracking module
├── rebounceproject/    # Core Django project settings
├── manage.py
├── requirements.txt
└── .gitignore
```

---

## Usage

- Navigate to `/admin` to access the Django admin panel
- Register or log in to access the customer dashboard
- Add, update, or delete customer records and associated projects

---

## Dependencies

See [`requirements.txt`](requirements.txt) for the full list. Key packages:

- `Django==4.1.1` — web framework
- `python-decouple==3.6` — environment variable management
- `sqlparse==0.4.2` — SQL query formatting

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is open source and available under the [MIT License](LICENSE).

---

## Author

**Simbiat Damilola Adetoro**  
[GitHub](https://github.com/joyinola)

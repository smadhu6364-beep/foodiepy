# Foodiepy: Food Demand Forecasting and Inventory Management System

**Problem statement**

A food delivery company deals with a lot of perishable raw materials, so accurately forecasting daily and weekly demand matters. Too much inventory means wasted stock; too little means out-of-stock orders and customers going to a competitor instead.

**Solution**

Foodiepy is a Django web app that forecasts the number of orders a fulfilment center will need to prepare for, using a Gradient Boosting regression model trained on fulfilment center data (city, area, etc.) and meal data (category, sub-category, etc.). The model reached 92% training accuracy and 83% testing accuracy. It's a generalised model built for research and demonstration, not tuned for any specific company's data.

The app also includes an inventory management section where restaurant owners can sign up, track available inventory, and manage customers and orders.

## Demo

- Video walkthrough: https://youtu.be/45kdILuQyTs
- ML model notebook: https://colab.research.google.com/drive/1-IlwSyDkheIBuSZuY2EgYnS4EqRiZ9kQ?usp=sharing

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript, Bootstrap |
| Backend | Python, Django 3.1, SQLite |
| ML model | Gradient Boosting regression (scikit-learn) |

## Setup

### Prerequisites

- Python 3.8 or 3.9 (this project was built against Django 3.1 and an older scikit-learn model; newer Python/Django combinations aren't guaranteed to work without changes)

### Steps

1. Clone this repository: `git clone https://github.com/smadhu6364-beep/foodiepy.git`
2. Go to the project directory
3. Create a virtual environment: `python3 -m venv env`
4. Activate it: `env/Scripts/activate` (Windows) or `source env/bin/activate` (macOS/Linux)
5. Install dependencies: `pip install -r requirements.txt`
6. Copy `.env.example` to `.env` and fill in a real secret key for anything beyond local testing
7. Apply migrations: `python manage.py migrate`
8. Create a superuser: `python manage.py createsuperuser`
9. Run the project: `python manage.py runserver`

### Environment Variables

| Variable | Description |
|---|---|
| `DJANGO_SECRET_KEY` | Django's cryptographic signing key. A dev-only placeholder is used if unset; generate a real one before deploying anywhere public. |
| `DJANGO_DEBUG` | `True` for local development, `False` in production (default). |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated list of allowed hostnames, required when `DJANGO_DEBUG=False`. |

### Notes on this repository

- `gradientboostmodel.pkl` was trained with scikit-learn 0.24.1. It fails to load on current scikit-learn releases because of internal API changes, but loads and runs cleanly with the versions pinned in `requirements.txt` (`numpy==1.23.5`, `scikit-learn==1.0.2`), which was verified directly against this file.
- Only the font weights actually referenced by `static/css/style.css` are included (Regular, Medium, Bold, Light Italic). The original Open Sans family download included many more static weights and two variable-width fonts that nothing in this project uses, so they were left out to keep the repository lean.

## Contributors

- Darshan Bhavsar: https://www.linkedin.com/in/darshan-bhavsar-93370721a/
- Jigar Parmar: https://www.linkedin.com/in/jigar-parmar-b507a3229/
- Nirmal Trivedi: https://www.linkedin.com/in/nirmal-trivedi-80929a23b/
- Madhu: smadhu6364@gmail.com

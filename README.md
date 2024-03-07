# MINIMI - Django Email Classifier Application

**This coding test involves developing a Django web application that classifies emails as either newsletters or regular emails. The application will integrate various technologies, including Django, machine learning, and CSV parsing. The goal is to assess your skills in web development, data processing, and machine learning.**

# Pyenv/Virtual Environment

### Create a virtual environment

```bash
python3 -m venv myenv
```

### Activate the virtual environment

```
source myenv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

# Initial Setup

> Setup Database

```
python manage.py makemigrations
python manage.py migrate
```


> Start the App

```
python manage.py createsuperuser # create the admin
python manage.py runserver       # start the project
python manage.y test             # test the project
```

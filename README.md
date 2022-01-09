# Library

Administrates, organizes and program your next readings. This small web application is made with Django, so it has all it's benefits. This project includes class-based views, HTTP redirections and models for the database.

## Quickstart

First of all, clone this repo.

``
git clone https://github.com/DD21S/library.git
``

Then, in the project directory, you install the requirements.

``
pip install -r requirements.txt
``

Now, make the migrations.

``
python3 manage.py migrate
``

And finally, run the project.

``
python3 manage.py runserver
``

Ready, now your library is running :&#41;

---

It's recommended to use a virtual enviroment to run Python web applications.

Create one with this command:

``
python3 -m venv venv
``
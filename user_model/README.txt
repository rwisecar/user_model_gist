user_model README
==================

Getting Started
---------------

- cd <directory containing this file>

- $VENV/bin/pip install -e .

- $VENV/bin/initialize_user_model_db development.ini

- $VENV/bin/pserve development.ini

Wednesday "Gist": ends at 12:30pm
-----------------------------------------
- Create a new repo
- Create in that repo a pyramid scaffold that lets you interact with a database
- Create an app with a User model that allows them to login, logout, register, see their profile, and has a home page
- Each User should have a username, hashed password, email, first name, last name, and favorite food
- No CSS necessary but each route should have a template
- Logged-in users shouldn't see a "login" or "registration" link, and logged-out users shouldn't see a "logout" or "profile" link
- No tests necessary
- Email me a link to the repo you created.
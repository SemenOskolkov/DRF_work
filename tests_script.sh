python3 -m venv env
source env/bin/activate
python3 manage.py test
coverage run --source='.' manage.py test
coverage html
deactivate
FROM python:3

WORKDIR /code

RUN pip3 install -r /code/requirements.txt

COPY . .

CMD python manage.py migrate
CMD python manage.py runserver
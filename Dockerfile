FROM python:3.9.0

WORKDIR /home/

Run echo "dkanwefwesjskeee"

RUN git clone https://github.com/gandi0330/DjangoProject.git

WORKDIR /home/DjangoProject/

RUN echo "SECRET_KEY=django-insecure-ftv4q#lb+sk1%zf$b&q4wb$kjemfku2y4z+jrry7654vnwzwqz" > .env

RUN pip install -r requirements.txt

RUN pip install mysqlclient

RUN pip install gunicorn

EXPOSE 8000

CMD ["bash","-c","python manage.py collectstatic --noinput --settings=DjangoProject.settings.deploy && python manage.py migrate --settings=DjangoProject.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=DjangoProject.settings.deploy DjangoProject.wsgi --bind 0.0.0.0:8000"]

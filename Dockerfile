FROM python:3.9.0

WORKDIR /home/

Run echo "dkanwefwefrssjsk"

RUN git clone https://github.com/gandi0330/DjangoProject.git

WORKDIR /home/DjangoProject/

RUN echo "SECRET_KEY=django-insecure-ftv4q#lb+sk1%zf$b&q4wb$kjemfku2y4z+jrry7654vnwzwqz" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn","DjangoProject.wsgi","--bind","0.0.0.0:8000"]

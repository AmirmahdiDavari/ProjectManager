FROM dockerhub.ir/python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

RUN apt update
RUN apt install default-libmysqlclient-dev build-essential -y

#RUN apt install libmysqlclient-dev
ADD requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /app/
RUN pip install djangorestframework
RUN pip install django-rest-swagger
RUN pip install django-jalali-date
RUN pip install django-filter
RUN pip install pymysql
RUN pip install mysqlclient
RUN pip install djangorestframework-simplejwt
RUN pip install Pillow


#RUN python manage.py runserver 0.0.0.0:8000
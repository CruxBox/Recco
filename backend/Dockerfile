FROM python:3.6

ENV PYTHONBUFFERED 1

RUN mkdir /backend

COPY ./requirements.txt /backend/requirements.txt

WORKDIR /backend

RUN pip3 install -r requirements.txt

COPY . /backend/

RUN chmod +x /backend/docker-entrypoint.sh

ENTRYPOINT ["bash","/backend/docker-entrypoint.sh"]
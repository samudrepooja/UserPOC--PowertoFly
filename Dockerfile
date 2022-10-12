FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /USERPOC

ADD . /USERPOC

COPY ./requirements.txt /USERPOC/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -r requirements.txt

COPY . /USERPOC

EXPOSE 6379


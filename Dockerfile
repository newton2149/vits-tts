FROM continuumio/anaconda3:latest

WORKDIR /vits

COPY . .

RUN pip install -r requirements.txt



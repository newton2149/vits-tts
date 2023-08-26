FROM continuumio/anaconda3:latest

WORKDIR /vits

COPY . .



RUN apt-get update && apt-get install -y build-essential

RUN apt-get install -y espeak

RUN pip install -r requirements.txt

RUN python /vits/monotonic_align/setup.py build_ext --inplace



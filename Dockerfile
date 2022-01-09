FROM python:3.10
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
LABEL maintainer "MahanBi"
WORKDIR /pro_data
COPY requirements.txt /pro_data/
RUN pip install -r requirements.txt
COPY . /pro_data/
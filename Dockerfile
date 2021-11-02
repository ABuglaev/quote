FROM python:3
LABEL maintainer="a_buglaev@gmx.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt && rm -f Dockerfile requirements.txt
EXPOSE 8081

CMD python3 ./server.py
FROM python:3.11.1-slim

WORKDIR /app/

ENV PYTHONDONTWRITEBYTEapp 1
ENV PYTHONBUFFERED 1
ENV SERVER_PORT=8000

RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE $SERVER_PORT

RUN chmod +x ./start.sh

ENTRYPOINT ["./start.sh"]

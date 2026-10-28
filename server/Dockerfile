# docker build <directory> -t <name>
# docker run --rm -p 80:7000 <name>
FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7000

CMD ["python", "./server.py"]
FROM python:3.9

# cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . app
WORKDIR /app

EXPOSE 8001

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8001"]
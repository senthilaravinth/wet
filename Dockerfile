FROM python:3.9-slim
WORKDIR /app
COPY app.py .
# The script runs, creates the file, then the container stays alive for a bit
CMD ["python", "app.py"]
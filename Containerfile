FROM docker.io/python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN useradd -m -r appuser
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --progress-bar off -r requirements.txt
COPY app.py .
COPY templates/ templates/
RUN chown -R appuser:appuser /app
USER appuser
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
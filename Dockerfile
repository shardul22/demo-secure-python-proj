# Use an official lightweight Python image
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN useradd -m -r appuser
WORKDIR /app

# 1. Copy the application source code
COPY pyproject.toml app.py README.md ./

# 2. COPY the generated wheels from your Mac into the Docker image
COPY ./generated_wheels /app/wheelfiles/

# 3. Install the application directly from the baked-in wheels
RUN pip install --no-cache-dir --no-index --find-links=/app/wheelfiles .

# 4. Create the new explicitly named export directory and set ownership
RUN mkdir output /app/exported_scanned_wheels && \
    chown appuser:appuser output /app/exported_scanned_wheels /app/wheelfiles

USER appuser

# 5. The startup command: Copy wheels to the new export volume, THEN run the app
CMD cp -r /app/wheelfiles/* /app/exported_scanned_wheels/ && run-demo
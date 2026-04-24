# Use an official lightweight Python image
FROM python:3.10-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a non-root user for security compliance
RUN useradd -m -r appuser

# Set the working directory
WORKDIR /app

# Copy the project files
COPY pyproject.toml app.py README.md ./

# Install the package (this fetches wheels from PyPI based on pyproject.toml)
RUN pip install --no-cache-dir .

# Ensure output directory exists and is owned by the non-root user
RUN mkdir output && chown appuser:appuser output

# Switch to the non-root user
USER appuser

# Define the default execution command
CMD ["run-demo"]
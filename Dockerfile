# Use official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system packages required by some Python wheels (Pillow, etc.)
COPY requirements.txt .
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	   build-essential \
	   libjpeg-dev \
	   zlib1g-dev \
	   libfreetype6-dev \
	   liblcms2-dev \
	   libwebp-dev \
	   tcl8.6-dev \
	   tk8.6-dev \
	&& rm -rf /var/lib/apt/lists/* \
	&& python -m pip install --upgrade pip setuptools wheel \
	&& pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]


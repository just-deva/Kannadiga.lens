FROM python:3.10-slim

# Install Tesseract OCR and Kannada language data
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-kan \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy all project files into container
COPY . /app

# Install Python requirements if present
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Expose Render container port
EXPOSE 10000

# Start server.py
CMD ["python", "server.py"]

# Start with a lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first (speeds up future builds)
COPY requirements.txt .

# Install all packages
RUN pip install -r requirements.txt

# Copy everything else into the container
COPY . .

# Tell Docker this app uses port 5000
EXPOSE 5000

# The command to run when the container starts
CMD ["python", "app.py"]
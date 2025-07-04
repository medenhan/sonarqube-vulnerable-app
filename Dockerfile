# Start with a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# --- FIX: Create and use a non-root user ---
# Create a new user named "appuser"
RUN useradd -m appuser

# Switch to the new user
USER appuser
# ------------------------------------------

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
# Explicitly copy only the necessary files
COPY app.py .
COPY requirements.txt .
COPY sonar-project.properties .

# Expose the port the app runs on
EXPOSE 8080

# The command to run when the container starts
CMD ["python", "app.py"]
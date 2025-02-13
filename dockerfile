# Use the official Python 3.11 slim image as the base
FROM python:3.11-slim

# Install OpenJDK (headless) for the Anvil app server
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jre-headless \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages:
#  - anvil-app-server: The open-source Anvil server
RUN pip install --no-cache-dir \
    anvil-app-server \
    tensorflow \
    numpy \
    pandas \
    scikit-learn \
    matplotlib

# Set up a working directory
WORKDIR /app

# Copy your Anvil application code into /app
COPY . /app

# Expose the default port for the Anvil server
EXPOSE 3030

# On container start, run the Anvil App Server
CMD ["anvil-app-server", "--app", "/app", "--port", "3030"]

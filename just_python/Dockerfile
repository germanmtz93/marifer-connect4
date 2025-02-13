FROM python:3.11

# Copy requirements.txt to the root directory of the container
COPY requirements.txt /

# Install the dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Create a directory and set permissions
RUN mkdir /FOLDERNAME/
RUN chmod -R 777 /FOLDERNAME

# Copy the checking.py script to the root directory of the container
COPY checking.py /
COPY cnn_67.h5 /
COPY transformer_47.h5 /

# Set environment variable to ensure output is not buffered
ENV PYTHONUNBUFFERED=1

# Command to run the checking.py script
CMD [ "python", "./checking.py" ]
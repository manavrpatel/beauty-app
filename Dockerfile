# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=beauty_app.settings

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY ./requirements.txt /app/requirements.txt


# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt


# Copy the current directory contents into the container at /app
COPY . .


RUN ls

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run Gunicorn when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:application",  "--timeout", "1000"]

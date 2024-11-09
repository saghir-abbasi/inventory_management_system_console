
# base image
FROM python:3.12-slim

# setup working directory in container
WORKDIR /app

# copy all files to app directory
COPY . .


# command to run on container start
CMD ["python", "main.py"]
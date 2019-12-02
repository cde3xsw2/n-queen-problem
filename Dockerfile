FROM python:3

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install pipenv
COPY requirements.txt  /code/
RUN pip install -r requirements.txt 

COPY . /code/







CMD [ "python", "./solve.py" ]





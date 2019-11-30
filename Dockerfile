FROM python:3


ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update && apt-get upgrade -y && apt-get install -y git

RUN pwd

ADD check.py /check.py
ADD core /core

RUN pwd
ENTRYPOINT ["python", "-u", "/check.py" ]

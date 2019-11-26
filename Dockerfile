FROM python:3

ADD check.py /
ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt
CMD [ "python", "-u", "./check.py" ]

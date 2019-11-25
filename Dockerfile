FROM python:latest

ADD check.py /check.py
ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt
RUN chmod +x check.py
ENTRYPOINT ["/checker.py"]

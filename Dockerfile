FROM python:latest

ADD checker.py /checker.py
ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt
RUN chmod +x checker.py
ENTRYPOINT ["/checker.py"]

FROM python:3

RUN pwd
ADD check.py /
ADD core/fileproc.py /core/fileproc.py
ADD core/urlmarker.py /core/urlmarker.py
ADD core/urlproc.py /core/urlproc.py
    
ADD requirements.txt /requirements.txt

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

RUN pip install -r requirements.txt
RUN pwd
CMD [ "python", "-u", "./check.py" ]

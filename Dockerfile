FROM python:3
RUN apt-get install -y git
RUN pip install urlchecker==0.0.11
COPY entrypoint.sh /entrypoint.sh
WORKDIR /github/workspace
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]

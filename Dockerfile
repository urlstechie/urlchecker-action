FROM ghcr.io/urlstechie/urlchecker:0.0.32
COPY entrypoint.sh /entrypoint.sh
RUN pip install "git+https://github.com/danger89/fake-useragent@master#egg=fake-useragent"
WORKDIR /github/workspace
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]

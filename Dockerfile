FROM ghcr.io/urlstechie/urlchecker:0.0.32
COPY entrypoint.sh /entrypoint.sh
RUN pip uninstall fake-useragent && \
    pip install git+https://github.com/danger89/fake-useragent.git
WORKDIR /github/workspace
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]

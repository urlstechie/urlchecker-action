FROM quay.io/urlstechie/urlchecker:0.0.25
COPY entrypoint.sh /entrypoint.sh
WORKDIR /github/workspace
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]

FROM ghcr.io/urlstechie/urlchecker:0.0.33
COPY entrypoint.sh /entrypoint.sh
WORKDIR /github/workspace
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]

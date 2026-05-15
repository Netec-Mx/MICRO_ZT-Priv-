FROM postgres:16-bookworm

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       bash \
       curl \
       dnsutils \
       iproute2 \
       iptables \
       nftables \
       iputils-ping \
       netcat-openbsd \
       procps \
    && rm -rf /var/lib/apt/lists/*
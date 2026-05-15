FROM nginx:1.27-bookworm

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

COPY default.conf /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/index.html
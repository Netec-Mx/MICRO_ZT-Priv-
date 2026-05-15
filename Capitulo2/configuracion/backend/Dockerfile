FROM python:3.12-slim-bookworm

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

WORKDIR /app
COPY app.py /app/app.py

EXPOSE 8080

CMD ["python", "/app/app.py"]
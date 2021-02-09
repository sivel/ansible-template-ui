FROM alpine
MAINTAINER Matt Martz <matt@sivel.net>

RUN set -x && \
    apk add --no-cache python3 py3-pip openssl-dev python3-dev libffi-dev ca-certificates gcc make musl-dev git yaml-dev && \
    apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community rust cargo && \
    pip3 install -U pip && \
    pip3 install ansible jmespath netaddr && \
    apk del openssl-dev python3-dev libffi-dev gcc make musl musl-dev git yaml pkgconf rust cargo

COPY execute.sh /execute.sh
COPY playbook.yml /playbook.yml

CMD ["/bin/sh", "/execute.sh"]

FROM alpine
MAINTAINER Matt Martz <matt@sivel.net>

RUN set -x && \
    apk add -U python3 py3-pip openssl-dev python3-dev libffi-dev ca-certificates gcc make musl-dev git yaml-dev && \
    pip3 install -U pip && \
    pip3 install ansible jmespath netaddr && \
    apk del openssl-dev python2-dev libffi-dev gcc make musl musl-dev git yaml pkgconf

COPY execute.sh /execute.sh
COPY playbook.yml /playbook.yml

CMD ["/bin/sh", "/execute.sh"]

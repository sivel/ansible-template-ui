FROM alpine
MAINTAINER Matt Martz <matt@sivel.net>

RUN set -x && \
    apk add -U python2 py-pip openssl-dev python2-dev libffi-dev ca-certificates gcc make musl-dev git && \
    pip install -U pip && \
    pip install ansible jmespath netaddr && \
    apk del openssl-dev python2-dev libffi-dev gcc make musl-dev git

COPY execute.sh /execute.sh
COPY hosts /hosts
COPY playbook.yml /playbook.yml

CMD ["/bin/sh", "/execute.sh"]

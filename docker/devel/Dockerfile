FROM alpine
MAINTAINER Matt Martz <matt@sivel.net>

RUN set -x && \
    apk add -U python3 py3-pip openssl-dev python3-dev libffi-dev ca-certificates gcc make musl-dev git && \
    pip3 install -U pip && \
    pip3 install git+https://github.com/ansible/ansible.git@devel#egg=ansible jmespath netaddr && \
    apk del openssl-dev python2-dev libffi-dev gcc make musl-dev git

COPY execute.sh /execute.sh
COPY playbook.yml /playbook.yml

CMD ["/bin/sh", "/execute.sh"]

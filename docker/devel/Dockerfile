FROM alpine
MAINTAINER Matt Martz <matt@sivel.net>

COPY clean_collections.py /tmp/clean_collections.py
COPY execute.sh /execute.sh
COPY playbook.yml /playbook.yml

ENV PIP_BREAK_SYSTEM_PACKAGES=1

RUN set -x && \
    apk add --no-cache python3 py3-pip openssl-dev python3-dev libffi-dev ca-certificates gcc make musl-dev git yaml-dev rust cargo && \
    pip3 install --no-cache-dir --no-compile -U pip && \
    pip3 install --no-cache-dir --no-compile jmespath netaddr && \
    pip3 install --no-cache-dir --no-compile ansible && \
    pip3 install --no-cache-dir --no-compile -U https://github.com/ansible/ansible/archive/devel.tar.gz && \
    apk del py3-pip openssl-dev python3-dev libffi-dev ca-certificates gcc make musl-dev git yaml rust cargo && \
    python3 /tmp/clean_collections.py && \
    rm -rf /root/.cache && \
    rm -rf /root/.cargo

CMD ["/bin/sh", "/execute.sh"]

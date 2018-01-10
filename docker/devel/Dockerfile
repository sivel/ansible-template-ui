FROM alpine
MAINTAINER Matt Martz <matt@sivel.net>

RUN apk add -U python2 py-pip openssl-dev python2-dev libffi-dev ca-certificates gcc make musl-dev git

RUN pip install git+https://github.com/ansible/ansible.git@devel#egg=ansible jmespath netaddr

COPY execute.sh /execute.sh
COPY hosts /hosts
COPY playbook.yml /playbook.yml

CMD ["/bin/sh", "/execute.sh"]

#!/bin/sh

export ANSIBLE_STDOUT_CALLBACK=json
export ANSIBLE_COMMAND_WARNINGS=0
export ANSIBLE_RETRY_FILES_ENABLED=0

echo $VARIABLES | base64 -d > /variables.yml
echo $TEMPLATE | base64 -d > /template.j2

timeout -s KILL 5 ansible-playbook -i hosts -e @variables.yml playbook.yml

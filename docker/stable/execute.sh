#!/bin/sh

export ANSIBLE_STDOUT_CALLBACK=json
export ANSIBLE_COMMAND_WARNINGS=0

echo $VARIABLES | base64 -d > /variables.yml
echo $TEMPLATE | base64 -d > /template.j2

timeout -t 3 -s KILL ansible-playbook -i hosts -e @variables.yml playbook.yml

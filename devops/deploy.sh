#!/bin/bash
ansible-playbook ./ansible/deploy.yml --private-key=~/.ssh/id_rsa -K -u deployer -i ./ansible/hosts

#!/bin/bash

sudo sed -i 's@file_path": "/var/log/eb-docker/containers/eb-current-app/stdouterr.log@file_path": "/var/log/eb-docker/containers/eb-current-app/*-stdouterr.log@g' /opt/aws/amazon-cloudwatch-agent/etc/beanstalk.json

sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/opt/aws/amazon-cloudwatch-agent/etc/beanstalk.json -s


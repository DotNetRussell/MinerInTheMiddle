#!/bin/bash

apt-get update;
apt install python-pip -y;
pip install wheel;
apt-get install build-essential python-dev libnetfilter-queue-dev;
pip install NetfilterQueue;
apt install dsniff -y;
pip install scapy;



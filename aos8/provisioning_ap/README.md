# Overview
AOS8 Aruba Mobility Controller Support REST API for most of configuration.
You can provision AP's parameters by this script.

# Usage
- Set Controller's login credential, IP address and config_path in "config.ini"
- Set AP Parameters in "ap_data.csv". In this example, you can set ap_name, ap_group, ipaddr, netmask and gatewayip. AP wired-mac is mandatory parameter.
- Run provision_ap.py script to provision your APs. Need config.ini and ap_data.csv files in the same directory.

# Caution
In this sample script, https server certification verification was disabled. Please enable verification for your environment.

# How to use AOS8 API
Please refer following Aruba Developer Hub for more detail about basic AOS8 REST API.
Getting Started with AOS 8 API
https://developer.arubanetworks.com/aruba-aos/docs/getting-started-aos8-restapi

AP provisioning workflow via API
https://developer.arubanetworks.com/aruba-aos/docs/day-1-configuration-tasks#ap-provisioning-workflow-via-api

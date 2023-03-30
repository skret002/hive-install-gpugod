#!/bin/bash
import os, subprocess, requests, time, json
service = ('tune','miner-a','card_auto_fan','fan', 'cpu_fuse')
def install_deps():
    global service
    os.system("yes | sudo apt-get install lm-sensors")
    os.system("yes | sudo sensors-detect")
    os.system("sudo cp -r /home/hive-install-gpugod/modules /etc/")
    response = requests.post('http://176.119.147.118:8000/soft_revison/')
    url = response.json()["data"]["url"]
    os.system("wget -O fanonrig.zip "+ url)
    os.system("unzip fanonrig.zip -D /home/onrig")
    os.system("rm fanonrig.zip")
    os.system("cd /home/onrig/ && sudo  cp -r *.sh /home/ && sudo  cp -r *.service /etc/systemd/system/ && cd /home/ && sudo chmod ugo+x *.sh")
    os.system("sudo systemctl daemon-reload")
    for i in service:
       os.system(f"systemctl enable {i}") 
    os.system("sudo systemctl start fan")

if __name__ == '__main__':
    install_deps()

#!/bin/bash
import os, subprocess, requests, time,json
service = ('keeper_fan','tune','miner-a','card_auto_fan','fan', 'cpu_fuse')
def install_deps():
    global service
    os.system("yes | sudo apt-get install lm-sensors")
    os.system("yes | sudo sensors-detect")
    os.system("sudo cp -r /home/hive-install-gpugod/modules /etc/")
    response = requests.post('http://176.119.147.118:8000/soft_revison/')
    url = response.json()["data"]["url"]
    os.system("wget -O fanonrig.zip "+ url)
    os.system("rm -r /home/onrig")
    os.system("unzip fanonrig.zip -d /home/onrig")
    os.system("rm fanonrig.zip")         
    os.system("sudo  cp -r /home/onrig/*.sh /home/ && sudo  cp -r /home/onrig/*.service /etc/systemd/system/ && sudo chmod ugo+x /home/*.sh")
    os.system("sudo systemctl daemon-reload")
    for i in service:
       os.system(f"systemctl enable {i}") 
    os.system("sudo systemctl start fan")
    os.system("reboot")
    
if __name__ == '__main__':   
    install_deps() 
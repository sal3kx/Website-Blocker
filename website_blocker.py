import time
from datetime import datetime as dt
from sys import platform

hosts_path = ''

if platform == "linux" or platform == "linux2":
    # linux
    hosts_path = "/etc/hosts"
elif platform == "darwin":
    # OS X
    host_path =  "/private/etc/hosts"
elif platform == "win32"
	# Windows
	hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
	

hosts_temp=r"D:\Dropbox\pp\block_websites\Demo\hosts"
hosts_path="/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","dub119.mail.live.com","www.dub119.mail.live.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours...")
    time.sleep(5)

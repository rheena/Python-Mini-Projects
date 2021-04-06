import time
from datetime import datetime as dt
hosts_path = r'/etc/hosts' #r is for raw string
hosts_temp = 'hosts'
redirect = '127.0.0.2'
web_sites_list = ['www.instagram.com', 'instagram.com']
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() <dt(dt.now().year, dt.now().month, dt.now().day, 22):
        print('Working hours')
        with open(hosts_path, 'r+')as file:
            content = file.read()
            for website in web_sites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+' '+website+'\n')
                
    else:
        print('Fun time')
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)    #reset the pointer to the top of the text file
            for line in content:
                #overwriting the whole file
                if not any(website in line for website in web_sites_list):
                    file.write(line)
                #Do nothing otherwise
            file.truncate()     #This deletes the trailing lines (that contains DNS)
        time.sleep(5)

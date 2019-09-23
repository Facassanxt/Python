import re
def get_ip_from_cfg(file_name):
    with open('15\\' + file_name + '.txt','r') as f:
        list = []
        for line in f:
            match  = re.search(r'ip address (?P<ip>([0-9]{1,3}[\.]){3}[0-9]{1,3}) (?P<mask>([0-9]{1,3}[\.]){3}[0-9]{1,3})', line)
            if match != None:
                list_ip = match.group('ip')
                list_mask = match.group('mask')
                tuple = (list_ip,list_mask)
                list.append(tuple)
    return list
    
if __name__ == "__main__":
    print(get_ip_from_cfg('config_r1'))
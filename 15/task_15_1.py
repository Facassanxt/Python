import re
def get_ip_from_cfg(file_name):
    with open('15\\' + file_name + '.txt','r') as f:
        list = []
        for line in f:
            match  = re.search(r'ip address (\S+) (\S+)', line)
            if match != None:
                list.append(match.groups())
    return list

if __name__ == "__main__":
    print(get_ip_from_cfg('config_r1'))
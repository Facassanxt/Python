import re
def get_ip_from_cfg(file_name):
    with open('15\\' + file_name + '.txt','r') as f:
        dict = {}
        for line in f:
            interface = re.search(r'interface (\S+)', line)
            ip = re.search(r'ip address (\S+) (\S+)', line)
            if interface:
                k = interface.group(1)
            elif ip:
                dict.update({k:ip.groups()})
    return dict

if __name__ == "__main__":
    print(get_ip_from_cfg('config_r1'))
import re
def get_ip_from_cfg(file_name):
    with open('15\\' + file_name + '.txt','r') as f:
        dict = {}
        list_value = []
        for line in f:
            interface = re.search(r'interface (\S+)', line)
            ip = re.search(r'ip address (\S+) (\S+)', line)
            if interface:
                key = interface.group(1)
            elif ip and line.startswith(' '):
                if key in dict:
                    dict[key].append(ip.groups())
                else:
                    list_value.append(ip.groups())
                    dict.update({key:list_value})
                    list_value = []
    return dict

if __name__ == "__main__":
    print(get_ip_from_cfg('config_r2'))
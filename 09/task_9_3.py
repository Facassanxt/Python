def get_int_vlan_map(config_filename):
    access = {}
    trunk = {}
    with open('09\\' + config_filename,'r') as f:
        for line in f:
            line = line.rstrip()
            if line.find('FastEthernet') != -1:
                FastEthernet = line.split()[1]
            if line.find('access vlan') != -1:
                access.update({FastEthernet:int(line.split()[3])})
            if line.find('allowed vlan') != -1: 
                allowed_vlan = list(map(int,''.join(line.split()[4]).split(',')))
                trunk.update({FastEthernet:allowed_vlan})
    return access,trunk
if __name__ == "__main__":
    print(get_int_vlan_map('config_sw1.txt'))
def get_int_vlan_map(config_filename):
    access = {}
    trunk = {}
    flag = False
    with open('09\\' + config_filename,'r') as f:
        for line in f:
            line = line.rstrip()
            if (line.find('FastEthernet') != -1) and flag == False:
                FastEthernet = line.split()[1]
                flag = True
            elif line.find('access vlan') != -1:
                access.update({FastEthernet:int(line.split()[3])})
                flag = False
            elif line.find('allowed vlan') != -1: 
                allowed_vlan = list(map(int,''.join(line.split()[4]).split(',')))
                trunk.update({FastEthernet:allowed_vlan})
                flag = False
            elif (line.find('!') != -1) and flag == True:
                access.update({FastEthernet:int(1)})
                flag = False
    return access,trunk
if __name__ == "__main__":
    print(get_int_vlan_map('config_sw2.txt'))
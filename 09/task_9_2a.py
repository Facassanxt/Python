trunk_mode_template = [
    'switchport mode trunk', 'switchport trunk native vlan 999',
    'switchport trunk allowed vlan'
]

trunk_config = {
    'FastEthernet0/1': [10, 20, 30],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]
}

def generate_trunk_config(intf_vlan_mapping,trunk_template):
    list = []
    d = {}
    for intf, vlan in intf_vlan_mapping.items():
        for command in trunk_template:
            if command.endswith('switchport trunk allowed vlan'):
                strvlan = ",".join(str(x) for x in vlan)
                list.append(command + ' ' + strvlan)
            else:
                list.append(command)
        d.update({intf:list})
        list = []
    return d

if __name__ == "__main__":
    print(generate_trunk_config(trunk_config,trunk_mode_template))


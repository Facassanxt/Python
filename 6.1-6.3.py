mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []
# print(mac[0].replace(':','.'))
for num in range(len(mac)):
    mac_cisco.append(mac[num].replace(':','.'))
print(mac_cisco)

# ip = input('Введите IP-адреса в формате 10.0.1.1: ')
# Ip = ip.split('.')
# if int(Ip[0]) >=1 and int(Ip[0])<=223:
#     print('unicast')
# elif int(Ip[0]) >=224 and int(Ip[0]) <=239:
#     print('multicast')
# elif ip == '255.255.255.255':
#     print('local broadcas')
# elif ip == '0.0.0.0':
#     print('unassigned')
# else: 
#     print('unused')

'''
ip = input('Введите IP-адреса в формате 10.0.1.1: ')
Ip = ip.split('.')
while True:
    ip_correct = True
    for num in range(4):
        print(int(Ip[num]))
        if int(Ip[num]) < 0 or int(Ip[num]) > 255 or len(Ip) != 4:
            print('Неправильный IP-адрес')
            Ip = input('Введите IP-адреса в формате 10.0.1.1 еще раз: ').split('.')
            ip_correct = False
            break
    if ip_correct == True:
        if int(Ip[0]) >=1 and int(Ip[0])<=223:
            print('unicast')
        elif int(Ip[0]) >=224 and int(Ip[0]) <=239:
            print('multicast')
        elif ip == '255.255.255.255':
            print('local broadcas')
        elif ip == '0.0.0.0':
            print('unassigned')
        else: 
            print('unused')
        break
'''

access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

access = {
    '0/12': '10',
    '0/14': '11',
    '0/16': '17',
    '0/17': '150'
}
trunk = {
        '0/1': ['add', '10', '20'],
        '0/2': ['add', '11', '30', '69'],
        '0/4': ['only', '17'],
        '0/8': ['del', '17'],
        '0/10': ['only', '17'],
        '0/22': ['add', '17'],
        '0/32': ['del', '17'],
        '0/6': ['only', '17']
    }

for intf, vlan in access.items():
    print('interface FastEthernet ' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))

for intf, vlan in trunk.items():
    print('\n------------------'+vlan[0]+'------------------')
    print('interface FastEthernet ' + intf)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            if vlan[0] == 'add':
                vlan.remove(vlan[0])
                print(' {} {}'.format(command, 'add ' + ",".join(vlan)))
            if vlan[0] == 'only':
                vlan.remove(vlan[0])
                print(' {} {}'.format(command, ",".join(vlan)))
            if vlan[0] == 'del':
                vlan.remove(vlan[0])
                print(' {} {}'.format(command, 'remove ' +  ",".join(vlan)))
        else:
            print(' {}'.format(command))
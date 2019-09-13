london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
#print(london_co[input('Введите имя устройства: ')])
#print(london_co[input('Введите имя устройства: ')][input('Введите имя параметра (ios, model, vendor, location, ip): ')])
'''
try:
    print(london_co[input('Введите имя устройства: ')][input('Введите имя параметра (ios, model, vendor, location, ip): ')])
except KeyError:
    print('Введите правильные данные!')
'''

'''
try:
    print(london_co[input('Введите имя устройства: ')][input('Введите имя параметра (ios, model, vendor, location, ip): ').lower()])
except KeyError:
    print('Введите правильные данные!')
'''

'''
vvod = input("Введите IP-сети в формате: 10.1.1.0/24: ")
ip, mask = vvod.split('/')
ip = ip.split('.')
IP = '{:<8} {:<8} {:<8} {:<8}'.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))
BINIP = '{:08b} {:08b} {:08b} {:08b}'.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))
print('Network:')
print(IP)
print(BINIP)
print("\n")

Mask = '{:0<32}'.format('1' * int(mask))
print('Mask:')
print('/' + mask)
print('{:<8} {:<8} {:<8} {:<8}'.format(int(Mask[0:8],2), int(Mask[8:16],2), int(Mask[16:24],2), int(Mask[24:32],2)))
print('{:<8} {:<8} {:<8} {:<8}'.format(Mask[0:8], Mask[8:16], Mask[16:24], Mask[24:32]))
'''

'''
vvod = input("Введите IP-сети в формате: 10.1.1.0/24: ")
ip, mask = vvod.split('/')
ip = ip.split('.')
if ip[3] != 0:
    ip[3] = 0
IP = '{:<8} {:<8} {:<8} {:<8}'.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))
BINIP = '{:08b} {:08b} {:08b} {:08b}'.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))
print('Network:')
print(IP)
print(BINIP)
print("\n")

Mask = '{:0<32}'.format('1' * int(mask))
print('Mask:')
print('/' + mask)
print('{:<8} {:<8} {:<8} {:<8}'.format(int(Mask[0:8],2), int(Mask[8:16],2), int(Mask[16:24],2), int(Mask[24:32],2)))
print('{:<8} {:<8} {:<8} {:<8}'.format(Mask[0:8], Mask[8:16], Mask[16:24], Mask[24:32]))
'''

# from sys import argv
# vvod = argv[1]
# ip, mask = vvod.split('/')
# ip = ip.split('.')
# if ip[3] != 0:
#     ip[3] = 0
# IP = '{:<8} {:<8} {:<8} {:<8}'.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))
# BINIP = '{:08b} {:08b} {:08b} {:08b}'.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))
# print('Network:')
# print(IP)
# print(BINIP)
# print("\n")

# Mask = '{:0<32}'.format('1' * int(mask))
# print('Mask:')
# print('/' + mask)
# print('{:<8} {:<8} {:<8} {:<8}'.format(int(Mask[0:8],2), int(Mask[8:16],2), int(Mask[16:24],2), int(Mask[24:32],2)))
# print('{:<8} {:<8} {:<8} {:<8}'.format(Mask[0:8], Mask[8:16], Mask[16:24], Mask[24:32]))

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
dict = {'access':access_template,'trunk':trunk_template}
ac = input('Введите режим работы интерфейса (access/trunk): ')
print('interface {}'.format(input('Введите тип и номер интерфейса: ')))
print('\n'.join(dict.get(ac)).format(input('Введите номер влан(ов): ')))
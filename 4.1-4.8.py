NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(NAT.replace('Fast','Gigabit') + '\n')

mac = 'AAAA:BBBB:CCCC'
print(mac.replace(':','.') + '\n')

config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
print(config[config.find('1'):].split(','))
print()

vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
print(sorted(dict.fromkeys(vlans)))
print()

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

command1 = command1[command1.find('1'):].split(',')
command2 = command2[command2.find('1'):].split(',')
result = list(set(command1) & set(command2))
print(result)
print()

ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.replace('O','OSPF').replace('[', '').replace(']', '').replace(',', '')
RESULT = ospf_route.split(' ')
print('Protocol:             ', RESULT[0])
print('Prefix:               ', RESULT[1])
print('AD/Metric:            ', RESULT[2])
print('Next-Hop:             ', RESULT[4])
print('Last update:          ', RESULT[5])
print('Outbound Interface:   ', RESULT[6])
print()

mac = 'AAAA:BBBB:CCCC'
print(bin(int(mac.replace(':',''), 16)))
print()

ip = '192.168.3.1'
IP = ip.split('.')
nIP = '{:<8} {:<8} {:<8} {:<8}'.format(int(IP[0]), int(IP[1]), int(IP[2]), int(IP[3]))
BINIP = '{:08b} {:08b} {:08b} {:08b}'.format(int(IP[0]), int(IP[1]), int(IP[2]), int(IP[3]))
print(nIP)
print(BINIP)
print("\n")

ip_template = '''
{0:<8} {1:<8} {2:<8} {3:<6}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template.format(int(IP[0]), int(IP[1]), int(IP[2]), int(IP[3])))
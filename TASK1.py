########################################################## first task ####################################################################

NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NAT2 = NAT.replace('Fast','Gigabit')
print(NAT2)
print("\n")

########################################################## second task ###################################################################

mac = 'AAAA:BBBB:CCCC'
commands3 = mac.replace(':', ".")
print(commands3)
print("\n")

#********************************************************* second option *********************************************************

commands = mac.split(':')
commands2 = commands[0]+"."+commands[1]+"."+commands[2]
print(commands2)
print("\n")

########################################################### third task ##########################################################
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
config.find('1')
config = config[30:]
config = config.split(',')
print(config)
print("\n")

########################################################### fourth task ##########################################################
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
print(sorted(vlans))
print("\n")

########################################################### fiveth task ##########################################################
command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'
# print(command1.find('1')) # c 30-го
command1 = command1[30::].split(',')
command2 = command2[30::].split(',')
print(command1)
print(command2)
print("\n")

########################################################### sixth task ##########################################################
ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.replace('O','OSPF')

RESULT = ospf_route.split(' ')

print('Protocol: ', RESULT[0])
print('Prefix: ', RESULT[1])
print('AD/Metric: ', RESULT[2])
print('Next-Hop: ', RESULT[4])
print('Last update: ', RESULT[5])
print('Outbound Interface: ', RESULT[6])
print("\n")

########################################################### seventh task ##########################################################
MAC = 'AAAA:BBBB:CCCC'

MAC = MAC.replace(':','')
MAC = int(MAC, 16)
MAC = bin(MAC)

print(MAC)
print("\n")

########################################################### eighth task ##########################################################
IP = '192.168.3.1'

NEWIP = IP.split('.') # делаем список вида ['192', '168', '3', '1']
IP = '{:<8} {:<8} {:<8} {:<8}'.format(192, 168, 3, 1)
BINIP = '{:08b} {:08b} {:08b} {:08b}'.format(192, 168, 3, 1) 

print(IP)
print(BINIP)
print("\n")

#********************************************************* second options *********************************************************
ip_template = '''
{0:<8} {1:<8} {2:<8} {3:<6}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

print(ip_template.format(192, 168, 3, 1))


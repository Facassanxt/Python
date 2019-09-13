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
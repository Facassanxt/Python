# -*- coding: utf-8 -*-
'''
Задание 9.3a

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

'''
def get_int_vlan_map(config_filename):
    access = {}
    trunk = {}
    flag = False
    with open('C:\\Users\\Facassanxt\\Desktop\\Python\\9\\' + config_filename,'r') as f:
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
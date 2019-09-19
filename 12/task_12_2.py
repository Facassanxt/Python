# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''
import re
import subprocess
import ipaddress
def convert_ranges_to_ip_list(IP_list):
    list = []
    for ip in IP_list:
        if ip.find('-') != -1:
            ip = ip.split('-')
            try: 
                ip_1 = ipaddress.ip_address(ip[0])
                ip_2 = ipaddress.ip_address(ip[1])
                while ip_1 < ip_2:
                    ip_1 += 1
                    list.append(str(ip_1))
            except ValueError:
                for number in range(int(ip[1])):
                    list.append(str(ipaddress.ip_address(ip[0]) + number))
        else:
            list.append(ip)
    return list
def ping_ip_addresses(IP_list):
    list_up = []
    list_down = []
    for ip in IP_list:
        ping = subprocess.run(["ping", "-n", "1", ip]).returncode
        if ping == 0:
            list_up.append(ip)
        else:
            list_down.append(ip)
    tuple = (list_up,list_down)
    return tuple

if __name__ == "__main__":
    IP_list = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    print(ping_ip_addresses(convert_ranges_to_ip_list(IP_list)))
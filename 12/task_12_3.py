from tabulate import tabulate
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
def print_ip_table(Reachable,Unreachable):
    columns = ['Reachable', 'Unreacheble']
    return tabulate({columns[0]:Reachable, columns[1]:Unreachable}, headers='keys')

if __name__ == "__main__":
    IP_list = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132','192.168.0.0-3']
    Reachable,Unreachable = ping_ip_addresses(convert_ranges_to_ip_list(IP_list))
    print(print_ip_table(Reachable,Unreachable))



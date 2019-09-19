import subprocess
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
    IP_list = ['1.1.1', '8.8.8.8', '8.8.4.4', '8.8.7.1']
    print(ping_ip_addresses(IP_list))
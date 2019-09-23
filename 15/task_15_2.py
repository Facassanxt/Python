import re
def parse_sh_ip_int_br(file_name):
    with open('15\\' + file_name + '.txt','r') as f:
        list = []
        for line in f:
            find = re.search(r'^(\S+)\s+([\w.]+)[ \w]*(up|administratively down)\s+(\S+)$',line)
            if find:
                list.append(find.groups())
    return list
if __name__ == "__main__":
    print(parse_sh_ip_int_br('sh_ip_int_br'))
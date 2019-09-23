import re
headers = ['interface', 'address', 'status', 'protocol']
def convert_to_dict(headers,list):
    result = []
    dict = {}
    for param in list:
        for i, head in enumerate(headers):
            dict.update({head:param[i]})
        result.append(dict)
        dict = {}
    return result

def parse_sh_ip_int_br(file_name):
    with open('15\\' + file_name + '.txt','r') as f:
        list = []
        for line in f:
            find = re.search(r'^(\S+)\s+([\w.]+)[ \w]*(up|administratively down)\s+(\S+)$',line)
            if find:
                list.append(find.groups())
    return list
if __name__ == "__main__":
    print(convert_to_dict(headers,parse_sh_ip_int_br('sh_ip_int_br')))
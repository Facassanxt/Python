def parse_cdp_neighbors(command_output):
    flag = True
    with open('C:\\Users\\Facassanxt\\Desktop\\Python\\11\\sh_cdp_n_sw1.txt','r') as f:
        dict = {}
        for line in f:
            if line.find('show cdp neighbors') != -1:
                name = line.split('>')[0]
            elif line.find('Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID') != -1:
                flag = False
            elif flag == False:
                value = line.split()
                Local_Intrfce = value[1] + value[2]
                tuple1 = (name,Local_Intrfce)
                Device_ID = value[0]
                Port_ID = value[len(value)-2] + value[len(value)-1]
                tuple2 = (Device_ID,Port_ID)
                dict.update({tuple1:tuple2})
    return dict

if __name__ == "__main__":
    command_output = input()
    if command_output == 'show cdp neighbors':
        print(parse_cdp_neighbors(command_output))
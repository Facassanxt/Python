from draw_network_graph import draw_topology
def create_network_map(filenames):
    flag = True
    dict = {}
    for name_file in filenames:
        with open('11\\'+ name_file +'.txt','r') as f:
            for line in f:
                if line.find('show cdp neighbors') != -1:
                    name = line.split('>')[0]
                elif line.find('Device ID') != -1:
                    flag = False
                elif flag == False:
                    value = line.split()
                    Local_Intrfce = value[1] + value[2]
                    tuple1 = (name,Local_Intrfce)
                    Device_ID = value[0]
                    Port_ID = value[len(value)-2] + value[len(value)-1]
                    tuple2 = (Device_ID,Port_ID)
                    if name == 'SW1':
                        dict.update({tuple2:tuple1})
                    else:
                        dict.update({tuple1:tuple2})
        flag = True
    return dict


if __name__ == "__main__":
    command_output = input()
    if command_output == 'show cdp neighbors':
        filenames = ['sh_cdp_n_sw1','sh_cdp_n_r1','sh_cdp_n_r2','sh_cdp_n_r3']
        draw_topology(create_network_map(filenames))
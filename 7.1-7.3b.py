# from sys import argv

# f = open('7.1.txt')
# ospf_route = f.read()
# ospf_route = ospf_route.replace('O','OSPF').replace('[', '').replace(']', '').replace(',', '')
# RESULT = ospf_route.split(' ')
# print('Protocol:             ', RESULT[0])
# print('Prefix:               ', RESULT[1])
# print('AD/Metric:            ', RESULT[2])
# print('Next-Hop:             ', RESULT[4])
# print('Last update:          ', RESULT[5])
# print('Outbound Interface:   ', RESULT[6])
# print()
# f.close()

# ignore = ['duplex', 'alias', 'Current configuration']
# config_sw1 = open(argv[1] + '.txt')
# cleared = open(argv[2] + '.txt', 'w')
# for line in config_sw1:
#     result = list(set(ignore) & set(line[0:len(line)-1].split(' ')))
#     if line.startswith('!') or len(result) != 0:
#         continue
#     else:
#         print(line)
#         cleared.write(line)
# cleared.close()

CAM_table = open('7.3.txt')
Cam = CAM_table.read()
CAM_table.seek(Cam.find('Ports')+f.readline())
for line in CAM_table:
    print(line.rstrip())
    result = line.rstrip().split()
print(result)

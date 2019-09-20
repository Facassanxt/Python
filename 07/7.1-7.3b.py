from sys import argv
import os

for currentFolder, subFolders, fileNames in os.walk('.\\7'):
    print('В папке {} :\n\tСодержатся папки: {}\n\tСодержатся файлы: {}'.format(currentFolder,subFolders, fileNames))

f = open('7\\7.1.txt')
ospf_route = f.read()
ospf_route = ospf_route.replace('O','OSPF').replace('[', '').replace(']', '').replace(',', '')
RESULT = ospf_route.split(' ')
print('Protocol:             ', RESULT[0])
print('Prefix:               ', RESULT[1])
print('AD/Metric:            ', RESULT[2])
print('Next-Hop:             ', RESULT[4])
print('Last update:          ', RESULT[5])
print('Outbound Interface:   ', RESULT[6])
print()
f.close()

# ignore = ['duplex', 'alias', 'Current configuration']
# config_sw1 = open('7\\' + argv[1] + '.txt')
# cleared = open('7\\' + argv[2] + '.txt', 'w')
# for line in config_sw1:
#     result = list(set(ignore) & set(line[0:len(line)-1].split(' ')))
#     if line.startswith('!') or len(result) != 0:
#         continue
#     else:
#         print(line)
#         cleared.write(line)
# cleared.close()

phrase='10'
a = []
with open('7\\7.3.txt','r') as f:
    for (i, line) in enumerate(f):
        b = line.split(maxsplit=1)
        if len(b) != 0 and argv[1] == b[0]:
            a += line.rstrip().replace('  DYNAMIC  ','').split('\n')
if len(a)-1 >= 0:
    for i in range(len(a)-1):
        if a[i].split()[0] > a[i+1].split()[0]:
            c = a[i]
            a[i] = a[i+1]
            a[i+1] = c
        print(a[i])
    print(a[len(a)-1])
else:
    print('Не найдено')

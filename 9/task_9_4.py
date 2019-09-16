ignore = ['duplex', 'alias', 'Current configuration']

def convert_config_to_dict(config_filename):
    dict = {}
    value = []
    flag = False
    with open('C:\\Users\\Facassanxt\\Desktop\\Python\\9\\' + config_filename,'r') as f:
        for line in f:
            line = line.rstrip()
            if line == '' or line.find('!') != -1 or ignore_command(line,ignore) == True:
                continue
            else:
                if flag == False:
                    key = line
                    flag = True
                elif line[0] == ' ':
                    value.append(line[1:])
                else:
                    dict.update({key:value})
                    value = []
                    key = line
        dict.update({key:value})
    return dict
    
def ignore_command(command, ignore):
    return any(word in command for word in ignore)

if __name__ == "__main__":
    print(convert_config_to_dict('config_sw1.txt'))

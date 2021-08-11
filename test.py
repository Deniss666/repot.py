import os
import re
import shutil
import sys
from sys import argv, exit
from os import path

x = int()


print(argv[1])
put = path.abspath(argv[1])
put_origin = path.abspath(argv[1])
put_temp = path.abspath(argv[1].replace(".txt", "123.txt"))
put_new = path.abspath(argv[1].replace(".txt", "12.txt"))
shutil.copyfile(put, put_new)
cheks = []
temp = ''
numbs = []
newCheks = []

with open(put_origin, 'r') as rep:
    text = rep.readlines()
    for id, line in enumerate(text): #парсим
        if id > 2:
            rezult = re.split(r";", line)  #репорт
            del rezult[0:3]
            line = (";".join(rezult))
            if rezult[0] == '42':
                cheks.append(temp)        # на чеки
                temp = line


            elif rezult[0] == '64':  # Служебные операции
                cheks.append(temp)
                temp = line

            elif rezult[0] == '63':  # Служебные операции
                cheks.append(temp)
                temp = line
            elif rezult[0] == '60':  # Служебные операции
                cheks.append(temp)
                temp = line

            else:
                temp += line

        else:
            temp += line
    cheks.append(temp)
            # на чеки




for numb, ch in enumerate(cheks):
    if ch not in newCheks:
        newCheks.append(ch)
    else:
        numbs.append(numb)
       # print(numb)




temp = ''
cheks.clear()
newCheks.clear()
text = ''


with open(put_origin, "r") as rep:    #В этом куске не удаляется воремя и номер операции
    text = rep.readlines()
    for id, line in enumerate(text): #парсим
        if id > 2:
            rezult = re.split(r";", line)  #репорт
            if rezult[3] == '42':
                cheks.append(temp)        # на чеки
                temp = line
            elif rezult[3] == '64':  # Служебные операции
                cheks.append(temp)
                temp = line
            elif rezult[3] == '63':  # Служебные операции
                cheks.append(temp)
                temp = line
            else:
                temp += line
        else:
            temp += line
    cheks.append(temp)


for id, ch in enumerate(cheks):
    if id not in numbs:
        if ch.strip():
            newCheks.append(ch)

with open(put_temp, 'w') as f:
    for ch in newCheks:

        f.write(ch)
# Здесь в массиве ньючекс удалены задвойки
temp = ''
cheks.clear()
newCheks.clear()
text = ''
ch = ''
with open(put_temp, 'r') as rep:
    text = rep.readlines()
    checkN = int((re.split(r";", text[3]))[5])
    for id, line in enumerate(text): #парсим
        if id > 3:
            rezult = re.split(r";", line)  #репорт
            line = (";".join(rezult))
            if int(rezult[5]) == checkN:
                temp += line
                #print('line  \n',  temp)
                #print('numb ', checkN)
                #print('rezult[5] ', rezult[5])

                # на чеки
            if int(rezult[5]) > checkN:
                cheks.append(temp)
                temp = ''
                temp += line
                checkN += 1
        else:
            temp += line

    cheks.append(temp)
    checkN += 1


#os.remove(put_temp)

for numb, ch in enumerate(cheks):
    if ch not in newCheks:
        newCheks.append(ch)
    else:
        numbs.append(numb)
       #print(numb, '\n', ch)

with open(put, "w") as f:
    for ch in newCheks:
        if ch.strip():
            f.write(ch)

#sys.exit(1)

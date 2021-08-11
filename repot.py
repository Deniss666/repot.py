import re

x = int()

cheks = []
temp = ''
numbs = []
newCheks = []
with open('report.txt', 'r') as rep:
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

            else:
                temp += line

        else:
            temp += line
    cheks.append(temp)
            # на чеки




for numb, ch in enumerate(cheks):
    if ch not in newCheks:
        newCheks.append(ch)
        print(numb, '\n', ch)
    else:
        numbs.append(numb)
        print(numb, '\n', ch)




temp = ''
cheks.clear()
newCheks.clear()
text = ''


with open("report.txt", "r") as rep:
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


with open("report123.txt", "w") as f:
    for id, ch in enumerate(cheks):
        if id not in numbs:
            if ch.strip():
                f.write(ch)



temp = ''
cheks.clear()
newCheks.clear()
text = ''
ch = ''
with open('report123.txt', 'r') as rep:
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
            if int(rezult[5]) == (checkN + 1):
                cheks.append(temp)
                temp = ''
                temp += line
                checkN += 1
            if int(rezult[5]) == (checkN + 2):
                cheks.append(temp)
                temp = ''
                temp += line
                checkN += 2
        else:
            temp += line

    cheks.append(temp)
    checkN += 1

for numb, ch in enumerate(cheks):
    if ch not in newCheks:
        newCheks.append(ch)
    else:
        numbs.append(numb)
        #print(numb, '\n', ch)

with open("report12.txt", "w") as f:
    for ch in newCheks:
        if ch.strip():
            f.write(ch)
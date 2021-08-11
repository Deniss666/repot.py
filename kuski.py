while True:
    line = rep.readline()
    result = re.split(r';', line)
    if result[3] == '42':
        cheks[0].append(line)
    if not line:
        break

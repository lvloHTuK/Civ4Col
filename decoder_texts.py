def decode(name: str):
    name = name.encode('windows-1251')
    data = ""
    for i in name:
        if i > 127:
            data += "&#"
            data += str(i)
            data += ";"
        else:
            data += chr(i)
        # data += "&#" + str(i) + ";"

    return data


def encode(name: str):
    data = []
    i = 0
    while i < len(name):
        if name[i] == '&':
            if name[i + 1] == '#':
                j = i + 2
                while name[j] != ';':
                    j += 1
                data.append(int(name[i + 2:j]))
                i = j
        else:
            data.append(ord(name[i]))
        i += 1


print(decode('Удваивает скорость'))

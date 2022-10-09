cnt = 0
while True:
    str = input()
    if (str.lower() == 'stop'):
        break
    if cnt == 0:
        minlen = maxlen = len(str)
        maxstr = minstr = str
    # pdb.set_trace()
    if minlen > len(str):
        minstr = str
        minlen = len(str)
    if maxlen < len(str):
        maxstr = str
        maxlen = len(str)
    cnt += 1

print(maxstr, minstr)

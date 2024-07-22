flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽"
for i in range(0, len(flag), 2):
    print(''.join [chr((ord(flag[i]) << 8) + ord(flag[i + 1]))])

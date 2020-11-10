s = "10#11#12"

s = s[::-1]
print(s)
while s.replace('#', '')[0].isnumeric():
    if s[0] == '#':
        s = s + chr(int(s[2] + s[1]) + 96)
        s = s[3::]
        print(s)
    else:
        s = s + chr(int(s[0]) + 96)
        s = s[1::]
        print(s)
s = s[::-1]
print(s)
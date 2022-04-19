def move(com):
    if com == 1:
        tmp = status[0]
        status[0] = status[3]
        status[3] = status[2]
        status[2] = status[1]
        status[1] = tmp
    if com == 2:
        tmp = status[0]
        status[0] = status[1]
        status[1] = status[2]
        status[2] = status[3]
        status[3] = tmp
    if com == 3:
        tmp = status[0]
        status[0] = status[4]
        status[4] = status[2]
        status[2] = status[5]
        status[5] = tmp
    if com == 4:
        tmp = status[0]
        status[0] = status[5]
        status[5] = status[2]
        status[2] = status[4]
        status[4] = tmp

n, m, x, y, command = input().split()
m = int(m)
n = int(n)
x = int(x)
y = int(y)
command = int(command)

s = []
for i in range(int(n)):
    s.append(list(map(int, input().split())))
com = list(map(int, input().split()))

status = [0,0,0,0,0,0]

for i in com:
    if i == 1: #동
        if y == m-1:
            continue
        move(i)
        y += 1
        if s[x][y] == 0:
            s[x][y] = status[2]
        else:
            status[2] = s[x][y]
            s[x][y] = 0

    if i == 2 : #서
        if y == 0:
            continue
        move(i)
        y -= 1
        if s[x][y] == 0:
            s[x][y] = status[2]
        else:
            status[2] = s[x][y]
            s[x][y] = 0

    if i == 3: #북
        if x == 0:
            continue
        move(i)
        x -= 1
        if s[x][y] == 0:
            s[x][y] = status[2]
        else:
            status[2] = s[x][y]
            s[x][y] = 0

    if i == 4:
        if x == n-1:
            continue
        move(i)
        x += 1
        if s[x][y] == 0:
            s[x][y] = status[2]
        else:
            status[2] = s[x][y]
            s[x][y] = 0

    print(status[0])



#북 0 동 1 남 2 서 3
N, M = map(int, input().split())
r, c, d = map(int, input().split())
out =0
motion = 1

def spin():
    global d
    if d == 0:
        d = 3
    elif d == 1:
        d = 0
    elif d == 2:
        d = 1
    elif d == 3:
        d = 2

def go_back():
    global d
    global r
    global c
    global out
    global motion

    if d == 0:
        if s[r+1][c] == 1:
            motion = 0
        if r != N-1:
            r += 1
    if d == 1:
        if s[r][c-1] == 1:
            motion = 0
        if c != 0:
            c -= 1
    if d == 2:
        if s[r-1][c] == 1:
            motion = 0
        if r != 0:
            r -= 1
    if d == 3:
        if s[r][c+1] == 1:
            motion = 0
        if c != M-1:
            c += 1
    out = 0

def go_and_clear():
    global d
    global r
    global c
    global out

    out = 0
    if d == 0:
        if r-1 != 0:
            r -= 1
            s[r][c] = 2
    if d == 1:
        if c+1 != M-1:
            c += 1
            s[r][c] = 2
    if d == 2:
        if r+1 != N-1:
            r += 1
            s[r][c] = 2
    if d == 3:
        if c-1 != 0:
            c -= 1
            s[r][c] = 2

def run():
    global d
    global r
    global c
    global out
    global motion

    if d == 0:
        if c-1>=0:
            if s[r][c-1] == 0:
                spin()
                go_and_clear()
            else:
                spin()
                out += 1
                if out >= 8:
                    go_back()
    elif d == 1:
        if r-1>=0:
            if s[r-1][c] == 0:
                spin()
                go_and_clear()
            else:
                spin()
                out += 1
                if out >= 8 :
                    go_back()
    elif d == 2:
        if c+1<M:
            if s[r][c+1] == 0:
                spin()
                go_and_clear()
            else:
                spin()
                out += 1
                if out >= 8:
                    go_back()
    elif d == 3:
        if r+1<N:
            if s[r+1][c] == 0:
                spin()
                go_and_clear()
            else:
                spin()
                out += 1
                if out >= 8:
                    go_back()

s = []
for i in range(N):
    s.append(list(map(int,input().split())))

s[r][c] = 2

while motion == 1:
    run()

cnt = 0
for i in range(len(s)):
    for j in range(len(s[0])):
        if s[i][j] == 2:
            cnt += 1

# for i in range(len(s)):
#     print(s[i])
print(cnt)


# 0의 개수 반환
import copy
from collections import deque

def bfs():
    virus = []
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 2:
                tmp = []
                tmp.append(i)
                tmp.append(j)
                virus.append(tmp)

    dq = deque(virus)
    while(len(dq)):
        cur_pos = dq[-1]
        dq.pop()

        if cur_pos[0]+1 < N:
            if s[cur_pos[0]+1][cur_pos[1]] == 0:
                s[cur_pos[0] + 1][cur_pos[1]] = 2
                tmp = [cur_pos[0]+1, cur_pos[1]]
                # print("deque append : ", tmp)
                dq.append(tmp)
        if cur_pos[0]-1 >= 0:
            if s[cur_pos[0]-1][cur_pos[1]] == 0:
                s[cur_pos[0]-1][cur_pos[1]] = 2
                tmp = [cur_pos[0]-1, cur_pos[1]]
                # print("deque append : ", tmp)
                dq.append(tmp)
        if cur_pos[1]+1 < M:
            if s[cur_pos[0]][cur_pos[1]+1] == 0:
                s[cur_pos[0]][cur_pos[1]+1] = 2
                tmp = [cur_pos[0], cur_pos[1]+1]
                # print("deque append : ", tmp)
                dq.append(tmp)
        if cur_pos[1]-1 >= 0:
            if s[cur_pos[0]][cur_pos[1]-1] == 0:
                s[cur_pos[0]][cur_pos[1]-1] = 2
                tmp = [cur_pos[0], cur_pos[1]-1]
                # print("deque append : ", tmp)
                dq.append(tmp)

        # print(dq)

def count_zero(li):
    cnt = 0
    for i in range(len(li)):
        for j in range(len(li[0])):
            if li[i][j] == 0:
                cnt += 1
    return cnt

# 값 입력
N, M = map(int, input().split())

s = []
for i in range(N):
    s.append(list(map(int, input().split())))

# 좌표값 0인 점들 저장하기
zero_pos = []
for i in range(N):
    for j in range(M):
        if s[i][j] == 0:
            tmp = []
            tmp.append(i)
            tmp.append(j)
            zero_pos.append(tmp)

# combination
combinate = []
for i in range(len(zero_pos)-2):
    for j in range(i+1, len(zero_pos)-1):
        for k in range(j+1, len(zero_pos)):
            tmp = []
            tmp.append(zero_pos[i])
            tmp.append(zero_pos[j])
            tmp.append(zero_pos[k])
            combinate.append(tmp)

# 바이러스 전염시키기
s_tmp = copy.deepcopy(s)
# print(s_tmp)
max_zero = 0

for a in range(len(combinate)):
    s[combinate[a][0][0]][combinate[a][0][1]] = 1
    s[combinate[a][1][0]][combinate[a][1][1]] = 1
    s[combinate[a][2][0]][combinate[a][2][1]] = 1

    bfs()

    max_zero = max(max_zero, count_zero(s))

    s = []
    s = copy.deepcopy(s_tmp)
print(max_zero)


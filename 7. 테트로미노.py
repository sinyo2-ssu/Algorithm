tetrominos = []
tet1_1 = [[1,1,1,1]]
tetrominos.append(tet1_1)
tet1_2 = [[1],[1],[1],[1]]
tetrominos.append(tet1_2)
tet2_1 = [[1,1],[1,1]]
tetrominos.append(tet2_1)
tet3_1 = [[1,0],[1,0],[1,1]]
tetrominos.append(tet3_1)
tet3_2 = [[0,0,1],[1,1,1]]
tetrominos.append(tet3_2)
tet3_3 = [[1,1],[0,1],[0,1]]
tetrominos.append(tet3_3)
tet3_4 = [[1,1,1],[1,0,0]]
tetrominos.append(tet3_4)
tet4_1 = [[1,0],[1,1],[0,1]]
tetrominos.append(tet4_1)
tet4_2 = [[0,1,1],[1,1,0]]
tetrominos.append(tet4_2)
tet5_1 = [[1,1,1],[0,1,0]]
tetrominos.append(tet5_1)
tet5_2 = [[0,1],[1,1],[0,1]]
tetrominos.append(tet5_2)
tet5_3 = [[0,1,0],[1,1,1]]
tetrominos.append(tet5_3)
tet5_4 = [[1,0],[1,1],[1,0]]
tetrominos.append(tet5_4)

N, M = map(int, input().split())

s = []
for i in range(N):
    s.append(list(map(int,input().split())))

print(tetrominos)
answer = 0
for tetro_idx in range(len(tetrominos)):
    for i in range(N-len(tetrominos[tetro_idx])+1):
        for j in range(M-len(tetrominos[tetro_idx][0])+1):
            tmp = 0
            for a in range(i,i+len(tetrominos[tetro_idx])):
                for b in range(j,j+len(tetrominos[tetro_idx][0])):
                    
                    tmp += s[a][b]
            print(" ")
            answer = max(answer, tmp)
print(answer)






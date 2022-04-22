def to_decimal(li):
    for i in range(len(li)):


T= int(input())

for i in range(T):
    N, K = map(int, input().split())
    S = list(input())
    li_1 = S[0:int(N / 4)]
    li_2 = S[int(N / 4): int(N/4) * 2]
    li_3 = S[int(N / 4) * 2 : int(N / 4) * 3]
    li_4 = S[int(N / 4) * 3 : int(N / 4) * 4]

    for j in range(int(N/4)):


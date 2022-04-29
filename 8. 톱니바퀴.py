# def compare_right(arr1, arr2):
#     if arr1[2] == arr2[6]:
#         return True
#     else:
#         return False
#
# def compare_left(arr1, arr2):
#     if arr1[6] == arr2[2]:
#         return True
#     else:
#         return False
#
# def spin_clock(arr):
#     tmp = arr[7]
#     del(arr[7])
#     arr.insert(0,tmp)
#
# def spin_unclock(arr):
#     tmp = arr[0]
#     del(arr[0])
#     arr.append(tmp)
#
# def do_spin(arr1, arr2, arr3, arr4, spin_w, direction):
#     if spin_w == 1:
#         if compare_right(arr1,arr2):
#             if direction == 1:
#                 spin_clock(arr1)
#                 spin_unclock(arr2)
#                 if compare_right(arr2,arr3):
#                     spin_clock(arr3)
#                     if compare_right(arr3, arr4):
#                         spin_unclock(arr4)
#                     else:
#                         return
#                 else:
#                     return
#             else:
#                 return
#         else:
#             return
#
#
# w1 = list(map(int, input().split()))
# w2 = list(map(int, input().split()))
# w3 = list(map(int, input().split()))
# w4 = list(map(int, input().split()))
#
# K = int(input())
# s = []
# for i in range(K):
#     s.append(list(map(int, input().split())))
#
# print(w1)
# print(w2)
# print(w3)
# print(w4)

from collections import deque
def rotate(a,array):
    temp = [0]*8
    if a == -1: #반시계방향
        temp[7] = array[0]
        for i in range(1,len(array)):
            temp[i-1] = array[i]
    if a == 1: #시계방향
        temp[0] = array[7]
        for i in range(len(array)-1):
            temp[i+1] = array[i]
    return temp


score = [1,2,4,8]
topni = []


for _ in range(4):
    topni.append(list(map(int,input())))
k = int(input())

def check(a,dir):
    rotate_list = []
    visitied = [False]*4
    queue = deque()
    queue.append((a-1,dir))
    visitied[a-1] = True
    rotate_list.append((a-1,dir))
    while queue:
        x,dir = queue.popleft()
        #왼쪽톱니바퀴와 맞닿을때
        nx = x-1
        if (0<=nx<4 and topni[nx][2] != topni[x][6] and not visitied[nx]):
            queue.append((nx,-dir))
            rotate_list.append((nx,-dir))
            visitied[nx] = True
        #오른쪽 톱니바퀴와 맞닿을때
        nx = x+1
        if(0<=nx<4 and topni[nx][6] != topni[x][2] and not visitied[nx]):
            queue.append((nx,-dir))
            rotate_list.append((nx,-dir))
            visitied[nx] = True
    return rotate_list

for _ in range(k):
    number,direc = map(int,input().split())
    rotate_list= check(number,direc)
    for i,j in rotate_list:
        topni[i] = rotate(j,topni[i])


sum = 0
for i in range(len(topni)):
    if topni[i][0] == 0:
        sum+=0
    if topni[i][0] == 1:
        sum+=score[i]
print(sum)
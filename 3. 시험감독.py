N = int(input())
arr = list(map(int, input().split()))
Master, Sub = map(int, input().split())

cnt = len(arr)
for i in range(len(arr)):
    arr[i] -= Master
    if arr[i] <= 0:
        continue
    else:
        if arr[i] % Sub == 0:
            cnt += int(arr[i] / Sub)
        else :
            cnt += int((arr[i] / Sub))
print(cnt)


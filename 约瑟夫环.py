a = []
n = int(input("n:"))
for i in range(1, n + 1):
    a.append(i)
i = 0  # 当前位置
j = 0  # 报的数
k = 0  # 删掉个数
while k <= n - 2:
    if a[i] != 0: j += 1
    if j == 3:
        a[i] = 0
        k += 1
        j = 0
    i += 1
    if i == n:
        i = 0
print(a)
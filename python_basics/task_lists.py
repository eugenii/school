# 1
# a = [int(i) for i in input().split()]
# b = len([i for i in a if i % a[0] == 0])
# c = len([i for i in a if i > sum(a) / len(a)])
# print(b, c)

# 2
data = ['a', 'b', 'c', 'x']
# count = int(input())
out = []
for i in range(int(input())):
    out.append(data[i % len(data)])
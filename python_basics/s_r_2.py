# # 6.2
# n = int(input())
# num = 1
# while num <= n:
#     print(num)
#     num += 1
#     
# # 6.3
# num = 10
# while num <= 100:
#     if num % 2 != 0:
#         print(num)
#     num += 1
# 
# # print(*[i for i in range(11, 100, 2)], end="\n")
# # 6.4
# num = 191
# while num % 17 != 0:
#     num += 1
# print(num)

# 6.5
num = 139
c = 1
while c * num <= 5000:
    c += 1
print((c - 1) * num)

# 6.6
fact = int(input())
n = 2
while fact // n != 1:
    fact //= n
    n += 1
print(n)

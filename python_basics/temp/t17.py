# 1_16
# def F(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return F(n - 1) + F(n - 2)
# 
# print(F(17))

# 1_17
# 
# out = []
# for i in range(1316, 9965):
#     A = (i % 3 != 0)
#     B = (i % 7 != 0)
#     C = (i % 11 != 0)
#     D = (i % 25 != 0)
#     if i % 5 == 0 and A and B and C and D:
#         out.append(i)
# print(len(out), max(out))

# 1_22
# stop = 0
# x = 1
# 
#     L = 94; M = 0
#     while L >= x:
#         M += 1
#         L -= x
#     if M < L:
#         x = M
#         M = L
#         L = x
#     if L == 3 and M == 7:
#         stop = x
#         break
# print(x)

# 1_24
# f = open("24-01.txt")
# data = f.read().strip()
# #  data = "abcccda"
# max_len = 0
# temp = 1
# for i in range(len(data) - 1):
#     if data[i + 1] == data[i]:
#         temp += 1
#     else:
#         if max_len < temp:
#             max_len = temp
#         temp = 1
# print(max_len)

# 1_25

for i in range(150_000, 200_001):
    delit = []
    for j in range(2, int(i ** 0.5)):
        if i % j == 0:
            delit.append(j)
            delit.append(i // j)
        if len(delit) > 48:
            break
    if len(delit) == 48:
        print(delit)
        print(max(delit))
        

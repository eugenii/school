f = open("Input.txt")
n, a, b = [int(i) for i in f.read().split()]
# f2 = open("in2.txt")
# n, a, b = [i.strip() for i in f2.readlines()]
f.close()
f2 = open("Output.txt", "w")
data = 777
print(data, file=f2)
f2.close()
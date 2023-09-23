x = int(input())

# integer11
a = x // 100
b = x % 100 // 10
c = x % 10
print(a + b + c, a * b * c, sep="\n")

# integer12

print(c * 100 + b * 10 + a)

# integer13

print(b *100 + c * 10 + a)

# integer14

print(c * 100 + a * 10 + b)

# integer15

print(b * 100 + a * 10 + c)

# integer16

print(a * 100 + c * 10 + b)

# if1

if x > 0:
    print(x + 1)
else:
    print(x)
    
# if2

if x > 0:
    print(x + 1)
else:
    print(x - 2)
    
# if3

if x > 0:
    print(x + 1)
elif x < 0:
    print(x - 2)
else:
    print(10)

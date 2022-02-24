a, b = input().split()

for i in range(len(a)):
    if a[i] in b:
        a_pin = i
        b_pin = b.find(a[i])
        break

for j in range(len(b)):
    if j == b_pin:
        print(a)
    else:
        print("." * a_pin + b[j] + "." * (len(a)-a_pin-1))
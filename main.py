i = 0
for i in range(0, 4):
    x = int(input("x = "))
    print("x =", f"{x:>3}")
    print("x =", "{0:3d}".format(x))
    print("x =", "%3d" % x)
    i += 1
input()

i = 0
for i in range(0, 2):
    x = float(input("x = "))
    print("x =", f"{x:>9f}")
    print("x =", "{0:9f}".format(x))
    print("x =", "%9f" % x)
input()

i = 0
for i in range(0, 2):
    x = float(input("x = "))
    print("x =", f"{x:5.2f}")
    print("x =", "{0:5.2f}".format(x))
    print("x =", "%5.2f" % x)
input()

s = input("Input string: ")
print(f"{s:.3s}")
print("{0:.3s}".format(s))
print("%.3s" % s)

b = False
print(f"{b:}")
print("{0:}".format(b))
print("%s" % b)
input()

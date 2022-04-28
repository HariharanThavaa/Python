# P1
# x = input("What's x? ")
# y = input("What's y? ")
#
# z = int(x) + int(y)
#
# print(z)

# P2
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# print(x + y)

# P3
# print(int(input("What's x? ")) + int(input("What's y? ")))

# P4 with float
# x = float(input("What's x? "))
# y = float(input("What's y? "))
#
# print(x + y)

# P5 Round
# x = float(input("What's x? "))
# y = float(input("What's y? "))
#
# z = round( x + y)
#
# print(f"{z:,}")


# P6 Division with round
# x = float(input("What's x? "))
# y = float(input("What's y? "))
#
# z = round(x / y, 2)
#
# print(z)

# # P7 Division with format
# x = float(input("What's x? "))
# y = float(input("What's y? "))
#
# z = x / y
#
# print(f"{z:.2f}")


def main():
    x = int(input("What's x? "))
    print("x squared is ", square(x))


def square(n):
    return n * n


main()





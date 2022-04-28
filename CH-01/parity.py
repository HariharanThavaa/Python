x = int(input("What's x? "))


def main():
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0
    # P2
    # return True if n % 2 == 0 else False
    # P1
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False


main()

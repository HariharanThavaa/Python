# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")

def main():
    # print_column(5)
    # print_row(4)
    print_square(3)


def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


def print_column(height):
    for _ in range(height):
        print("#")


def print_row(width):
    for _ in range(width):
        print("?", end="")


main()

# # Ask user for the name
# # Remove the whitespace from str
# # Capitalise user's name
# name = input("What's your name? ").strip().title()
#
# # Say Hello to user
# print(f"hello, {name}")


# Say Hello to user
# print("hello, " + name)

# print("hello, ", end='')
# print('\"'+name+'\"')

# P3
# def hello(to="world"):
#     # Say Hello to user
#     print("hello, " + to)
#
# # Ask user for the name
# # Remove the whitespace from str
# # Capitalise user's name
# name = input("What's your name? ").strip().title()
#
# hello()
# hello(name)


# P4
def hello(to="world"):
    # Say Hello to user
    print("hello, " + to)

name = input("What's your name? ").strip().title()

hello()
hello(name)



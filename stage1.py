friends_dict = {}

friends = int(input("Enter the number of friends joining (including you):\n"))

if friends >= 1:
    print("\nEnter the name of every friend (including you), each on a new line:")

    for i in range(friends):
        friends_dict[input()] = 0

    print()
    print(friends_dict)
else:
    print("\nNo one is joining for the party")

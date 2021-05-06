list_of_friends = []
friends_dict = {}

friends = int(input("Enter the number of friends joining (including you):\n"))

if friends >= 1:
    print("\nEnter the name of every friend (including you), each on a new line:")

    for i in range(friends):
        list_of_friends.append(input())

    print("\nEnter the total bill value:")
    bill = int(input())

    friends_dict = dict.fromkeys(list_of_friends, round(bill / friends, 2))

    print()
    print(friends_dict)
else:
    print("\nNo one is joining for the party")

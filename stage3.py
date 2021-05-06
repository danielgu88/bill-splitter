import random

list_of_friends = []

friends = int(input("Enter the number of friends joining (including you):\n"))

if friends >= 1:
    print("\nEnter the name of every friend (including you), each on a new line:")

    for i in range(friends):
        list_of_friends.append(input())

    print("\nEnter the total bill value:")
    bill = int(input())

    print("\nDo you want to use the \"Who is lucky?\" feature? Write Yes/No:")
    use_feature = input()

    if use_feature == "Yes":
        random.seed()
        print("\n{} is the lucky one!".format(list_of_friends[random.randint(0, friends - 1)]))
    else:
        print("\nNo one is going to be lucky")
else:
    print("\nNo one is joining for the party")

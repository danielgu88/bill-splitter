import random

list_of_friends = []
friends_dict = {}

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
        lucky_one = list_of_friends[random.randint(0, friends - 1)]
        print("\n{} is the lucky one!".format(lucky_one))

        friends_dict = dict.fromkeys(list_of_friends, round(bill / (friends - 1), 2))
        friends_dict[lucky_one] = 0
    else:
        print("\nNo one is going to be lucky")

        friends_dict = dict.fromkeys(list_of_friends, round(bill / friends, 2))

    print()
    print(friends_dict)
else:
    print("\nNo one is joining for the party")

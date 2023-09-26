userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply=="yes":
    print("we can help you ship that package!")
else:
    print("Please come back when you need to ship a package. thank you.")
userReply=input("Would you like to buy stamps, buy an envelop, or make a copy?(enter stamps, envelope,or copy)")
if userReply=="stamps":
    print("we have many stamp desings to choose from")
elif userReply=="envelope":
    print("we have many envelope sizes to choose from.")
elif userReply=="copy":
    copies=input("how many copies would you like ?(enter a number)")
    print("her are {} copies.".format(copies))
else:
    print("thank you, please come again.")
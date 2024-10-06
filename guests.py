from random import randrange as rand_numb

def start_program():
    guests = ['name1', 'name2', 'name3']
    
    # print(rand_numb(0, len(guests)))
    
    # for guest in guests:  
    #     message = f"""Hi, {guest}
    # I want to invite you to lunch...
    # Kostisntyn
    # """
    #     print(message)

    # will_not_come = 'name2'
    # print(will_not_come)
    # guests = ["name8" if guest == "name2" else guest for guest in guests]
    # print(guests)

    def new_guest(guests, name):
        print(name)
        print(guests)
        for guest in guests:
            if guest == 'name2':
                guests[guests.index(guest)] = name

    new_guest(guests, 'Alfred')
    print(guests)

    extra_friends = 3

    print("I decided to add 3 more friends.")
    while extra_friends != 0:
        if rand_numb(0, len(guests)) == 0:
            guests.insert(0, (input("Extra guest: ")))
        elif rand_numb(0, len(guests)) >= 1 and rand_numb(0, len(guests)) <= len(guests):
            guests.insert(int((len(guests)/2)), (input("Extra guest: ")))
        else:
            guests.append((input("Extra guest: ")))

        extra_friends -= 1
    print(guests)

    for guest in guests:
        message = f"""Hi, {guest.title()}
        I want to invite you to lunch...
        Kostisntyn
        """
        
        print(message)

    guests_not_come = []

    while len(guests) != 2:
        guests_not_come.append(guests.pop(rand_numb(0, len(guests))))

    print(guests)
    print(guests_not_come)
    for guest in guests_not_come:
        message = f"""
        Hi {guest},
    
        Sorry, I had a problem with ordering a large table.
        My new table won't arrive until next week, so I canceled lunch on this week.
        This week I will have lunch with only two people: {guests[0]}, {guests[1]}.
    
        Kostiantyn
        """
        print(message)

    print(guests)
    print(len(guests))

    del guests[:]

    print(guests)

try:
    start_program()
# except ValueError and SyntaxError and NameError:
except NameError:
    print("Something wrong!")
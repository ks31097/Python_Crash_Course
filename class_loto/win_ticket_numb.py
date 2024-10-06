from class_loto import WinTicket

ticket = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'F', 'A', 'H', 'O', 'T')

def loto_function(WinTicket, ticket):
    my_ticket = WinTicket(ticket)
    win_ticket = my_ticket.win_ticket_number()
    print(f"Win ticket number: {win_ticket}")

    numb = 0
    while True:
        result = my_ticket.win_ticket_number()
        # breakpoint()
        numb += 1
        if result == win_ticket: 
            break

    print(f"Checking a number ticket: {result}")
    print(f"The found combination has the number: {numb}")

try:
    loto_function(WinTicket, ticket)
except:
    print("Something is wrong! Check the program!")

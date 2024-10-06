from random import choice

class WinTicket():
    def __init__(self, values):
        self.ticket = values
        self.random_value = []

    def win_ticket(self):
        self.random_value.clear()
        for _ in range(5):
            self.random_value.append(choice(self.ticket))
        
        return self.random_value

    def win_ticket_number(self):
        self.win_ticket()
        win_ticket_number = ''.join(str(_) for _ in self.random_value)
        return win_ticket_number
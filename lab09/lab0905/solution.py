def SeatType():
    while True:
        s = input("Select the seat type (P or D or H): ").lower();
        if s in ["p", "d", "h"]:
            return s
        print("Wrong seat type! Please select again.")
def MovieType():
    while True:
        m = input("Select the movie type (1 or 2): ");
        if m in ["1", "2"]:
            return m
        print("Wrong movie type! Please select again.")


def TicketPrice(s, m):
    m = int(m) - 1 
    s = s.lower()
    price = {
        "p": [100, 120],
        "d": [140, 200],
        "h": [400, 500]
    }
    print("The ticket price is", price[s][m])

S = SeatType()
M = MovieType()
TicketPrice(S, M)
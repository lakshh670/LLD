class Movie():
    movie_name:str
    total_tickets:int
    ticket_price:int
    booked_seats:int
    def __init__(self,name:str,total_tickets:int,ticket_price:int):
        self.movie_name=name
        self.total_tickets=total_tickets
        self.ticket_price=ticket_price
        self.booked_seats=0

    def book_tickets(self):

        print(f"Welcome to the booking counter.\n"
              f"Movie name: {self.movie_name}\n"
              f"Tickets available: {self.total_tickets}\n"
              f"Ticket price: {self.ticket_price}")
        self.no_of_seats=int(input("Please enter the number of seats you want to book"))
        if self.no_of_seats>self.total_tickets:
            print("Sorry, you cannot book more seats than we have.")
            return
        print("Tickets have been booked.")
        self.booked_seats+=self.no_of_seats
        self.total_tickets-=self.no_of_seats
        print(f"Please pay Rs {self.no_of_seats*self.ticket_price}")

    def status(self):
        print(f"Movie name: {self.movie_name}\n"
              f"Tickets available: {self.total_tickets}\n"
              f"Ticket price: {self.ticket_price}\n"
              f"Booked seats: {self.booked_seats}\n")
m1=Movie("Dark Knight",150,100)
m1.book_tickets()
m1.status()


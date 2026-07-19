from random import randint
class train:
    def __init__(self,train_number):
        self.train_number=train_number
    def book_ticket(self,from_station,to_station):
        print(f"Ticket booked for train {self.train_number} from {from_station} to {to_station}")
    def seat_availability(self,from_station,to_station):
        print(f"Seat availability for train {self.train_number}  from {from_station} to {to_station} have 10 remaining seats")
    def fare_info(self,from_station,to_station):
        print(f"fare of train {self.train_number} from {from_station} to {to_station} is {randint(222, 6466)}")
t= train(764634)
t.book_ticket("lahore","karachi")
t.fare_info("lahore","karachi")
t.seat_availability("lahore","karachi")

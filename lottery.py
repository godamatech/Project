import string as s
from random import choices

print("================ Lottery ticket =====================")

def lottery_ticket_generator():
    # my_list = [0,1,2,3,4,5,6,7,8,9,'A','B','D','U','L']
    my_list = list(s.digits)
    my_list.extend(['A','B','D','U','L'])
    
    random_list = "".join(choices(my_list,k=4))
    return random_list

print(f"Any ticket matching these four numbers or letters wins a prize: {lottery_ticket_generator()}")
print()


print("================ Lottery Analysis =====================")
my_ticket = 'AB10'
counter = 0
while lottery_ticket_generator() != my_ticket:
    counter += 1
print(f"It loops {counter} times to win the Ticket")
print()

from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        generated_num=randint(1, self.sides)
        return generated_num
    

die = Die()

print("=================    6 Sided Die =================")
for d in range(10):
    print(die.roll_die())

print("=================    10 Sided Die =================")
die = Die(10)
for d in range(10):
    print(die.roll_die())


print("=================    20 Sided Die =================")
die = Die(20)
for d in range(10):
    print(die.roll_die())

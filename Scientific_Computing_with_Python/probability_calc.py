import copy
import random


class Hat():

    def __init__(self, **balls):

        self.balls = balls
        self.contents = []

        for color, quantity in self.balls.items():
            for quantity in range(quantity):
                self.contents.append(color)

    def __str__(self):

        hat_string = ""

        for color, quantity in self.balls.items():
            hat_string += "{}={}, ".format(color, quantity)

        return f"{type(self).__name__}({hat_string.rstrip(', ')})"

    def draw(self, quantity): # VER

        if quantity >= len(self.contents):
            return self.contents
        else:
            drawn_balls = []
            complete_hat = copy.deepcopy(self.contents)
            while len(drawn_balls) < quantity:

                position = random.randint(0, len(self.contents))
                drawn_balls.append(complete_hat.pop(position))

            return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    full_hat = copy.deepcopy(hat.contents)
    success_events = 0

    for experiment in range(num_experiments):

        drawn_balls = hat.draw(num_balls_drawn)
        drawn_balls_dict = {color: drawn_balls.count(color)
                       for color in set(drawn_balls)}
        print(drawn_balls)
        print(drawn_balls_dict)


hat1 = Hat(yellow=4, red=5)

print(hat1)
print(hat1.contents)

experiment(hat1, {'red':2, 'yellow':4}, 7, 1) # no esta funcionando. falla la funcion draw
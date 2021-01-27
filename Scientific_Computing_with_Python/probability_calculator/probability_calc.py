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

    def draw(self, quantity):

        drawn_balls = []

        if quantity >= len(self.contents):
            drawn_balls = self.contents
        else:
            while len(drawn_balls) < quantity:
                position = random.randint(0, len(self.contents) - 1)
                drawn_balls.append(self.contents.pop(position))

        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    event_flag = 1  # 1: success, 0: failed
    success_events = 0

    for experiment in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        drawn_balls = experiment_hat.draw(num_balls_drawn)

        for color in expected_balls.keys():
            if drawn_balls.count(color) >= expected_balls[color]:
                continue
            else:
                event_flag = 0
                break

        if event_flag == 1:
            success_events += 1
        else:
            event_flag = 1
            continue

    return success_events / num_experiments


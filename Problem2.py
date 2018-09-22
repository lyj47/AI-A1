"""
V1.0
"""

"""
The state space consists of 3 states containing the water amount for each 7, 4, and 3 liter jugs.

You shouldn't pour more than 4 liters of water into the 4 liter jug, and 3 liters for the 3 liter jug.
"""

from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search

class Problem2(Problem):

    # Seven liter, Four liter, Three liter
    S = 0; F = 1; T = 2


    tempS = self.initial[S]; tempF = self.initial[F]; tempT = self.initial[T]

    def __init__(self, goal):
        self.initial = (7,0,0)
        self.goal = goal

    list = []
    def actions(self, state):
        newState = (0, 0, 0)
        #the amounts of add and subtract

        # Pour as much as you can into the 7 liters from 3 liter
        for x in range(state[S]):
            if tempS == 0 OR tempT == 3:
                break
            tempS = tempS - 1
            tempT = tempT + 1

        newState = (tempS, state[F], tempT)
        reset()
        if(validate(newState)):
            list.append(newState)
        # Pour as much as you can into the 7 liters from 4 liter
        newState = (state[S] + state[F], state[F] - state[F], state[T])
        if(validate(newState)):
            list.append(newState)



    def validate(self, state):

        # check for negative amounts
        if state[Problem2.S] < 0 OR state[Problem2.F] < 0 OR state[Problem.T] < 0:
            return False
        # check if there is an overflow of water
        if state[Problem2.S] > 7 OR state[Problem2.F] > 4 OR state[Problem.T] > 3:
            return False

        return True

    def reset():
        state[S] = self.initial[S]
        state[F] = self.initial[F]
        state[T] = self.initial[T]

def main():

    goalState = (2,2,3)

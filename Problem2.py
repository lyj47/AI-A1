"""
V1.0
"""

"""
States:
The states consists of keeping track of the amount the 3 jugs (7, 4, and 3 liters) hold at any time.

Actions possible:

Pour water from the 7 liter jug into the 4 liter jug until the 4 liter is full or the 7 liter is empty
Pour water from the 7 liter jug into the 3 liter jug until the 3 liter is full or the 7 liter is empty
Pour water from the 4 liter jug into the 7 liter jug until the 7 liter is full or the 4 liter is empty
Pour water from the 4 liter jug into the 3 liter jug until the 3 liter is full or the 4 liter is empty
Pour water from the 3 liter jug into the 7 liter jug until the 7 liter is full or the 3 liter is empty
Pour water from the 3 liter jug into the 4 liter jug until the 4 liter is full or the 3 liter is empty
"""

from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search

class Problem2(Problem):

    # Seven liter, Four liter, Three liter
    S = 0; F = 1; T = 2

    tempS = 0; tempF = 0; tempT = 0

    def __init__(self, goal):
        self.initial = (7,0,0)
        self.goalState = goal
        tempS = self.initial[Problem2.S]; tempF = self.initial[Problem2.F]; tempT = self.initial[Problem2.T]

    def actions(self, state):
        list = []
        newState = (0, 0, 0)

        # Pour as much as you can from the 7 liters into 3 liters
        for x in range(state[Problem2.S]):
            if Problem2.tempS == 0 or Problem2.tempT == 3:
                break
            Problem2.tempS = Problem2.tempS - 1
            Problem2.tempT = Problem2.tempT + 1

        newState = (Problem2.tempS, Problem2.tempF, Problem2.tempT)
        self.reset(state)
        if self.validate(newState):
            list.append(newState)
        # Pour as much as you can from the 7 liters into 4 liters
        for x in range(state[Problem2.S]):
            if Problem2.tempS == 0 or Problem2.tempF == 4:
                break
            Problem2.tempS = Problem2.tempS - 1
            Problem2.tempF = Problem2.tempF + 1

        newState = (Problem2.tempS, Problem2.tempF, Problem2.tempT)
        self.reset(state)
        if self.validate(newState):
            list.append(newState)

        # Pour as much as you can from the 4 liters into 3 liters
        for x in range(state[Problem2.F]):
            if Problem2.tempF == 0 or Problem2.tempT == 3:
                break
            Problem2.tempF = Problem2.tempF - 1
            Problem2.tempT = Problem2.tempT + 1

        newState = (Problem2.tempS, Problem2.tempF, Problem2.tempT)
        self.reset(state)
        if self.validate(newState):
            list.append(newState)
        # Pour as much as you can from the 4 liters from 7 liters
        for x in range(state[Problem2.F]):
            if Problem2.tempF == 0 or Problem2.tempS == 7:
                break
            Problem2.tempF = Problem2.tempF - 1
            Problem2.tempS = Problem2.tempS + 1

        newState = (Problem2.tempS, Problem2.tempF, Problem2.tempT)
        self.reset(state)
        if self.validate(newState):
            list.append(newState)

        # Pour as much as you can into the 3 liters from 4 liters
        for x in range(state[Problem2.T]):
            if Problem2.tempT == 0 or Problem2.tempF == 4:
                break
            Problem2.tempT = Problem2.tempT - 1
            Problem2.tempF = Problem2.tempF + 1

        newState = (Problem2.tempS, Problem2.tempF, Problem2.tempT)
        self.reset(state)
        if self.validate(newState):
            list.append(newState)
        # Pour as much as you can into the 3 liters from 7 liters
        for x in range(state[Problem2.T]):
            if Problem2.tempT == 0 or Problem2.tempS == 7:
                break
            Problem2.tempT = Problem2.tempT - 1
            Problem2.tempS = Problem2.tempS + 1

        newState = (Problem2.tempS, Problem2.tempF, Problem2.tempT)
        self.reset(state)
        if self.validate(newState):
            list.append(newState)

        return list

    def validate(self, state):

        # check for negative amounts
        if state[Problem2.S] < 0 or state[Problem2.F] < 0 or state[Problem2.T] < 0:
            return False
        # check if there is an overflow of water
        if state[Problem2.S] > 7 or state[Problem2.F] > 4 or state[Problem2.T] > 3:
            return False

        return True

    def result(self, state, action):
        return action

    def goal_test(self, state):
        return state == self.goalState

    def reset(self, state):
        Problem2.tempS = state[Problem2.S]
        Problem2.tempF = state[Problem2.F]
        Problem2.tempT = state[Problem2.T]

def main():
    #Runs the Cannibals and Missionary problem, will provide a solution to getting all missionaries
    #and all cannibals to the other side, without missionaries ever being outnumbered by cannibals
    #on either side.
    print('Missionaries/Cannibals Problem: ')
    print(' Tuples are in this format --> [<Node (leftMissionaries, rightMissionaries, leftCannibals, rightCannibals, boatSide)>]')
    goalState = (2,2,3)

    problem = Problem2(goalState)
    goal = depth_first_search(problem)

    print("\nPath = ",goal.path(),"\n\nPath cost = ",goal.path_cost)
    #print("      Steps = " + str(goal.path()), "\n      Cost = " + str(goal.path_cost))
    print()

main()

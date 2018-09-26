"""
V1.0
"""

'''
States:
The states are based on the sides for each person, with the sons and daughters
grouped into 1 state, and the boat having it's own state.

There is a LEFT state for the Thief, Mom, Dad, Sons, Daughters, Police.
There is also a corresponding RIGHT state for each of those.
The boat is binary, 0 for left and 1 for right. 

Actions possible:

Police moves right
Police & Thief moves right
Police & Mom moves right
Police & Dad moves right
Police & 1 son moves right
Police & 1 daughter moves right
Dad moves right
Dad & 1 son moves right
Dad & 1 daughter moves right
Dad & Thief moves right
Mom moves right
Mom & 1 son moves right
Mom & 1 daughter moves right
Mom & Thief moves right
Mom & Dad moves right

All the same moves are possible for moving to the left.

'''
from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search

class Problem1(Problem):

    TL = 0; ML = 1; Dad_L = 2; SL = 3; Dau_L = 4; PL = 5
    TR = 6; MR = 7; Dad_R = 8; SR = 9; Dau_R = 10; PR = 11; B = 12

    def __init__(self, goal):
        self.initial = (1,1,1,2,2,1,0,0,0,0,0,0,0)
        self.goalState = goal

    def actions(self, state):
        list = []
        # boat is on the left
        if state[Problem1.B] == 0:
            # police moves to the right
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL]-1, state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR]+1, 1)
            if self.validate(newState):
                list.append(newState)

            # police and thief move to the right
            newState = (state[Problem1.TL]-1, state[Problem1.ML], state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL]-1, state[Problem1.TR]+1, state[Problem1.MR], state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR]+1, 1)
            if self.validate(newState):
                list.append(newState)

            # police and 1 son move to the right
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L], state[Problem1.SL]-1, state[Problem1.Dau_L], state[Problem1.PL]-1, state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R], state[Problem1.SR]+1, state[Problem1.Dau_R], state[Problem1.PR]+1, 1)
            if self.validate(newState):
                list.append(newState)

            # police and 1 daughter move to the right
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L]-1, state[Problem1.PL]-1, state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R]+1, state[Problem1.PR]+1, 1)
            if self.validate(newState):
                list.append(newState)

            # police and mom move to the right
            newState = (state[Problem1.TL], state[Problem1.ML]-1, state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL]-1, state[Problem1.TR], state[Problem1.MR]+1, state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR]+1, 1)
            if self.validate(newState):
                list.append(newState)

            # police and dad move to the right
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L]-1, state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL]-1, state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R]+1, state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR]+1, 1)
            if self.validate(newState):
                list.append(newState)

            # dad moves to the right
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L]-1, state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R]+1, state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR], 1)
            if self.validate(newState):
                list.append(newState)

            # dad and mom moves to the right
            newState = (state[Problem1.TL], state[Problem1.ML]-1, state[Problem1.Dad_L]-1, state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR], state[Problem1.MR]+1, state[Problem1.Dad_R]+1, state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR], 1)
            if self.validate(newState):
                list.append(newState)

            # dad and 1 son move to the right
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L]-1, state[Problem1.SL]-1, state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R]+1, state[Problem1.SR]+1, state[Problem1.Dau_R], state[Problem1.PR], 1)
            if self.validate(newState):
                list.append(newState)

            # dad and 1 daughter move to the right
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L]-1, state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R]+1, state[Problem1.SR], state[Problem1.Dau_R]+1, state[Problem1.PR], 1)
            if self.validate(newState):
                list.append(newState)

            # dad and thief moves to the right
            newState = (state[Problem1.TL]-1, state[Problem1.ML], state[Problem1.Dad_L]-1, state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR]+1, state[Problem1.MR], state[Problem1.Dad_R]+1, state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR], 1)
            if self.validate(newState):
                list.append(newState)

            # mom moves to the right
            newState = (state[Problem1.TL], state[Problem1.ML]-1, state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR], state[Problem1.MR]+1, state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR], 1)
            if self.validate(newState):
                list.append(newState)

            # mom and 1 son move to the right
            newState = (state[Problem1.TL], state[Problem1.ML]-1, state[Problem1.Dad_L], state[Problem1.SL]-1, state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR], state[Problem1.MR]+1, state[Problem1.Dad_R], state[Problem1.SR]+1, state[Problem1.Dau_R], state[Problem1.PR], 1)
            if self.validate(newState):
                list.append(newState)

            # mom and 1 daughter move to the right
            newState = (state[Problem1.TL], state[Problem1.ML]-1, state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L]-1, state[Problem1.PL], state[Problem1.TR], state[Problem1.MR]+1, state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R]+1, state[Problem1.PR], 1)
            if self.validate(newState):
                list.append(newState)

            # mom and thief move to the right
            newState = (state[Problem1.TL]-1, state[Problem1.ML]-1, state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR]+1, state[Problem1.MR]+1, state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR], 1)
            if self.validate(newState):
                list.append(newState)

        # boat is on the right
        else:
            # police moves to the left
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL]+1, state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR]-1, 0)
            if self.validate(newState):
                list.append(newState)

            # police and thief move to the left
            newState = (state[Problem1.TL]+1, state[Problem1.ML], state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL]+1, state[Problem1.TR]-1, state[Problem1.MR], state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR]-1, 0)
            if self.validate(newState):
                list.append(newState)

            # police and 1 son move to the left
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L], state[Problem1.SL]+1, state[Problem1.Dau_L], state[Problem1.PL]+1, state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R], state[Problem1.SR]-1, state[Problem1.Dau_R], state[Problem1.PR]-1, 0)
            if self.validate(newState):
                list.append(newState)

            # police and 1 daughter move to the left
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L]+1, state[Problem1.PL]+1, state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R]-1, state[Problem1.PR]-1, 0)
            if self.validate(newState):
                list.append(newState)

            # police and mom move to the left
            newState = (state[Problem1.TL], state[Problem1.ML]+1, state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL]+1, state[Problem1.TR], state[Problem1.MR]-1, state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR]-1, 0)
            if self.validate(newState):
                list.append(newState)

            # police and dad move to the left
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L]+1, state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL]+1, state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R]-1, state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR]-1, 0)
            if self.validate(newState):
                list.append(newState)

            # dad moves to the left
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L]+1, state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R]-1, state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR], 0)
            if self.validate(newState):
                list.append(newState)

            # dad and thief moves to the left
            newState = (state[Problem1.TL]+1, state[Problem1.ML], state[Problem1.Dad_L]+1, state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR]-1, state[Problem1.MR], state[Problem1.Dad_R]-1, state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR], 0)
            if self.validate(newState):
                list.append(newState)

            # dad and 1 son move to the left
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L]+1, state[Problem1.SL]+1, state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R]-1, state[Problem1.SR]-1, state[Problem1.Dau_R], state[Problem1.PR], 0)
            if self.validate(newState):
                list.append(newState)

            # dad and 1 daughter move to the left
            newState = (state[Problem1.TL], state[Problem1.ML], state[Problem1.Dad_L]+1, state[Problem1.SL], state[Problem1.Dau_L]+1, state[Problem1.PL], state[Problem1.TR], state[Problem1.MR], state[Problem1.Dad_R]-1, state[Problem1.SR], state[Problem1.Dau_R]-1, state[Problem1.PR], 0)
            if self.validate(newState):
                list.append(newState)

            # dad and mom moves to the left
            newState = (state[Problem1.TL], state[Problem1.ML]+1, state[Problem1.Dad_L]+1, state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR], state[Problem1.MR]-1, state[Problem1.Dad_R]-1, state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR], 1)
            if self.validate(newState):
                list.append(newState)

            # mom moves to the left
            newState = (state[Problem1.TL], state[Problem1.ML]+1, state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR], state[Problem1.MR]-1, state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR], 0)
            if self.validate(newState):
                list.append(newState)

            # mom and 1 son move to the left
            newState = (state[Problem1.TL], state[Problem1.ML]+1, state[Problem1.Dad_L], state[Problem1.SL]+1, state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR], state[Problem1.MR]-1, state[Problem1.Dad_R], state[Problem1.SR]-1, state[Problem1.Dau_R], state[Problem1.PR], 0)
            if self.validate(newState):
                list.append(newState)

            # mom and 1 daughter move to the left
            newState = (state[Problem1.TL], state[Problem1.ML]+1, state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L]+1, state[Problem1.PL], state[Problem1.TR], state[Problem1.MR]-1, state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R]-1, state[Problem1.PR], 0)
            if self.validate(newState):
                list.append(newState)

            # mom and thief move to the right
            newState = (state[Problem1.TL]+1, state[Problem1.ML]+1, state[Problem1.Dad_L], state[Problem1.SL], state[Problem1.Dau_L], state[Problem1.PL], state[Problem1.TR]-1, state[Problem1.MR]-1, state[Problem1.Dad_R], state[Problem1.SR], state[Problem1.Dau_R], state[Problem1.PR], 0)
            if self.validate(newState):
                list.append(newState)

        return list

    def validate(self, state):
        # Any negatives
        if (state[Problem1.ML] < 0 or state[Problem1.Dad_L] < 0 or state[Problem1.SL] < 0 or state[Problem1.Dau_L] < 0 or
            state[Problem1.PL] < 0 or state[Problem1.TL] < 0 or state[Problem1.MR] < 0 or state[Problem1.Dad_R] < 0 or
            state[Problem1.SL] < 0 or state[Problem1.Dau_R] < 0 or state[Problem1.PR] < 0 or state[Problem1.TR] < 0) :
            return False
        # Overflow
        if (state[Problem1.ML] > 1 or state[Problem1.Dad_L] > 1 or state[Problem1.SL] > 2 or state[Problem1.Dau_L] > 2 or
            state[Problem1.PL] > 1 or state[Problem1.TL] > 1 or state[Problem1.MR] > 1 or state[Problem1.Dad_R] > 1 or
            state[Problem1.SL] > 2 or state[Problem1.Dau_R] > 2 or state[Problem1.PR] > 1 or state[Problem1.TR] > 1) :
            return False
        # Mom is left with sons
        if (state[Problem1.ML] == 1 and state[Problem1.SL] > 0 and state[Problem1.Dad_L] == 0) or (state[Problem1.MR] == 1 and state[Problem1.SR] > 0 and state[Problem1.Dad_R] == 0):
            return False
        # Dad is left with daughters
        if (state[Problem1.ML] == 0 and state[Problem1.Dau_L] > 0 and state[Problem1.Dad_L] == 1) or (state[Problem1.MR] == 0 and state[Problem1.Dau_R] > 0 and state[Problem1.Dad_R] == 1):
            return False
        # Thief is alone with a family member
        if (state[Problem1.PL] == 0 and state[Problem1.TL] == 1 and self.family_is_left(state)) or (state[Problem1.PR] == 0 and state[Problem1.TR] == 1 and self.family_is_right(state)):
            return False

        return True

    def family_is_left(self, state):
        return state[Problem1.ML] == 1 or state[Problem1.Dad_L] == 1 or state[Problem1.SL] > 0 or state[Problem1.Dau_L] > 0

    def family_is_right(self, state):
        return state[Problem1.MR] == 1 or state[Problem1.Dad_R] == 1 or state[Problem1.SR] > 0 or state[Problem1.Dau_R] > 0

    def result(self, state, action):
        return action

    def goal_test(self, state):
        return state == self.goalState

def main():
    print('River Crossing: ')
    print(' Tuples are in this format --> [<Node (leftThief, leftMom, leftDad, leftSons, leftDaughters, leftPolice, rightThief, rightMom, rightDad, rightSons, rightDaughters, rightPolice boatSide)>]')
    goalState = (0,0,0,0,0,0,1,1,1,2,2,1,1)

    problem = Problem1(goalState)
    goal = depth_first_search(problem)

    print("\nPath = ",goal.path(),"\n\nPath cost = ",goal.path_cost)
    #print("      Steps = " + str(goal.path()), "\n      Cost = " + str(goal.path_cost))
    print()

main()

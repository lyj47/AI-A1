"""
V1.0
"""

"""
The state space consists of 3 states containing the water amount for each 7, 4, and 3 liter jugs.

You shouldn't pour more than 4 liters of water into the 4 liter jug, and 3 liters for the 3 liter jug.


"""

'''
ehhhhhhh i'm sean and i use single quotes ehghhhhhhhhhhhhhhhh - Sean Mitchell

P.S hello GT, i luv u <4. Speak your sweet Clean Code words to me. And giv wife pls. Best waifu. - Sean Mitchell

P.S.S i'm the dude doin' the practi-cummmmmmmm
'''
from search import Problem, breadth_first_search,depth_first_search, iterative_deepening_search

class Problem2(Problem):

    # Seven liter, Four liter, Three liter
    S = 0; F = 1; T = 2

    def __init__(self, goal):
        self.initial = (7,0,0)
        self.goal = goal

    list = []
    def actions(self, state):


    def validate(self, state):

        # check for negative amounts
        if state[Problem2.S] < 0 OR state[Problem2.F] < 0 OR state[Problem.T] < 0:
            return False
        # check if there is an overflow of water
        if state[Problem2.S] > 7 OR state[Problem2.F] > 4 OR state[Problem.T] > 3:
            return False

        return True

def main():

    goalState = (2,2,3)

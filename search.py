# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # 0th
    # Check if initial state is goal state
    if problem.isGoalState(problem.getStartState()):
        return []

    # INIT
    else:
        from util import Stack

        # stackXY: ((x,y),[path]) #
        stackXY = Stack()

        visited = []  # Visited states
        path = []  # Every state keeps it's path from the starting state
    #============

    # 1st get ROOT - Start from the beginning and find a solution
    stackXY.push((problem.getStartState(), []))
    # example:
    # Stack.push( (34,16), empty_path_list )

    """Friendly reminder: in a while loop, NODE can be any thing, from the root to the child"""
    while not (stackXY.isEmpty()): # fight till the end baby
        # 2nd pop the NODE
        xy, path = stackXY.pop()

        # 2.b. marked Visited
        visited.append(xy)

        # 3rd Expand - Moving to intercept next targets
        targetList = problem.expand(xy)

        if targetList:
            for target in targetList:
                # target[0] is the target's coordinate
                if target[0] not in visited:
                    # Lectures code: Artillerie, feuer auf diese Position
                    # if target[0] not in visited and target[0] not in (state[0] for state in stackXY.list):
                    #   if problem.isGoalState(target[0]):
                    #       return path + [target[1]]

                    # 3.b. Calculate new path
                    newPath = path + [target[1]]

                    # 4th check Jackpot?
                    if problem.isGoalState(target[0]):
                        return newPath

                    # Students code: attack enemy fucking position
                    # 5th push to Stack
                    stackXY.push((target[0], newPath))
#end depthFirstSearch()
#==================================================================================

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    if problem.isGoalState(problem.getStartState()):
        return []

    # INIT
    else:
        from util import Queue

        # queueXY: ((x,y),[path]) #
        queueXY = Queue()

        visited = []  # Visited states
        path = []  # Every state keeps it's path from the starting state
    # ============

    # 1st get ROOT - Start from the beginning and find a solution
    queueXY.push((problem.getStartState(), []))
    # example:
    # Stack.push( (34,16), empty_path_list )

    """Friendly reminder: in a while loop, NODE can be any thing, from the root to the child"""
    while not (queueXY.isEmpty()):  # fight till the end baby
        # 2nd pop the NODE
        xy, path = queueXY.pop()

        # 2.b. marked Visited
        visited.append(xy)

        # 3rd Expand - Moving to intercept next targets
        targetList = problem.expand(xy)

        if targetList:
            for target in targetList:
                # target[0] is the target's coordinate
                if target[0] not in visited:
                    # Lectures code: Artillerie, feuer auf diese Position
                    # if target[0] not in visited and target[0] not in (state[0] for state in queueXY.list):
                    #   if problem.isGoalState(target[0]):
                    #       return path + [target[1]]

                    # 3.b. Calculate new path
                    newPath = path + [target[1]]

                    # 4th check Jackpot?
                    if problem.isGoalState(target[0]):
                        return newPath

                    # Students code: attack enemy fucking position
                    # 5th push to Stack
                    queueXY.push((target[0], newPath))

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch

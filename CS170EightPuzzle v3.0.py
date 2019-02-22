#Version 3.0 notes
#-cleaned up code for presentation
import math, queue, copy, time
puzzleSize = 9;  #number of tiles in square
winState = ['1','2','3','4','5','6','7','8','0']

def goalTest(gameboard):
    for i in range(0, puzzleSize):
        if gameboard[i] != winState[i]:
          return False
    return True

def misplacedTile(gameboard):
    count = 0
    if gameboard != []:
        for i in range(0, puzzleSize):
            if gameboard[i] != winState[i]:
                count += 1
    return count     #return number of misplaced tiles

def manhattanDistance(gameboard):
    manSum = 0
    for i in range(0, puzzleSize):
         if int(gameboard[i]) != 0 and gameboard[i] != winState[i]:
            iRow = i // math.sqrt(puzzleSize) #converting to coordinates
            iCol = i % math.sqrt(puzzleSize)
            winRow = int(winState.index(gameboard[i])) // math.sqrt(puzzleSize)
            winCol = int(winState.index(gameboard[i])) % math.sqrt(puzzleSize)
            manSum += abs(iRow - winRow) + abs(iCol - winCol)
    return manSum     #return manhattan distance calculation

def expand(node, g):
    t1 = copy.deepcopy(node)
    t2 = copy.deepcopy(node)
    t3 = copy.deepcopy(node)
    t4 = copy.deepcopy(node)
    templist = []
    if checkUp(node):
        templist.append(moveUp(t1))
    if checkDown(node):
        templist.append(moveDown(t2))
    if checkLeft(node):
        templist.append(moveLeft(t3))
    if checkRight(node):
        templist.append(moveRight(t4))
    return templist

#This function is builds the tree for uniform search and returns the goal state on success or empty list on failure
def generalSearch(gameboard, choice):
    nodes = queue.PriorityQueue()
    nodes.put((0,gameboard))
    g = 0
    while True:
        if nodes.empty():
            return [] #no solution
        node = nodes.get()
        g = g + 1;
        print("Best state to expand with g(n) = " + str(g) + " and h(n) = " + str(node[0]) + " is ")
        displayState(node[1])
        if goalTest(node[1]):
            return node[1] #node is a tuple, node[0] is the A* calculation and node[1] is the state
        tempnodes = expand(node[1], g) #the new nodes that we expand then put into our PriorityQueue
        if choice == '1':
            for i in range(0, len(tempnodes)):
                nodes.put((g, tempnodes[i])) #g is just g(n) since h(n) is hardcoded to 0
        elif choice == '2':
            for i in range(0, len(tempnodes)):
                nodes.put((misplacedTile(tempnodes[i]),tempnodes[i])) #misplacedTile returns h(n)
        elif choice == '3':
            for i in range(0, len(tempnodes)):
                nodes.put((manhattanDistance(tempnodes[i]), tempnodes[i])) #manhattaDistance returns h(n)

def displayState(gameboard):
    print(gameboard[0] + " " + gameboard[1] + " " + gameboard[2])
    print(gameboard[3] + " " + gameboard[4] + " " + gameboard[5])
    print(gameboard[6] + " " + gameboard[7] + " " + gameboard[8])

#These functions check if moves are valid and make the swap in the list
def checkUp(gameboard):
    if gameboard.index('0') != 0 and gameboard.index('0') != 1 and gameboard.index('0') != 2:
        return True
    return False
def moveUp(gameboard):
    a = gameboard.index('0')
    b = gameboard.index('0') - 3
    gameboard[b], gameboard[a] = gameboard[a], gameboard[b]
    return gameboard
def checkDown(gameboard):
    if gameboard.index('0') != 6 and gameboard.index('0') != 7 and gameboard.index('0') != 8:
        return True
    return False

def moveDown(gameboard):
    a = gameboard.index('0')
    b = gameboard.index('0') + 3
    gameboard[b], gameboard[a] = gameboard[a], gameboard[b]
    return gameboard
def checkLeft(gameboard):
    if gameboard.index('0') != 0 and gameboard.index('0') != 3 and gameboard.index('0') != 6:
        return True
    return False

def moveLeft(gameboard):
    a = gameboard.index('0')
    b = gameboard.index('0') - 1
    gameboard[b], gameboard[a] = gameboard[a], gameboard[b]
    return gameboard
def checkRight(gameboard):
    if gameboard.index('0') != 2 and gameboard.index('0') != 5 and gameboard.index('0') != 8:
        return True
    return False

def moveRight(gameboard):
    a = gameboard.index('0')
    b = gameboard.index('0') + 1
    gameboard[b], gameboard[a] = gameboard[a], gameboard[b]
    return gameboard

print("Welcome to Richard Rangel's 8-puzzle solver!")
print("Enter your puzzle in order(each element in each row, left to right), use a zero to represent the blank")
gameboard = []
for i in range(0, puzzleSize):
    gameboard.append(input("Enter board element " + str(i) + ": "))

displayState(gameboard)
print("Enter your choice of algorithm: \n1. Uniform Cost Search\n2. A* with the Misplaced Tile heuristic\n3. A* with the Manhattan Distance heuristic.")
choice = input()
startTime = time.time()
if generalSearch(gameboard, choice) != []:
    stopTime = time.time() - startTime
    print("solution found")
    print("Elapsed time = " + str(stopTime) + " seconds.")
else:
    stopTime = time.time() - startTime
    print("solution not found")
    print("Elapsed time = " + str(stopTime) + " seconds.")
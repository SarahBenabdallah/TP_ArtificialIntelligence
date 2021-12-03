import queue

from colorama import Fore, Back, Style


left_down_angle = '\u2514'
right_down_angle = '\u2518'
right_up_angle = '\u2510'
left_up_angle = '\u250C'

middle_junction = '\u253C'
top_junction = '\u252C'
bottom_junction = '\u2534'
right_junction = '\u2524'
left_junction = '\u251C'

bar = Style.BRIGHT + Fore.BLACK + '\u2502' + Fore.RESET + Style.RESET_ALL
dash = '\u2500'

first_line = Style.BRIGHT + Fore.BLACK + left_up_angle + dash + dash + dash + top_junction + dash + dash + dash + top_junction + dash + dash + dash + right_up_angle + Fore.RESET + Style.RESET_ALL
middle_line = Style.BRIGHT + Fore.BLACK + left_junction + dash + dash + dash + middle_junction + dash + dash + dash + middle_junction + dash + dash + dash + right_junction + Fore.RESET + Style.RESET_ALL
last_line = Style.BRIGHT + Fore.BLACK + left_down_angle + dash + dash + dash + bottom_junction + dash + dash + dash + bottom_junction + dash + dash + dash + right_down_angle + Fore.RESET + Style.RESET_ALL

def print_node(array):
    print(first_line)
    for a in range(len(array)):
        if array[a] == 0:
            print(bar, ' ' + Back.RESET, end=' ')
        else:
            print(bar, array[a], end=' ')
        if a % 3 == 2 and a != 8:
            print(bar)
            print(middle_line)
    print(bar)
    print(last_line)

def print_sol(etat,moves):
    list = []
    list[:0] = moves
    print_node(etat)
    for move in list:
        index = etat.index(0)
        if move == "L":
            etat[index] = etat[index - 1]
            etat[index - 1] = 0
        elif move == "R":
            etat[index] = etat[index + 1]
            etat[index + 1] = 0

        elif move == "U":
            etat[index] = etat[index - 3]
            etat[index - 3] = 0

        elif move == "D":
            etat[index] = etat[index + 3]
            etat[index + 3] = 0
        print_node(etat)

def valid(indexOf0,move):
    if move == "L":
        return indexOf0 not in [0,3,6]

    elif move == "R":
        return indexOf0 not in [2,5,8]

    elif move == "U":
        return indexOf0 not in [0,1,2]

    elif move == "D":
        return indexOf0 not in [6,7,8]

def nouvEtat(etatInitial, moves):
    list = []
    list[:0] = moves
    etat = etatInitial.copy()
    for move in list:
        index = etat.index(0)
        if move == "L":
            etat[index] = etat[index - 1]
            etat[index - 1] = 0
        elif move == "R":
            etat[index] = etat[index + 1]
            etat[index + 1] = 0

        elif move == "U":
            etat[index] = etat[index - 3]
            etat[index - 3] = 0

        elif move == "D":
            etat[index] = etat[index + 3]
            etat[index + 3] = 0

    return etat


def BFS(etatInitial):
    moves = queue.Queue()
    moves.put("")
    path = ""
    etat = etatInitial
    visited = 0
    while not etat == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        path = moves.get()
        visited += 1
        etat = nouvEtat(etatInitial, path)
        if  etat == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            break
        for j in ["L", "R", "U", "D"]:
            put = path + j
            if valid(etat.index(0), j):
                moves.put(put)
    print_sol(etatInitial, path)
    print('depth =',len(path))
    print('visited node = ',visited)

def DFS(etatInitial):
    closed = []
    moves = queue.LifoQueue()
    moves.put("")
    path = ""
    etat = etatInitial
    visited = 0
    while not etat == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        path = moves.get()
        etat = nouvEtat(etatInitial, path)
        visited += 1
        closed.append(etat)
        if  etat == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            break
        for j in ["D", "R", "U", "L"]:
            put = path + j
            if valid(etat.index(0), j) and nouvEtat(etatInitial, put) not in closed:
                moves.put(put)
    print_sol(etatInitial, path)
    print('depth =',len(path))
    print('visited node = ',visited)

def DFSIteratif(etatInitial):
    index = 0
    visited = [0]
    found = DFSWithDepth(etatInitial,index ,visited)
    while found == 0:
        found = DFSWithDepth(etatInitial, index,visited)
        index+=1
    print_sol(etatInitial, found)
    print('depth =',len(found))
    print('visited node =',visited[0])

def DFSWithDepth(etatInitial,depth,visited):
    closed = []
    moves = queue.LifoQueue()
    moves.put("")
    path = ""
    etat = etatInitial
    while not etat == [0 ,1, 2, 3, 4, 5, 6, 7, 8] and not moves.empty():
        visited[0]+=1
        path = moves.get()
        etat = nouvEtat(etatInitial, path)
        closed.append(etat)
        if  etat == [0 ,1, 2, 3, 4, 5, 6, 7, 8]:
            break
        for j in ["D", "R", "U", "L"]:
            put = path + j
            if valid(etat.index(0), j) and nouvEtat(etatInitial, put) not in closed and len(put) <= depth:
                moves.put(put)
    if(etat == [0 ,1, 2, 3, 4, 5, 6, 7, 8]):
        return path
        #print_sol(etatInitial, path)
    else:
        return 0
        #print("no_solution")

if __name__ == '__main__':
     #DFS([3,1,2,4,5,0,6,7,8])
    # DFS([3,1,2,4,5,0,6,7,8])
    # DFS([1,2,3,4,8,5,7,0,6])
     DFSIteratif([3,1,2,4,5,0,6,7,8])

      


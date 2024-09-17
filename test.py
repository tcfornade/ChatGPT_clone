# def NextAnimal(animals, n):
#     # if n is under 5 then return n-1 because the index starts from 0
#     if(n <= 5):
#         return animals[n-1]

#     # if n > 5 then I observe a pattern , every animal appears first in the queue by a power of 2 
#     # to find a formula more easily I transform the animals into numbers: 1, 2, 3, 4, 5 and the queue will be: 1122334455 after 5 * 1 iterations
#     # and 11112222333344445555 after 5 * 2
#     # for that I subtract from n these values to reach a lower value
#     i=1
#     while(n - 5*i > 0):
#         n = n - 5*i
#         i = i * 2 

#     n = int(n/5) #the value we reached will have to be divided by the number of elements
    
#     # for a very large value of n I perform repeated divisions
#     while(n > 5):
#         n = int (n / 5) + 1
       
#     return animals[n-1]  

# animals =  ["Lion", "Giraffe", "Elephant", "Monkey", "Tiger"];
# print(NextAnimal(animals, 1))


from collections import deque 

def findTheFridge(officeMap, S, C):
    N, M = len(officeMap), len(officeMap[0]) #N-rows, M-columns
    
    #I initialized a queue to store the coordinates of the path (x, y)
    queue = deque([S]) # the first element is the S - start point

    #variable to store the visited nodes
    visit = set([S])
    
    #initialize a dictionary to store the parent of each node to reconstruct the path
    parent = {S: None}

    # directions for movement (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == C:
            return reconstructPath(parent, S, C)

        for row, col in directions:
            new_x, new_y = x + row, y + col
                
            if (0 <= new_x  and 0 <= new_y and (new_x, new_y) not in visit and officeMap[new_x][new_y] == '-'):
                queue.append((new_x, new_y))
                visit.add((new_x, new_y))
                parent[(new_x, new_y)] = (x, y)
                    
        return []

#function to reconstruct the path
def reconstructPath(parent, S, C):
    path = []
    current = C

    while current is not None:
        path.append(current)
        current = parent.get(current)
    path.reverse()
    return path

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, '-', '#', '#', '-', 'S', '#', '-', '#', 0],
        [0, '-', '-', '#', '-', '-', '-', '-', '#', 0],
        [0, '#', '-', '#', '-', '-', '#', '-', '#', 0],
        [0, '-', '-', '-', '-', '#', '-', '-', '#', 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

path = findTheFridge(grid, (1,5), (5,1))
print(path)
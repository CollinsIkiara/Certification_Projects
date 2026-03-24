# Tower of Hanoi Algorithm

# The Tower of Hanoi is a mathematical puzzle that consists of three rods and a number of disks of different sizes which can slide onto any rod. The puzzle starts with the disks stacked on one rod in order of decreasing size, the smallest at the top, thus making a conical shape. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
def hanoi_solver(n):
 
    rods = [list(range(n, 0, -1)), [], []]
    moves = []
 
    def state():
        return ' '.join(str(rod) for rod in rods)
 
    def move(num_disks, source, target, auxiliary):
        if num_disks == 0:
            return
        move(num_disks - 1, source, auxiliary, target)
        disk = rods[source].pop()
        rods[target].append(disk)
        moves.append(state())
        move(num_disks - 1, auxiliary, target, source)
 
    moves.append(state())
    move(n, 0, 2, 1)
 
    return '\n'.join(moves)

# Test the function with different numbers of disks
print(hanoi_solver(2))
print('') # Add a blank line for better readability
print(hanoi_solver(3))
print('')
print(hanoi_solver(4))
print('')
print(hanoi_solver(5))

## Output:
# [2, 1] [] []
# [2] [1] []
# [] [1] [2]
# [] [] [2, 1]

# [3, 2, 1] [] []
# [3, 2] [] [1]
# [3] [2] [1]
# [3] [2, 1] []
# [] [2, 1] [3]
# [1] [2] [3]
# [1] [] [3, 2]
# [] [] [3, 2, 1]

# [4, 3, 2, 1] [] []
# [4, 3, 2] [1] []
# [4, 3] [1] [2]
# [4, 3] [] [2, 1]
# [4] [3] [2, 1]
# [4, 1] [3] [2]
# [4, 1] [3, 2] []
# [4] [3, 2, 1] []
# [] [3, 2, 1] [4]
# [] [3, 2] [4, 1]
# [2] [3] [4, 1]
# [2, 1] [3] [4]
# [2, 1] [] [4, 3]
# [2] [1] [4, 3]
# [] [1] [4, 3, 2]
# [] [] [4, 3, 2, 1]

# [5, 4, 3, 2, 1] [] []
# [5, 4, 3, 2] [] [1]
# [5, 4, 3] [2] [1]
# [5, 4, 3] [2, 1] []
# [5, 4] [2, 1] [3]
# [5, 4, 1] [2] [3]
# [5, 4, 1] [] [3, 2]
# [5, 4] [] [3, 2, 1]
# [5] [4] [3, 2, 1]
# [5] [4, 1] [3, 2]
# [5, 2] [4, 1] [3]
# [5, 2, 1] [4] [3]
# [5, 2, 1] [4, 3] []
# [5, 2] [4, 3] [1]
# [5] [4, 3, 2] [1]
# [5] [4, 3, 2, 1] []
# [] [4, 3, 2, 1] [5]
# [1] [4, 3, 2] [5]
# [1] [4, 3] [5, 2]
# [] [4, 3] [5, 2, 1]
# [3] [4] [5, 2, 1]
# [3] [4, 1] [5, 2]
# [3, 2] [4, 1] [5]
# [3, 2, 1] [4] [5]
# [3, 2, 1] [] [5, 4]
# [3, 2] [] [5, 4, 1]
# [3] [2] [5, 4, 1]
# [3] [2, 1] [5, 4]
# [] [2, 1] [5, 4, 3]
# [1] [2] [5, 4, 3]
# [1] [] [5, 4, 3, 2]
# [] [] [5, 4, 3, 2, 1]

'''
Problem Statement
Write a python program to solve a classic ancient Chinese puzzle.

We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
Solution:-
'''

def solve(heads, legs):
    error_msg = "No solution"
    chicken_count = 0
    rabbit_count = 0

    if (heads >= legs):
        print(error_msg)
    elif (legs % 2 != 0):
        print(error_msg)
    else:
        rabbit_count = (legs - 2 * heads) / 2    # rabbits head count
        chicken_count = heads - rabbit_count
        print(int(chicken_count), int(rabbit_count))
  
solve(150, 400)

# end
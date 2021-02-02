import sys

def minCost(cost, row, col): 
    # For 1st column 
    for i in range(1, row): 
        cost[i][0] += cost[i - 1][0] 
    # For 1st row 
    for j in range(1, col): 
        cost[0][j] += cost[0][j - 1] 
    # For rest of the 2d matrix 
    for i in range(1, row): 
        for j in range(1, col): 
            cost[i][j] += (#min(cost[i - 1][j - 1],  # to go diagonally
                           min(cost[i - 1][j], 
                               cost[i][j - 1]))
  
    return cost[row - 1][col - 1] 

row, col = map(int, sys.stdin.readline().split())
m = list()
for i in range(row):
    m.append(list(map(int, sys.stdin.readline().split())))

print(minCost(m, row, col)); 


''' F. Turtle
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

There is a turtle in the upper left corner of the rectangular n × m table. 
Some acid is poured on each cell of this table. 
The turtle can move right or down and 
the turtle's route ends in the lower right corner of the table.

Each milliliter of acid causes a certain amount of damage to the turtle. 
Find the smallest possible damage, the turtle may take during its walk.

Input
The first line of the input contains two positive integers n and m (1 ≤ n, m ≤ 1 000) — the size of the table. 
Next n lines contain m positive integers each, separated by spaces — the description of a table showing for each cell acid content on it (in milliliters). 
It is guaranteed that the acid content of each cell does not exceed 250 milliliters.

Output
The sole line of the output should contain one integer — the minimal possible damage turtle can take.

Examples
Input
3 4
5 9 4 3
3 1 6 9
8 6 8 12
Output
35

Input
1 1
1
Output
1
'''
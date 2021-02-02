import sys
 
n = int(sys.stdin.readline())
k = 2
C = [0] + list(map(int, sys.stdin.readline().split()))

ans = {0:0}
for i in range(1,n+1):
	ans[i] = -10000001 #it should be max(a)==10000 * max(n)==100 +1
	for j in range(max(0,i-k), i):
		if ans[i] < (ans[j] + C[i]): 
			ans[i] = ans[j]+C[i]
 
print(ans[i])

''' C. Ladder
time limit per test: 6 seconds ; memory limit per test: 512 megabytes
input: standard input ; output: standard output

A ladder has n steps numbered by 1, 2, ..., n from bottom to top. Each step has a number written on it. Starting from the bottom of the ladder (the step with the identifier 0) you have to reach the top of the ladder (the step with the identifier n). At each turn, you can go up by one or two steps. When we get to the top, we sum the numbers written on the visited steps. You have to maximize this sum.

Input
The first line of the input contains n (1 ≤ n ≤ 100) — the number of steps in the ladder. The second line contains n integers a1, a2, ..., an ( - 10 000 ≤ ai ≤ 10 000) — the numbers written on the steps.

Output
The sole line of the output should contain one integer — the maximal sum that can be obtained when climbing the ladder.

Examples:
2
1 2
#3

3
-4838 -6093 2234
#-2604

1
1
#1

1
-1
#-1 #the last stairs is the last one, I have to come to it even if i should pay for it

2
1 -1
#0

2
-1 1
#1

3
1 2 3
#6

3
1 2 -1
#2 # 1+2-1 #the last stairs is the last one, I have to come to it even if i should pay for it

2
-3 -2
#-2

10
-8197 -8026 -5437 -6703 -1072 -6483 -1683 -1337 -976 -4827
#-22021

22
-2888 -2807 -8199 -2257 -2950 -2285 -2280 -3117 -6814 -4006 -9052 -8862 -661 -7108 -9788 -4908 -6158 -6061 -4066 -8865 -6052 -1913
#-51972
'''
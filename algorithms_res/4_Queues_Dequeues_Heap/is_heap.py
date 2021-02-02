n = int(input())

a = [0]
a.extend([int(i) for i in input().split()])
ans = True
i = 1
while 2*i+1 < n and ans:
	if a[i] > a[2*i]:
		ans = False
		break
	if a[i] > a[2*i+1]:
		ans = False
		break
	i +=1

if ans:
	if a[i] > a[2*i]:
		ans = False

if ans:
	print('YES')
else:
	print('NO')


''' H. Is it heap?
time limit per test: 1 second ; memory limit per test: 64 megabytes
input: standard input ; output: standard output

Heap can be implemented on an array. The array should satisfy the following condition. Each 1≤𝑖≤𝑛 should satisfy:
If 2𝑖≤𝑛 then 𝑎[𝑖]⩽𝑎[2𝑖] . If 2𝑖+1⩽𝑛 then 𝑎[𝑖]⩽𝑎[2𝑖+1]. 
You are given an array of integers. Please check whether it represents a heap.

Input
The first line of the input contains one integer 𝑛 (1⩽𝑛⩽105) — the number of elements in the array. The second line contains the array: 𝑛 integers that do not exceed 2⋅10^9 by an absolute value.

Output
The sole line of the output should contain «YES», if the array represents a heap, and «NO», otherwise.

Examples
Input
5
1 0 1 2 0
Output
NO

Input
5
1 3 2 5 4
Output
YES

'''
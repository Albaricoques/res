n = int(input())
h = [int(i) for i in input().split()]
lr = list(input())
s = [h[0]]
s_is_empty_and_the_first_was_smaller = False
Lsee = [0] ; now = 1
while now<n:
	Lsee.append(len(s))
	x = s.pop()
	while h[now]>x:
		try:
			x = s.pop()
		except:
			s_is_empty_and_the_first_was_smaller = True
			break
	
	if not s_is_empty_and_the_first_was_smaller :
		s.append(x)
	else:
		s_is_empty_and_the_first_was_smaller = False
	s.append(h[now])
	now+=1
####################################################
s = [h[n-1]]
s_is_empty_and_the_first_was_smaller = False
Rsee = [0]*n ; now = n-2
while now>=0: 
	Rsee[now] = len(s)
	x = s.pop()
	while h[now]>x:
		try:
			x = s.pop()
		except:
			s_is_empty_and_the_first_was_smaller = True
			break
	
	if not s_is_empty_and_the_first_was_smaller :
		s.append(x)
	else:
		s_is_empty_and_the_first_was_smaller = False
	s.append(h[now])
	now-=1

ans = []
for i in range(n):
	if lr[i]=='L':
		ans.append(Lsee[i])
	else:
		ans.append(Rsee[i])
print(*ans)


"""C. Counting in the order
time limit per test: 1 second ; memory limit per test: 512 megabytes
input: standard input ; output: standard output

There are n soldiers in Vasya's troop. Soldiers are standing in a row, each of them is looking to his left or to his right. The height of the i-th soldier in the row is hi. Vasya thinks that the soldier with number i sees the soldier with number j if the following conditions are true:
    soldier i looks in the direction of the soldier j;
    all soldiers standing between them are not taller than the soldier j. 

For example, if there are 4 soldiers in the row with heights h1 = 178, h2 = 180, h3 = 170, h4 = 190, and all soldiers are looking to the left, then the second soldier sees only the first one, the third soldier sees only the second one (because there is a taller soldier between him and the first soldier), the fourth one sees the second and the third soldier.

There is nothing to do while standing in the row, so Vasya wants to calculate how many other soldiers each of the soldiers in the row sees.


Input
The first line of input contains an integer n (1 ≤ n ≤ 105) — the number of soldiers in the row.
The second line contains n integers h1, h2, ..., hn (1 ≤ hi ≤ 109) — the heights of soldiers in the row.
The third line contains n characters representing the directions in which the soldiers look: the i-th symbol is equal to «L» if the i-th soldier looks to the left, and can potentially see only soldiers 1, 2, ..., i - 1, or to «R», if the i-th soldier looks to the right, and can potentially see soldiers i + 1, i + 2, ..., n.

Output
Output n integers, the i-th integer must be equal to the number of soldiers in the row that the i-th soldier sees.


Examples
Input
4
178 180 170 190
LLLL
Output
0 1 1 2

Input
5
178 180 175 170 190
LLRLL
Output
0 1 2 2 3

Input
5
178 180 170 170 160
LLRLL
Output
0 1 1 2 3
"""

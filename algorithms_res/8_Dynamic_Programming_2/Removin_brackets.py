''' E. Removing brackets
time limit per test: 2 seconds;  memory limit per test: 256 megabytes
input: standard input ; output: standard output

Given a string made up of round, square and curly brackets. 
Find a subsequence of maximal length that forms the correct bracket sequence.

Input
The sole line of the input contains a string of round, square and curly brackets. 
The length of the string does not exceed 100 characters.

Output
The sole line of the output should contain the maximum length of a string that is a correct bracket sequence and can be obtained from the original string by deleting some characters.

Examples
Input
([)]
Output
2

Input
{([(]{)})]
Output
6
'''

import sys

s = sys.stdin.readline().strip() ; length = len(s)

dpp = [[-1 for i in range(length)] for j in range(length)]
dpp[0][0] = 1

def dp(s, i=0,j=len(s)-1, rmv=0):
	if dpp[i][j] != -1:
		return dpp[i][j]

	d = {'(':')','[':']', '{':'}'}
	d2 = {v: k for k, v in d.items()}

	if i>j:
		dpp[j][i]=0
		return 0
	elif i==j:
		dpp[i][j]=1 #we have one bracket, unbalanced, so we should delete it
		return dpp[i][j]

	if s[i] not in d:
		dpp[i][j]=dp(s, i+1, j)+1
		return dpp[i][j]
	elif s[j] not in d2:
		dpp[i][j]=dp(s, i, j-1)+1
		return dpp[i][j]
	else:
		s2 = s[i:j+1].split(d[s[i]])

		ii = 1
		while ii<len(s2):
			if s2[ii]=='':
				s2.pop(ii)
				s2[ii-1] += '+'
			else:
				ii += 1

		if len(s2)==1:
			if d[s[i]]==s[j]:
				dpp[i][j]=dp(s, i+1, j-1)
				return dpp[i][j]
			dpp[i][j]=min(dp(s, i+1, j), dp(s, i, j-1)) + 1
			return dpp[i][j]

		ks = [i+len(s2[0])]
		for ii in range(1, len(s2)):
			add = ks[ii-1]+len(s2[ii])+1
			if add - 1 != j:
				ks.append(add)

		s2 = s[i:j+1].split(d2[s[j]])

		ii = len(s2)-1
		while ii>=0:
			if s2[ii]=='':
				s2.pop(ii)
				s2[ii] += '+'
			else:
				ii -= 1

		if len(s2)==1:
			if d2[s[j]]==s[i]:
				dpp[i][j]=dp(s, i+1, j-1)
				return dpp[i][j]
			dpp[i][j]=min(dp(s, i+1, j), dp(s, i, j-1)) + 1
			return dpp[i][j]
		
		n = len(ks)
		ks.append(i+len(s2[0]) - 1) # as we have k+1:j for j-half
		for ii in range(1, len(s2)):
			add = ks[n + ii - 1]+len(s2[ii])+1
			if add-1 != j:
				ks.append(add - 1) # as we have k+1:j for j-half

		if d[s[i]]!=s[j]:
			res = [dp(s,i,k)+dp(s,k+1,j) for k in ks]
			dpp[i][j]=min(res)
			return dpp[i][j]
		else:
			res = [dp(s,i,k,0)+dp(s,k+1,j,0) for k in ks[:-1]]
			res.append(dp(s, i+1, j-1))
			dpp[i][j]=min(res)
			return dpp[i][j]

print(len(s)-dp(s))

'''
{([(]{)})]
#6

{}[]()()(((((({{{{{
#11=dp, len=8

{}[]()()(({{]} 
#4=dp, len = 10


{}]]]))))){{{}}}[}]]]
#10

{[{(){{}[[[]]{]}{}}}
#18
{ [{ () { {} [[ [] ] { ] }{ } } }
[{ () { {} [[ [] ] { ] }{ } } 0
{ () { {} [[ [] ] { ] }{ } } 1
() { {} [[ [] ] { ] }{ } 1
{ {} [[ [] ] { ] } {} 1
{ {} [[ [] ] { ] } 1
{} [[ [] ] { ] 1
[[ [] ] { ] 1
[ [] ] { 1
{ 1
2

'''

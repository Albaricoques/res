t = int(input())
step = 0
while step < t:
	x = input()
	#if len(x)%2==0:
	if min(x.count('1'),x.count('0'))%2 == 1:# and x.count('0')%2 == 1:
		print('DA')
	else:
		print('NET')
	#else:
	#	if 
	step += 1

"""B. 01 Game
time limit per test
1 second
memory limit per test
256 megabytes
input
standard input
output
standard output

Alica and Bob are playing a game.Initially they have a binary string 𝑠 consisting of only characters 0 and 1. 
Alice and Bob make alternating moves: Alice makes the first move, Bob makes the second move, Alice makes the third one, and so on. During each move, the current player must choose two different adjacent characters of string 𝑠 and delete them. For example, if 𝑠=1011001 then the following moves are possible:
delete 𝑠1 and 𝑠2: 1011001→11001;
delete 𝑠2and 𝑠3: 1011001→11001;
delete 𝑠4and 𝑠5: 1011001→10101;
delete 𝑠6and 𝑠7: 1011001→10110. 

If a player can't make any move, they lose. Both players play optimally. You have to determine if Alice can win.

Input
First line contains one integer 𝑡 (1≤𝑡≤1000) — the number of test cases.
Only line of each test case contains one string 𝑠 (1≤|𝑠|≤100), consisting of only characters 0 and 1.

Output
For each test case print answer in the single line. If Alice can win print DA (YES in Russian) in any register. Otherwise print NET (NO in Russian) in any register.

Example
Input
3
01
1111
0011

Output
DA
NET
NET

Note
In the first test case after Alice's move string 𝑠 become empty and Bob can not make any move.
In the second test case Alice can not make any move initially.
In the third test case after Alice's move string 𝑠 turn into 01. Then, after Bob's move string 𝑠 become empty and Alice can not make any move.
"""

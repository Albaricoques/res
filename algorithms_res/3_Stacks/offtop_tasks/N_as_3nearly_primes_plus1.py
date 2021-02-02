stdin = int(input())

minimum = 2*3 + 2*5 + 2*7 + 1

for i in range(stdin):
	n = int(input())
	if n<minimum:
		print("NO")
	else:
		print('YES')
		last = n - minimum + 1
		if last in [6, 10, 14]:
			print('6 10 15', last-1)
		else:
			print('6 10 14', last)

'''
	A. Captain Flint and Crew Recruitment
	time limit per test
	1 second
	memory limit per test
	256 megabytes
	input
	standard input
	output
	standard output

	Despite his bad reputation, Captain Flint is a friendly person (at least, friendly to animals). Now Captain Flint is searching worthy sailors to join his new crew (solely for peaceful purposes). A sailor is considered as worthy if he can solve Flint's task.

	Recently, out of blue Captain Flint has been interested in math and even defined a new class of integers. Let's define a positive integer 𝑥
	as nearly prime if it can be represented as 𝑝⋅𝑞, where 1<𝑝<𝑞 and 𝑝 and 𝑞 are prime numbers. For example, integers 6 and 10 are nearly primes (since 2⋅3=6 and 2⋅5=10), but integers 1, 3, 4, 16, 17 or 44

	are not.

	Captain Flint guessed an integer 𝑛
	and asked you: can you represent it as the sum of 4 different positive integers where at least 3

	of them should be nearly prime.

	Uncle Bogdan easily solved the task and joined the crew. Can you do the same?
	Input

	The first line contains a single integer 𝑡
	(1≤𝑡≤1000

	) — the number of test cases.

	Next 𝑡
	lines contain test cases — one per line. The first and only line of each test case contains the single integer 𝑛 (1≤𝑛≤2⋅105)

	 — the number Flint guessed.
	Output

	For each test case print:

	    YES and 4

	different positive integers such that at least 3 of them are nearly prime and their sum is equal to 𝑛
	(if there are multiple answers print any of them);
	NO if there is no way to represent 𝑛
	as the sum of 4 different positive integers where at least 3

	    of them are nearly prime. 

	You can print each character of YES or NO in any case.

	Example
	Input
	Copy

	7
	7
	23
	31
	36
	44
	100
	258

	Output
	Copy

	NO
	NO
	YES
	14 10 6 1
	YES
	5 6 10 15
	YES
	6 7 10 21
	YES
	2 10 33 55
	YES
	10 21 221 6
'''
n = int(input())

q = list()
clients = 0
while clients < n:
	x = [int(i) for i in input().split()]
	timex = x[0]*60 + x[1]

	while len(q)!=0 and q[0]<=timex:
		q.pop(0)

	if len(q)>x[2]:
		print(*x[:2])
		clients+=1
		continue

	if len(q)!=0 and q[len(q)-1]>timex:
		timex=q[len(q)-1]

	q.append(timex + 20)
	hours = (timex+20)//60
	print(hours, (timex+20)%60)

	clients += 1


'''F. Hairdresser
time limit per test: 1 second ; memory limit per test: 256 megabytes
input: standard input ; output: standard output

A hairdresser works in a salon. He spends 20 minutes per client and gets the next client from the queue, or waits until a client comes.
You are given the times of appearance of clients in the salon (in the order of their appearance).
Each client has an impatience parameter. It shows how many people he can tolerate in the queue before him. If at the point of an entrance there are more people in the queue than his impatience he leaves. A person that is being served counts as the person in the queue.
If the end of the service of the client coincides with the entrance of another client, we can think that at first, the client stops being served, and then the second client comes.
For each client, you should calculate the time a which the client leaves.

Input
The first line contains one integer n (1 ≤ n ≤ 100) — the number of clients.
Next n lines contain times of appearance and impatience of the clients. The time is represented by two integers: hours from 0 to 23 and minutes from 0 to 59. The impatience is represented by a non-negative integer that does not exceed 100. All times are different and they are given in the increasing order.
It is guaranteed that all the clients will be served before the midnight.

Output
The output file should contain n pairs of integers: the exit times in hours and minutes. If for a client the queue contains more people than his impatience parameter you can consider his exit time to be equal to his entrance time.

Example
Input
3
10 0 0
10 1 1
10 2 1

Output
10 20
10 40
10 2
'''
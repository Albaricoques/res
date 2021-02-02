import bisect
 
array_length = input()
a = [int(i) for i in input().split()]
a.sort()
queries_quantity = int(input())
 
lst = list()
for i in range(queries_quantity):
	start, end = [int(i) for i in input().split()]
	start_ind = bisect.bisect_left(a,start)
	end_ind = bisect.bisect_right(a,end)
	lst.append(end_ind - start_ind)
 
 
print(*lst)

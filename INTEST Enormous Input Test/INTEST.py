# We take a line as input
# Split in into 2 parts by blank space
# type cast those Strings to int
# And assign them to n and k
# n is for number of lines for input
# k is the number which is divisor
(n, k) = map(int, input().split(' '))

# ans will store the integers divisible by k
# currently it is set to 0, as no number is divisibleby k
ans = 0

# for loop will take input and test if number is divisible by k
for i in range(n):
    # take x as input and type cast to int
	x = int(input())
	#check if number divisible by k
	# increment ans if divisible
	# else continue
	if x % k == 0:
	    # ans+=1 is faster than ans++ or ans= and+1
		ans += 1

print(ans)

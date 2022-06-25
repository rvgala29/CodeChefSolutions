T = int(input())
for tc in range(T):
    # Will take a single line as input
    # And split the line in 2 inputs using a blank space
    # Map will assign the assign the values to a & b
	(a, b) = map(int, input().split(' '))
	ans = a + b
	print(ans)

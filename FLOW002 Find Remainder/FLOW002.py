# T is the number of test cases
# type casted to int
T = int(input())

# GO through each test case
for x in range(T):
    # Take a line as input, split into by blank space
    # Assign the valus to A and B
    A,B = map(int, input().split())
    # Print the remainder of A%B 
    # % is used to return remainder
    # A % B is read as:
    # A mod B, or A modulous B
    print(A % B)

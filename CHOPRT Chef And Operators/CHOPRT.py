# Iterate for the testCases
for i in range(int(input())):
    
    # Take a line as input
    # Split it on basis of a blank space
    # and type cast it to int
    # Assign the 2 ints to A and B
    (A, B) = map(int, input().split(' '))
    
    # Check relation and print the symbol
    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:
        print("=")

# Go over the testCases
for testCases in range(int(input())):
    #Take a line as input
    # Split on basis of blank space
    # Type Cast to int 
    # Map function will assign the value to A, B, and C
    (A, B, C) = map (int, input().split(' '))
    
    # Check if all angles add upto 180
    if A+B+C==180:
        print("YES")
    else:
        print("NO")

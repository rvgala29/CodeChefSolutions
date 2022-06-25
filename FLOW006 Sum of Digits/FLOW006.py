# T is input as String and type casted to int
T=int(input())

# iterate for loop
for i in range(T):
    # Take input and type cast it to int 
    num=int(input())
    # sum of digits is 0
    sum=0
    # to iterate over the number
    # convert num to string
    # Use for loop on the string to iterate
    # Or move over the string characters
    for j in str(num):
        # Type cast the character to int and add it to sum
        # sum+=1 is faster than sum++ or sum=sum+1 
        sum+=int(j)
    print(sum)

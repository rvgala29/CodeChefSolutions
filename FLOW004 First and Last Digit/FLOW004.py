# direclty use for loop to iterate over the testcases
# save time and memory to allocatre a memory space and assign it 
for i in range(int(input())):
    # take a line as input as String
    s = input()
    
    # directly access the first and last digit of number
    # type cast them to int
    # print the result
    # len(s) will return length
    # but the indexing starts from 0
    # Thus, there are length-1 indices or indexes
    print(int(s[0]) + int(s[len(s) - 1]))

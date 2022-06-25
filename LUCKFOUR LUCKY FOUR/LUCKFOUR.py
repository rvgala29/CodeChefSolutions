t = int(input())
for i in range(t):
    # fours variable to count the occurences
    fours = 0
    # take th enumber input
    num = int(input())
    while(num):
        # find if last digit is 4 or not
        # 14%10 gives 4, remainder, or simply the last digit
        # if its 4 increment the counter
        if(num%10 == 4):
            fours +=1
        # remove the last digit of number and change values
        # 14%10 is 1.4, we type cast it to int
        # So 1.4 becomes 1
        num = int(num/10)
    print(fours)

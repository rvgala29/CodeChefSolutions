# take test case input
t = int(input())
for i in range(t):
    # currently the reversed number is 0
    reverse = 0
    # take the number input
    # type cast it to int
    num = int(input())
    # while loop will iterate till num is not 0
    while(num):
        # this remainder is the last digit of number
        # 45%10=5
        remainder = num%10
        # We will add the digit to reverse
        # First increase the number of digits of reverse
        # Because if we ad 4+5=9, but we want 54
        # which is 50 + 4
        reverse =reverse*10+remainder
        # Remove the last digit from number
        num = int(num/10)
    print(reverse)

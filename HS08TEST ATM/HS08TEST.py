# Take input as line
# Split on basis of blank space
# Type cast to float
# Assign the values to n, atm
n,atm=map(float,input().split())
n=int(n)
# Checking 2 conditions:
# First, if the sum of amount to be withdrawn and transaction charge 
# is greater than bank balance
# Second, check if amount to be withdrawn is multiple of 5 or not
if (n+0.5<=atm and n%5==0):
    # If the condition is satishfied, print the balance after transaction
    print(float(atm-n-0.5))
else:
    # If the conditions are failed, print the original balance
    print(float(atm))

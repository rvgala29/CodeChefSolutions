# cook your dish here
#directly iterrate over the test cases
for testCase in range(int(input())):
    # not required but, question required to iterate over it
    str_len = int(input())
    # the DNA strand is stored in it
    str_DNA = str(input())
    # store complementary strand
    str_comp=""
    #iterate over each letter in DNA strand
    for i in str_DNA:
        # if the letter A is in i, it will add T 
        if 'A' in i:
            str_comp+='T'
        elif 'T' in i:
            str_comp+='A'
        elif 'C' in i:
            str_comp+='G'
        elif 'G' in i:
            str_comp+='C'
    print(str_comp)

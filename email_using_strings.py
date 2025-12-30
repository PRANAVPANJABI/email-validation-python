## Using the string functions for this email validation code 

email = input("Enter an email : ") # g@g.in

k = 0 ## A variable made
j = 0 ## Another variable
d = 0 ## Another variable

if len(email) >= 6 :                    ## 1st condition checked, length of mail greater than 6
    if email[0].isalpha():              ## 2nd condition checked, 1st character in gmail should be alphabet
        if ("@" in email) and (email.count("@") == 1):      ## 3rd condition checked, is there @ in the email and it's count is 1.
            if (email[-4] == ".") ^ (email[-3] == "."):     ## 4th condition checked, the "." should be at -4 or -3 position(3rd from last or 4th from last). We do not use OR condition bc even if we have "." on both -3 and -4 position, it steals gives true. Also, "^" this is XOR condtion we used because it will give true when only 1 of the 2 condition is true.
                for i in email :
                    if i.isspace():    # 5 Checks for spaces
                        k = 1
                    elif i.isalpha():   # 5 Checks for alphabets
                        if i.isupper():   # P==P
                            j = 1
                    elif i.isdigit():       ## 5 Check for digit
                        continue
                    elif i =="_" or i =="." or i =="@":
                        continue
                    else :                      ## For anything other this like &, #,$,etc.
                        d = 1
                if k == 1 or j == 1 or d == 1:        ## "or" is used bc, if both or any of the 2(i and j) are 1 then wrong email case comes
                    print('wrong email 5')
                else :
                    print('Email is valid')
            else :
                print('Wrong email 4')
        else :
            print('Wrong email 3')
    else :
        print('Wrong email 2')

else :
    print('Wrong email 1')
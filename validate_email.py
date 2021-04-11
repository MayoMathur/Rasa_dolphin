import re
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

def isValidEmail(email):
 
    if(re.search(regex, email)):
        return True
 
    else:
        return False



 
def isValidPhone(s):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    return Pattern.match(s)
 


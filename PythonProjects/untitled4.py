def is_palindrome(s):
    control=""
    for i in s:
        if(i==s[len(s)-1]):
            control="true" 
        else:
            control="false"
            break
    return control        
is_palindrome("banana")

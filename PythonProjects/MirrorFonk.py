def mirror(s):
    ters_s=s[::-1]
    new_s=s+ters_s
    print('\'{0}\''.format(new_s))
    return new_s
mirror("good")
mirror("yes")
mirror('Python')
mirror("")
mirror("a")
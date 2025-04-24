def remove_letter(letter, strng):
    new_str=""
    for i in strng:        
        if(i!=letter):
            new_str+=i
    print('\'{0}\''.format(new_str))
    return new_str
remove_letter("a","apple")
remove_letter('a', 'banana')
remove_letter('z', 'banana')
remove_letter('i', 'Mississippi')
            
    
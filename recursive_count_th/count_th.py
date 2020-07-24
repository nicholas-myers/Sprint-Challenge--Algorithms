'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # TBC
    # could break the word into a list 
    # then get every combination of letters
    # no loops?
    # check first two indices
    # always pop the first index and reoccur
    if word == "":
        return 0
    elif word == "th":
        return 1
    elif len(word) > 2:
        first = word[0]
        second = word[1]
        is_the = first + second
        new_word = word[1:]
        if is_the == "th":
            # if the first two contain "th" return reoccured with just th to get the plus 1
            return count_th(new_word) + count_th("th")
        else:
            return count_th(new_word)
    else:
        return 0
            
        
        
    
count_th("thhtthht")
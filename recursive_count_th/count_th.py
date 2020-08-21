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
    # check if the word is empty
    if word == "":
        return 0
    # check if the word is th
    elif word == "th":
        return 1
    # check if the word is greater than two characters
    elif len(word) > 2:
        # combine the first two characters
        first = word[0]
        second = word[1]
        is_the = first + second
        # remove the first character
        new_word = word[1:]
        # 
        if is_the == "th":
            # if the first two contain "th" return reoccured with just th to get the plus 1
            return count_th(new_word) + count_th("th")
        else:
            # other wise call again with teh reduced word
            return count_th(new_word)
    else:
        # if we don't find th return 0
        return 0
            
        
        
    
count_th("thhtthht")
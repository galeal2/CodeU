    '''
        the function (find_alphabet)
        - takes a single parameter, a dictionary
        - iterates through the dictionary and adds the first letter of each word (if is not already in the dictionary) to the alphabet (a list of letters)
        - using the function 'find_order' and 'find_position' the letters are added to the alphabet in the right order
        - at the end the function 'add' is used to add all the letters existed in the dictionary but that were not added to the alphabet
        Returns: a list of characters (the alphabet)
    '''

def find_alphabet(dictionary):
    '''
        Input: a dictionary(a list of words in lexicographic order) of all words in an unknown/invented language
        Output: the alphabet (an ordered list of characters)
    '''
    
    alphabet = []
    for i in range(len(dictionary)-1):
        if dictionary[i][0] not in alphabet:
            alphabet.append(dictionary[i][0])
        if dictionary[i][0] == dictionary[i+1][0]:
            letter = find_order(dictionary[i],dictionary[i+1], alphabet)
            if letter:
                alphabet = list((find_position(letter, alphabet)))
    add(dictionary, alphabet)
    return (alphabet)

        
def find_order(word1, word2, alphabet):
    '''
        Input: 2 words and an alphabet
        Output: returns the first two letters (as a string) that are different in the given words
    '''
    order = ''
    for c in range(1,len(word1)):
        if word1[c] != word2[c] and (word1[c] not in alphabet or word2[c] not in alphabet):
            order = word1[c] + word2[c]
            return order
    return order

def find_position(order, alphabet):
    '''
        Input: - a string (order) that contains 2 letters and shows in which order the letters should appear in the dictionary
               - an alpabet
        Output: an alphabet with the letters added in the right order       
    '''
    
    if order[0] not in alphabet and order[1] not in alphabet:
        alphabet += [order[0], order[1]]
        return alphabet
    
    alphabet_order = ''
    if order[1] in alphabet and order[0] not in alphabet:
        for c in alphabet:
            if c == order[1]:
                alphabet_order += order[0]
            alphabet_order += c
            
    if order[0] in alphabet and order[1] not in alphabet:
        for c in alphabet:
            if c != order[0]:
                alphabet_order += c
            else:    
                alphabet_order += c
                alphabet_order += order[1]

    
    return alphabet_order    

def add(dic, alphabet):
    '''
        - the function takes a dictionary (dic) and an alphabet as parameters
        - checks if all the letters from the dictionary are in alphabet
        if one is missing, the letter is appended to the alphabet
    '''
    for w in dic:
        for c in w:
            if c not in alphabet:
                alphabet.append(c)
                
def main():
    
    dictionary = ['ART', 'TAT', 'CAT', 'CAR']
    assert find_alphabet(dictionary) == ['A', 'T', 'R', 'C']

    dictionary_2 = ['ART', 'ARC', 'ACD', 'CAT', 'CRC']
    assert find_alphabet(dictionary_2) == ['A', 'T', 'R', 'C', 'D']

    dictionary_3 = ['BACD', 'BACE', 'ACDE']
    assert find_alphabet(dictionary_3) == ['B', 'D', 'E', 'A', 'C']

    dictionary_4 = ['FG']
    assert find_alphabet(dictionary_4) == ['F', 'G']

    dictionary_5 = ['aBC', 'aDB', 'CDA']
    assert find_alphabet(dictionary_5) == ['a', 'B', 'D', 'C', 'A']
if __name__ == '__main__':
    main()

class Dictionary():
    '''
        Dictionary class takes a list as argument
        and it has two methods
        isWord(String) - Returns whether the given string exist in the dictionary.
        isPrefix(string) - Returns whether the given string is a prefix of at least one word in the
                        dictionary.
    '''
    
    def __init__(self, array = []):
        self.dictionary =  array
        
    def isWord(self, word):
        if word in self.dictionary:
            return True
        return False

    def isPrefix(self, prefix):
        for word in self.dictionary:
            if word[:len(prefix)] == prefix:
                return True
        return False


def find_word(rows, columns, grid, visited, i, j, string, dictionary, words):
    '''
        The function receives the: - number of rows,
                                   - number of columns,
                                   - a grid, 2-dimensional array of characters (of the native char data type),
                                   - position i and j in the grid
                                   - candidate word
                                   - and the dictionary.
                                   - a set where the vaild words are added      
    '''
    # add the word to the set if is valid
    if dictionary.isWord(string):
        words.add(string)
    row = i - 1 
    while row <= i + 1 and row < rows:
        col = j - 1
        while col <= j + 2 and col < columns:
            word = string + grid[i][j]
            if row >= 0 and col >= 0 and visited[row][col] == False and dictionary.isPrefix(word):
                find_word(rows, columns, grid, visited, row, col, word, dictionary, words)
            
            col += 1
        row += 1    

def find_words(rows, columns, grid, dictionary):
    '''
        The function receives the: - number of rows,
                                   - number of columns,
                                   - a grid, 2-dimensional array of characters (of the native char data type),
                                   - and the dictionary.
        
        Returns the set of all words found in the grid.

    '''
    # list to keep track of the visited positions
    visited = [[False for i in range(columns)] for i in range(rows)]
    
    words = set()
    string = ''
    for i in range(0, rows):
        for j in range(0, columns):
            find_word(rows, columns, grid, visited, i, j, string, dictionary, words)
    return words

# tests    
def main():
    grid = [['A', 'A', 'R'],
            ['T', 'C', 'D']]
    dictionary = Dictionary(["CAR", "CARD", "CART", "CAT"]) 
    assert find_words(2, 3,grid, dictionary) == {'CAR', 'CAT', 'CARD'}
    dictionary_2 = Dictionary() 
    assert find_words(2, 3,grid, dictionary_2) == set()

if __name__ == '__main__':
    main()




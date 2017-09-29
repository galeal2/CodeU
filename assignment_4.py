
def count_islands(rows, columns, grid):
    '''
        INPUT - # of rows
              - # of columns
              - 2-dimensional array of booleans
        RETURN - number of islands      
    '''
    
    visited = [[False for i in range(columns)] for i in range(rows)]
    count  = 0
    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == 'T' and not visited[row][col]:
                check_tile(rows, columns, row, col, grid, visited)
                count += 1
    

    return count
        
def check_tile(rows, columns, x, y, grid, visited):
    '''
    INPUT - # of rows
          - # of columns
          - position x, y on the grid
          - 2-dimensional array of booleans (grid)
          - 2-dimensional array of visited positions
    '''
    
    if grid[x][y] == 'F' or visited[x][y]:
        return
    visited[x][y] = True

    if x > 0:
        check_tile(rows, columns, x - 1, y, grid, visited)
    if x < rows-1:
        check_tile(rows, columns, x + 1, y, grid, visited)
    if y > 0:
        check_tile(rows, columns, x, y -1 , grid, visited)
    if y < columns - 1:
        check_tile(rows, columns, x, y + 1, grid, visited)

def main():
    grid = [['F', 'T', 'F', 'T'],
            ['T', 'T', 'F', 'F'],
            ['F', 'F', 'T', 'F'],
            ['F', 'F', 'T', 'F'] ]
    assert count_islands(4, 4, grid) == 3

    grid_2 = [['T', 'F', 'F', 'T'],
            ['F', 'T', 'F', 'F'],
            ['F', 'F', 'T', 'F']]

    assert count_islands(3, 4, grid_2) == 4

    grid_3 = [['F', 'F', 'F']]
    assert count_islands(1, 3, grid_3) == 0

    grid_4 = [[]]
    assert count_islands(0, 0, grid_4) == 0

if __name__== '__main__':
    main()

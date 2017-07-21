# Rearranging cars

def rearrange_cars(cars,order):
    '''
        Input: - 2 list of integers
                cars =  a list of integers that represents the cars
                order = a list of integers that represents in which order should the cars be rearranged
        Returns a list that contains all the moves made to get the rearrangement        
                
    '''
    empty = find_zero(cars) 
    moves = []
    dic = build_dic(order)
    for i in range(len(cars)):
        if cars[i] != order[i] and cars[i]!= 0:
            car_pos = dic[cars[i]]      
            
            if car_pos != empty:
                moves.append('move from {} to {}'.format(empty, car_pos))
                
            cars[empty], cars[car_pos] = cars[car_pos], cars[empty]
            empty = car_pos
            moves.append('move from {} to {}'.format(empty, i)) 
    
            cars[i], cars[empty] = cars[empty], cars[i]
            empty = i

    return moves   
            

def build_dic(lst):
    '''
        Input: a list
        It bulids a dictonary from the list 
    '''
    dic = {}
    for i in range(len(lst)):
        dic[lst[i]] = i
    return dic

def find_zero(lst):
    '''
        Input: a list of integers
        Returns: position of zero (0) in the list
    '''
    for i in range(len(lst)):
        if lst[i] == 0:
            return i



def main():

    assert rearrange_cars([1,2,0,3], [3,1,2,0]) == ['move from 2 to 1', 'move from 1 to 0', 'move from 0 to 3']
    assert rearrange_cars([0,5,3,1,4,2],[5,4,3,2,1,0]) == ['move from 0 to 1', 'move from 1 to 4', 'move from 4 to 3', 'move from 3 to 5']
    assert rearrange_cars([1,2,3,0], [1,2,3,0]) == []
    
if __name__ == '__main__':
    main()

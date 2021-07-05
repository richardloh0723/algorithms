def linear_search(list, target):
    """
    Returns the index position
    of the target if found, else
    returns None
    """
    for i in range(0,len(list)):
        if(list[i] == target):
            return i
    return None

def binary_search(list,target):
    """
    Returns the index position
    of the target if found, else
    returns None
    """
    first = 0 # 0 1 2 3 4 ... n-1
    last = len(list) - 1 #index of last value

    #Calculate the midpoint of list
    while first <= last:
        # calculate the midpoint with
        # floor division.
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def recursive_binary_search(list,target):
    if len(list) == 0:
        return False
    else:
        # calculate the midpoint by dividing
        # the list by 2
        midpoint = (len(list))//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:],target)
            else: # when the value of the midpoint is greater than the target
                #call the binary search function again
                #beginning -> midpoint
                return recursive_binary_search(list[:midpoint],target)
        
def verify(result):
    print("Target found: " , result)

numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers,155)
verify(result)
result = recursive_binary_search(numbers,6)
verify(result)

# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
    
        for j in range(i + 1, len(arr)): 
            if arr[j] < arr[cur_index]:
                smallest_index = j
                temp = arr[cur_index]
                arr[cur_index]=arr[smallest_index]
                arr[smallest_index] = temp

    return arr

### Print Test ############################################
test = [1, 7, 4, 6, 3, 2, 5, 9, 10, 8, 0]
selection_sort(test)
for x in test:
    print(x)
###########################################################


# Bubble Sort function ####################################
def bubble_sort( arr ):
    # for every number in the array to 0
    for i in range(0, len(arr)):
        # When the number is above zero and the number before it is less, its in the right spot.
        while i > 0 and arr[i] < arr[i - 1]:
            # If not swap them.
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            # Check out the spot below the current number.
            i -= 1
    # return the array        
    return arr

# Removes duplicates from list
    # for i in range(len(arr) - 1):
    #     for i in range(len(arr) - 1 - i):
    #         if arr[i] > arr[i + 1]:
    #             arr[i + 1], arr[i] = arr[i], arr[i + 1]
    #         elif arr[i] == arr[i + 1]:
    #             del arr[i]

    # return arr

### Print Test ############################################
test = [2, 7, 4, 1, 1, 10, 6, 6, 8, 3, 5, 0, 9]
bubble_sort(test)
for x in test:
    print(x)
###########################################################











# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

    # return arr
# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
    
        for j in range(i + 1, len(arr)): 
            if arr[j] < arr[cur_index]:
                smallest_index = j
                temp = arr[cur_index]
                arr[cur_index]=arr[smallest_index]
                arr[smallest_index] = temp



        # TO-DO: swap




    return arr

test = [1, 7, 4, 6, 3, 2, 5, 9, 10, 8, 0]
selection_sort(test)
for x in test:
    print(x)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j -1]: 
            arr[j], arr[j - 1] = arr[j - 1], arr[j] 
            j -= 1
            
    return arr

test = [2, 7, 4, 1, 10, 6, 8, 3, 5, 0, 9]
bubble_sort(test)
for x in test:
    print(x)

# STRETCH: implement the Count Sort function below
# def count_sort( arr, maximum=-1 ):

    # return arr
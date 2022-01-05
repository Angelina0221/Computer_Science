sorted_list = [1,4,6,9,11,13]
target = 13
def binary_search(sorted_list, target):
    left_idx = 0
    right_idx = len(sorted_list - 1)

    #repeat steps-
    #1calculate the middle between two points
    #2 check if the value at the middle index equals our target
    #3 if no and target is greater than middle value, update (move ) the right pointer(right bound)
    #4 if no and target is less than middle value, update (move )the left pointer(left bound)
    #5 if the value doesn't exist in the list , return -1
    while(left_idx <= right_idx):
        middle_idx = int((left_idx + right_idx) / 2)
        if(sorted_list[middle_idx] == target):
                    return middle_idx
        elif(target < sorted_list[middle_idx]):
                    right_idx = middle_idx -1
        else:
                    left_idx = middle_idx + 1

        return -1 #if the value isn't in the list, return -1
result  = binary_search(sorted_list, target)
print("the target number is at ist index:", result)



sorted_list = [1,4,6,8,10,13]
target = 10
def binary_search(sorted_list, target):
    left_indx = 0
    right_indx = len[sorted_list - 1]

    while (left_indx <=right_indx):
        middle_indx = int((left_indx + right_indx)/2)
        if(sorted_list[middle_indx] == target):
                return middle_indx
        elif (target < sorted_list[middle_indx]):
                right_indx = middle_indx -1
        else :
                left_indx = middle_indx +1
        
        return -1

result = binary_search(sorted_list, target)
print(result)




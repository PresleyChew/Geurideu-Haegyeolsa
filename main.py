#Test for input validity with respect to row, if for particular row specified
#by row contains num, then return boolean false, else true.
def isValidInputRow(arr, row, num) -> bool:
    return num not in arr[row]

#Test for input validity with respect to col, if for particular column specified
#by column contains num, then return boolean false, else true.
def isValidInputColumn(arr, col, num) -> bool:
    for i in range(9):
        if arr[i][col] == num:
            return False
    return True        

#Test for input validity with respect to the 3 by 3 grid it is in, if number specified
#by num is within box containing the col and row, then return boolean false,
#else true.
def isValidInputBox(arr, col, row, num) -> bool:
    newCol = (col // 3) * 3
    newRow = (row // 3) * 3
    for i in range (3):
        for x in range (3):
            if arr[newRow+i][newCol+x] == num:
                return False
    return True

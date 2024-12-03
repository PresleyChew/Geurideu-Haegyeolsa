import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Geurideu-Haegyeolsa")
        self.setGeometry(500,250,500,500)
        
        label = QLabel("BoilerPlate",self)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    

if __name__=="__main__":
    main()    
    grid =[[0 for x in range(9)]for y in range(9)]
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    sudokuSolver(grid)
    printGrid(grid)


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
def isValidInputBox(arr, row, col, num) -> bool:
    newCol = (col // 3) * 3
    newRow = (row // 3) * 3
    for i in range (3):
        for x in range (3):
            if arr[newRow+i][newCol+x] == num:
                return False
    return True

def findEmptyCell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i,j
    return None

def sudokuSolver(grid):
    emptyCell = findEmptyCell(grid)
    if not emptyCell:
        return True
    row, col = emptyCell
    for num in range(1,10):
        if(isValidInputRow(grid,row,num) and (isValidInputColumn(grid,col,num)) and (isValidInputBox(grid,row,col,num))):
            grid[row][col] = num
            
            if sudokuSolver(grid):
                return True

            grid[row][col] = 0
    return False

def printGrid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))



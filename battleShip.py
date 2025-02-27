""" Pseudocode 
        Prompt user input for total rounds of the game
        Initialize the total game score
        for each round:
            Validate the user input for board size and number of ships
            Handle invalid entries 
            Set the board and ships.
            for each shot in the round:
                Request the user to input the assumed ship coordinates
                Display the Hit message (Hit or Miss)
                Display the full board with updated attempts results 
            Show the final state of the board
            Display the user final score of this round
        Display the user final score of the game
"""

""" Import the libraries if appliable

"""
""" Define global variables if appliable

"""

# Suggest to start by understanding the code in the main function.
# Then proceed with the coding.

import random

def addShip(board, numShips):
    """ Function Description:
            Randomly places the specified number of ships ('S') on the board.
        Parameter(s): 
            board : The list of lists representing the game board
            numShips [int]: The number of ships that user wants on the board
        Return: None   
    """
    size = len(board) # Len will get the number of rows in the board.

    while numShips > 0:
        # I used size - 1 since the coordinates on the board start at zero, and size will add an extra coordinate.
        row = random.randint(0, size - 1) 
        col = random.randint(0, size - 1)

        # This if statement adds the ship on the board, and checks whether or not a ship is already placed in a specifc position.
        if board[row][col] == "~":
            board[row][col] = "S"
            numShips -= 1

def checkSetUpError(size, numShips):
    """ Function Description:
            Validates user input for the size of the board and the number of ships.
        Parameter(s): 
            size [int]: The size of the board
            numShips [int]: The number of ships
        Return [Boolean]: Return True if an error is found or False if there is no error.
    """
    # If statements check for errors.
    if (size < 2 or size > 5):
        return True
    
    maxShips = ((size * size) - 2)

    if (numShips < 1 or numShips > maxShips):
        return True

    return False

def checkFireError(board, row, col):
    """ Function Description:
            Validates user input for the coordinates to shot a ship
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user. 
        Return [Boolean]: Return True if an error is found or False if there is no error.   
    """
    # Since the board starts at index 0, it's necessary to subtract the length of the board by one, or you will get an index error.
    if (row > (len(board) - 1) or row < 0):
        return True
    
    elif (col > (len(board) - 1) or col < 0):
        return True
    
    elif (board[row][col] == "X" or board[row][col] == "O"):
        return True

    else:
        return False

def createBoard(size):
    """ Function Description:
            Creates a size-by-size game board initialized with '~'
        Parameter(s):
            size [int]: The size of the board which will be used to create a board of size x size
                        Example: size 2 will create [ ['~', '~'], ['~', '~']]
        Return: board which is a list of lists  
    """
    board = []
    for i in range(size):
        board.append(["~"] * size) # This creates multiple lists in a list, and will also make more cells by multiplying it with the user's size input.
    return board

def displayBoard(board, round=True):
    """ Function Description:
            Displays the current state of the board.  If round is True then print out the current
            state of the board without showing the ships 'S'.  Else round is False then print out the
            current state of the board showing hits 'X', misses 'O', ships that have not been hit 'S'
            and everything else '~'.
        Parameter(s):
            board : The list of lists representing the game board.
            round [Boolean] : True if you are print the board after each shot and False to display
            the end of a round version.  Default value of True.
        
        Return: None  
    """
    for i in board:
        currentBoard = [] # This will create the same amount of rows from the original board.
        for cell in i:
            if cell == "S" and round: # This will hide all the ships be replacing it with "~".
                currentBoard.append("~")
            else:
                # This will display the board when the round is false, showing the ships, hits, and misses.
                currentBoard.append(cell)
        print("".join(currentBoard))

def fireShot(board, row, col):
    """ Function Description:
            Marks a shot on the board.
        Parameter(s):
            board : The list of lists representing the game board
            row [int]: The row coordinate entered by the user.
            col [int]: The col coordinate entered by the user. 
        Return[Boolean]: Return True if a ship was hit and False if the shot missed a ship.     
    """  
    if (board[row][col] == "S"): # Here, the program looks at the chosen cell from the chosen row since they are still lists, but are displayed as coordinates.
        board[row][col] = "X"
        return True
    else:
        board[row][col] = "O"
        return False 

def playRound(board, numShips):
    """ Function Description:
            Main logic for playing one round 
            
            Pseudocode:
            Keep track of number of shots for the round
            Keep track of the score (number of hits) for the round
            Loop until user fires all their shots
                Ask user to enter coordinates for their shot.  Input two numbers separated by a space.
                Validate the shot coordinates using checkFireError function
                Fire a shot using the fireShot function
                Output if the shot is a hit or a miss
                display the board after the shot has been taken displayBoard(board)
            Output "End of round X"
            display the board at the end of the round displayBoard(board, False)
    
        Parameter(s):
            board : The list of lists representing the game board
            numShips [int]: The number of ships
        Return [int]: The number of hits (ships that were hit) for the round.   
    """
    hits = 0
    shotCount = 1

    # numShips is used to mimic the player's number of shots. This is possible since they are both equal.
    while numShips > 0:

        cords = input("Enter row and column to take a shot (e.g., 2 3): ").split(" ") # The split method seperates the numbers where a space exists.
        row = int(cords[0])
        col = int(cords[1])

        if (checkFireError(board, row, col)): 
            print("You will need to enter valid coordinates.") # This will print if the function returns True.
    
        elif (fireShot(board, row, col)):
            print(f"Shot {shotCount} is a Hit!")
            hits += 1
            shotCount += 1
            displayBoard(board, round=True)
            numShips -= 1
        
        else:
            print(f"Shot {shotCount} is a Miss!")
            displayBoard(board, round=True)
            numShips -= 1
            shotCount += 1

    print("End of round:")
    displayBoard(board, round=False) # This board will show all the ships, including the player's hits and misses.

    return hits

totalScore = 0

def main():    
    """ Function Description:
            Play the game in a designated number of rounds and present the final score to the user.
            You can not change the code in the main function.  If student changes the main function code
            then they will lose 25 marks.
        Parameter(s): No parameters
        Return: None  
    """
    currentRound = 0
    numRounds = int(input("Enter the number of rounds of Battleship you want to play: "))
    flag = True
    while currentRound < numRounds:
        while flag:
            size = int(input("Enter the size of the board: "))
            numShips = int(input("Enter the number of ships: "))
            flag = checkSetUpError(size, numShips)
            if (flag == False):
                break
            else:
                print("You will need to enter the size of the board and number of ships again.")
            
        board = createBoard(size)
        addShip(board, numShips)
        print(f"\nRound {currentRound + 1}:\n")
        hits = playRound(board, numShips)
        global totalScore
        totalScore += hits
        currentRound += 1
    print(f"\nFinal Score after {numRounds} round(s) is {totalScore} out {numShips * numRounds}.")
    return

if __name__ == '__main__':
    main()

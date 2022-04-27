from operator import indexOf


print("TIC-TAC-TOE")

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# function for printing game board
def print_board(board):
    for row in board:        
        for slot in row:
            print(f"{slot} ", end="")
        print()

print_board(board)

# function to quit the game
def quit(user_input):
    if user_input == "q":
        print("Thanks for playing :)")
        return True          # while loop will run
    else:
        return False

def boundaries(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is out of bounds.")      # T/F depending on user input
        return False
    else: 
        return True

# function to check input
def check_input(user_input):
    # check it it is a number
    if not isnum(user_input):
        return False
    user_input = int(user_input)
    # check if its 1-9
    if not boundaries(user_input):
        return False

    return True


# fuction to check if uuser input is a number or not
def isnum(user_input):  
    if not user_input.isnumeric():
        print("Please enter a valid num.")
        return False
    else:
        return True

def if_taken(user_input):
    
# all the functions will return true therefore, this while loop will run for every function

while True:
    user_input = input("Please a enter a position 1 through 9 or enter 'q' to quit: ")
    if quit(user_input):
        break          # if user input is q, if statemrent will break
    if not check_input(user_input):     # if check_input returns false
        print("Please try again.")
        continue
    user_input = int(user_input) - 1     # in the game board, index starts from 0, but user input is from 1-9
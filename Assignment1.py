#CSC 131 Assignment 1 
#Christina Zhou
#Fall 2018

#In this assignment we implement a simple two player tic- tac toe game. 
#The game is played by drawing a 9 space grid. One player is "X" and the other is "O"
#Players take turns choosing one of the 9 spaces by marking the space with their symbol. 
#When a player has 3 symbols in a row, column, or diagonal, they win.  
#A space may be occupied by only one symbol, so blocking your opponent is an important strategy.  
#If all of the spaces are occupied by a symbol, and neither player has 3 symbols in a row, column, or diagonal, the result is a tie game. 

#the board
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#copy of the board for positions
oGboard = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#empty board
eboard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

#takes a board (a list) as a parameter and draws the symbols in the parameter list, 3 on each row. 
#Note that this function can also be used to draw the position numbers in the instructions.

def drawBoard(board):
   
   print(board[0], board[1], board[2])
   print(board[3], board[4], board[5])
   print(board[6], board[7], board[8])

 
   return board
#takes the board (a list) and a player's name as parameters and prompts for and gets the players next move.
#This function should make sure that the input is valid.  To be valid, the user's input must be between 1 and 9.
#It must also be the position of an empty space (not already occupied).  
#If the input is invalid, your function should print an appropriate message and ask for the input again.
#It should keep doing this until the input is valid.

def getMove(board, name):
   global oGboard
   move = int(input("enter your move "))
   
   if (move < 1 or move > 9):
      print("invalid input, please enter your move using these positions")
      drawBoard(oGboard)

   elif ((eboard[move-1] == "X") or (eboard[move-1] == "O")): 
      print("that position is already taken, try again")
      
   else:
      
      eboard[move-1] = name
    
   
      return move; 
   
#Create a win() function that takes the board (a list) and a player's symbol as parameters.  It should return True if the symbol is in 3 consecutive positions in a row, column, or diagonal.  It should return False otherwise.  
def win(board, symbol):
      
   if (board[0] == symbol and board[1] == symbol and board[2] == symbol):
      win = True
      print ("you win! (r1) ")
      
   elif (board[3] == symbol and board[4] == symbol and board[5] == symbol ):
      win = True
      print ("you win! (r2)")
   elif (board[6] == symbol and board[7] == symbol and board[8]== symbol):
      win = True
      print ("you win! (r3)")

   elif (board[0] == symbol and board[3] == symbol and board[6]== symbol):
      win = True
      print ("you win! (c1)")

   elif (board[1] == symbol and board[4] == symbol and board[7]== symbol):
      win = True
      print ("you win! (c2)")

   elif (board[2] == symbol and board[5] == symbol and board[8]== symbol):
      win = True
      print ("you win! (c3)")

   elif (board[0] == symbol and board[4] == symbol and board[8]== symbol):
      win = True
      print ("you win! (d1)")
   
   elif (board[2] == symbol and board[4] == symbol and board[6]== symbol):
      win = True
      print ("you win! (d2)")
   else:
      win = False

   return win 

#Create a tieGame() function that takes the board (a list) as a parameter.  If any space is not yet occupied, then it should return False. It should return True if every space is occupied. 
def tieGame(board):
   count = 0
   n=0
   for n in range(9):
      if board[n] == "X" or board[n] == "O":
         count += 1 
      else:
         return False
   if(count == 9):
      return True

#main method, constructs the board and the tic tac toe game. 
#tests to see if there is a winner, or if it is a tie game 
#prints the name of the winner
def main():
   global board 
   print ("This program will allow two players to play the game of tic-tac toe")
   #go back fix excape characters
   print ("Player one has \'X', and Player two has \'O'")
  
   name1 = str(input("enter the name of player 1 "))
   
   symb1="X"
   
   name2 = str(input("enter the name of player 2"))
  
   symb2 = "O"

   drawBoard(board)

   print(name1, "you start. You are playing as \'X'")
   
   while(win(board, symb1) != True and win(board,symb2) !=True and tieGame(board) !=True):
      print(name1, end = " ")
      getMove(board, symb1)
      drawBoard(eboard)
      tieGame(eboard)
      print(name2, end = " ")
      getMove(board,symb2)
      drawBoard(eboard)
      tieGame(eboard)
      
      board = eboard    
 
   if(win(board,symb1) == True):
      print(name1, "you Win!")
   elif(win(board,symb2) == True):
      print(name2, "you Win!")

   else:
      print("Tie game! Game over.")
  


main()   






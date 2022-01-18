# Will print the board in order to let the players know whats going on.
def print_board(tablero):
 print ("", tablero[0],tablero[1],tablero[2], "\n", tablero[3],tablero[4],tablero[5], "\n", tablero[6], tablero[7], tablero[8])



# Calls the other 3 functiones, if any of them is true, we have a winner. Then it calls "check_who" to know whose winning move it was.
def check_win (tablero,n_turno):
   if (check_horizontals(tablero) or check_verticals(tablero) or check_diagonals(tablero) == True):
      print(("Ganó el jugador {}").format(check_who(n_turno)))
      return True
   else:
      return False

# Checks if any horizontal line is a winner
def check_horizontals(tablero):
   if (tablero  [0] == tablero [1] and tablero [0] == tablero [2]):
      return True
   elif (tablero [3] == tablero [4] and tablero [3] == tablero [5]):
      return True
   elif (tablero [6] == tablero [7] and tablero [6] == tablero [8]):
      return True
   else:
      return False

# Checks if any vertical line is a winner
def check_verticals(tablero):
   if (tablero [0] == tablero [3] and tablero [0] == tablero [6]):
      return True
   elif (tablero [1] == tablero [4] and tablero [1] == tablero [7]):
      return True
   elif (tablero [2] == tablero [5] and tablero [2] == tablero [8]):
      return True
   else:
      return False

# Checks if any diagonal is a winner
def check_diagonals(tablero):
   if (tablero [0] == tablero [4] and tablero [0] == tablero[8]):
      return True
   elif (tablero [2] == tablero [4] and tablero [2] == tablero [6]):
      return True
   else:
      return False

# We know that even turns are "X" and odd ones are "O" so it checks whose turn it is and it returns the player
def check_who(n_turno):
   if n_turno % 2 == 1:
      return "X"
   else:
      return "Ø"


# Still needs work. The idea is to check if a move can be done, and if it can´t, to ask for another move. Right now i just points the former
def check_legal (tablero,movimiento):
   if (movimiento > 8 or movimiento < 0):
      print("Movimiento Ilegal mayormenor")
      return False
   elif tablero [movimiento] == "X" or tablero[movimiento] == "O":
      print("Movimiento Ilegal ocupado")
      return False
   else:
      return True

if __name__ == '__main__':
   tablero = [0,1,2,3,4,5,6,7,8]
   end = False
   legal_move = False
   n_turno = 0



   while (n_turno < 9):
      while (n_turno % 2 == 0):
         movimiento = int(input("¿Cual es el movimiento de X?"))
         if (check_legal(tablero, movimiento) == True):
            tablero[movimiento] = "X"
            n_turno += 1
            print_board(tablero)
      if check_win(tablero,n_turno) == True:
         break
      while (n_turno % 2 == 1 and n_turno !=9):
         movimiento = int(input("¿Cual es el movimiento de Ø?"))
         if (check_legal(tablero,movimiento) == True):
            tablero[movimiento] = "Ø"
            print_board(tablero)
            n_turno += 1
      if check_win(tablero, n_turno) == True:
         break
   if n_turno == 9:
      print("Empate")






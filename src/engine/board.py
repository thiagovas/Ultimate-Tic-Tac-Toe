#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# In here, you can find the board class.


class Board:
  '''
    This class represents a tic-tac-toe board.
    
    In here, all indices are 0-based.
  '''
  
  
  def __init__(self):
    '''
      Board's constructor.
    '''
    self.tab = [['', '', ''] for x in range(3)]
  

  def valid_position(self, line, column):
    '''
      This function receives a position of the board in terms
      of line and column values.
      It returns whether the position is valid or not.
      Both indices must lie into the [0, 2] interval.
    '''
    if line < 0 or column < 0:
      return False
    if line > 3 or column > 3:
      return False
    return True


  def fill(self, line, column, value):
    '''
      This function fills the position <line, column> with the
      value received.
      
      [value] must be a string.
      
      This function does not check whether the position <line, column>
      is already filled.
      
      It returns a string; the string is empty if everything worked nicely,
      or it returns the error.
    '''
    if not isinstance(value, str):
      return "SUA PUTA! NÂO SABE USAR A MERDA DESSA CLASSE NÂO???"
    
    if not self.valid_position(line, column):
      return "SEU MERDA! MANDA A CARALHA DA POSIÇÂO DA MANEIRA CERTA!!!"
    
    self.tab[line][column] = value
    return ""
  
  
  def get_value(self, line, column):
    '''
      This function returns a string with the value found at the position
      <line, column> of the board.
    '''
    
    if not self.valid_position(line, column):
      return "SEU MERDA! MANDA A CARALHA DA POSIÇÂO DA MANEIRA CERTA!!!"
    
    return self.tab[line][column]
    

  def check_winner_lines(self):
    '''
      This function returns -1 if no one has won at any line.
      0 if player one has won at any line.
      1 if player two has won at any line of the board.
    '''
    pass


  def check_winner_column(self):
    '''
      This function returns -1 if no one has won at any column.
      0 if player one has won at any column.
      1 if player two has won at any line of the board.
    '''
    pass


  def check_winner_diagonals(self):
    '''
      This function returns -1 if no one has won at any diagonal.
      0 if player one has won at any diagonal.
      1 if player two has won at any diagonal of the board.
    '''
    pass

  
  def check_old_lady(self):
    '''
      This function checks if the game has come to a draw.
      The old_lady here is just a joke, in case you're not
      a portuguese speaker.
    '''
    for i in range(3):
      if not self.check_line_draw(i):
        return False
      if not self.check_column_draw(i):
        return False
    return check_diagonals_draw()
  
  
  def check_line_draw(self, line):
    '''
      This function checks if there is way for any player to win
      at the line [line].
    '''

    # Disclaimer: I implemented this function this way to not 
    #             define a pattern on the symbols.
    #             If the players want to play the game writing
    #             Y and Z, instead of X and O, this function
    #             won't need any modifications.
    dic = {}
    for i in range(3):
      if len(self.tab[line][i]) != 0:
        dic[self.tab[line][i]] = 1
    return (len(dic) == 2)


  def check_column_draw(self, column):
    '''
      This function checks if there is way for any player to win
      at a given column [column].
    '''
    
    # Disclaimer: I implemented this function this way to not 
    #             define a pattern on the symbols.
    #             If the players want to play the game writing
    #             Y and Z, instead of X and O, this function
    #             won't need any modifications.
    dic = {}
    for i in range(3):
      if len(self.tab[i][colummn]) != 0:
        dic[self.tab[i][column]] = 1
    return (len(dic) == 2)
  
  
  def check_diagonals_draw(self):
    '''
      This function checks if there's a way for any player to win
      at any diagonal.
    '''

    # Disclaimer: I implemented this function this way to not 
    #             define a pattern on the symbols.
    #             If the players want to play the game writing
    #             Y and Z, instead of X and O, this function
    #             won't need any modifications.
    main_diag = {}
    for i in range(3):
      if len(self.tab[i][i]) != 0:
        main_diag[self.tab[i][i]] = 1
    
    sec_diag = {}
    for i in range(3):
      if len(self.tab[i][2-i]) != 0:
        sec_diag[self.tab[i][2-i]] = 1
    
    return (len(main_diag) == 2 and len(sec_diag) == 2)

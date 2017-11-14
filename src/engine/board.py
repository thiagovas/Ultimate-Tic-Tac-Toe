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
    


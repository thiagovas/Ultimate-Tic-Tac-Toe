#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# In here, you can find all functions related to the game AI.
# The main function here is 'move'.

from base import BaseAI
from random import shuffle

class RandomAI(BaseAI):
  '''
    This class is the base class for all AI's one may create to
    this game.
  '''
  
  def __init__(self):
    '''
      Constructor of RandomAI's class.
    '''
    pass
  
  
  def move(self, big_board, small_boards, player_id, sline, scolumn):
    '''
      This is the main function of the AI class.
      The function changes the board with the move, and returns
      the place where the move was done.
    '''
    
    op = []
   
    # Filling op with the positions that are empty...
    for i in range(3):
      for j in range(3):
        if big_board.get_value(i, j) != '':
          continue
        if small_boards[i][j].board_fulfilled():
          continue
        for k in range(3):
          for l in range(3):
            if small_boards[i][j].get_value(k, l) == '':
              op.append([i, j, k, l])
    
    
    # If there is any space left to fill...
    if sline != -1 and scolumn != -1 and not small_boards[sline][scolumn].board_fulfilled():
        op = []
        for k in range(3):
          for l in range(3):
            if small_boards[sline][scolumn].get_value(k, l) == '':
              op.append([sline, scolumn, k, l])
    
    shuffle(op)
    if len(op) == 0:
      print sline, scolumn
      big_board.print_board()
      for i in range(3):
        for j in range(3):
          print ''
          small_boards[i][j].print_board()
    
    op = op[0]
    if player_id == 0:
      small_boards[op[0]][op[1]].fill(op[2], op[3], 'X')
    else:
      small_boards[op[0]][op[1]].fill(op[2], op[3], 'O')
    
    new_state = small_boards[op[0]][op[1]].check_state()
    if new_state == 0:
      big_board.fill(op[0], op[1], 'X')
    elif new_state == 1:
      big_board.fill(op[0], op[1], 'O')
    
    return op

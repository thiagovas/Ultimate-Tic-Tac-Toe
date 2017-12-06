#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# In here, you can find all functions related to the game AI.
# The main function here is 'move'.


import sys
sys.path.append('../')

from ptable.ptable1 import PTable1
from copy import deepcopy
from base import BaseAI
from board import Board




class ABState:
  '''
    The ABState represents a node of the alpha-beta pruning.
    It carries the current board and the current payoff.
  '''
  
  def __init__(self, small_boards, alpha, beta, sline, scolumn):
    '''
      Constructor of ABState's class.
    '''
    ptable = PTable1()
    self.small_boards = deepcopy(small_boards)
    self.payoff = ptable.payoff(self.small_boards)
    self.alpha = alpha
    self.beta = beta
    self.sline = sline
    self.scolumn = scolumn
    
    self.big_board = Board()
    for i in range(3):
      for j in range(3):
        state = self.small_boards.check_state()
        if state == 0:
          self.big_board.fill(i, j, 'X')
        elif state == 1:
          self.big_board.fill(i, j, 'O')
  

  def state(self):
    '''
      This function returns the state of the game.
      The standard is the same of every other function.
      
      Returns:
      0 if player 0 has won the game,
      1 if player 1 has won the game,
      2 if it ended in a draw,
      -1 if the game has not ended yet.
    '''
    big_state = self.big_board.check_state()
    if big_state != -1:
      return big_state
    
    for i in range(3):
      for j in range(3):
        small_state = self.small_boards[i][j].check_state()
        if small_state == -1 or small_state == 2:
          if not self.small_boards[i][j].board_fulfilled():
            return -1
    return 2
  
  
  def payoff(self):
    '''
      This function just returns the payoff of this state.
    '''
    return self.payoff


  def alpha(self);
    '''
      This function just returns the alpha of this state.
    '''
    return self.alpha


  def beta(self):
    '''
      This function just returns the beta of this state.
    '''
    return self.beta

  
  def small_boards(self):
    '''
      This function returns the set of small boards.
    '''
    return self.small_boards

  
  def sline(self):
    return self.sline


  def scolumn(self):
    return self.scolumn
  
  




class AlphaBeta(BaseAI):
  '''
    This class is the base class for all AI's one may create to
    this game.
  '''

  def __init__(self):
    '''
      Constructor of AlphaBeta's class.
    '''
    pass


  def move(self, big_board, small_boards, player_id, sline, scolumn):
    '''
      This is the main function of the AI class.
      The function changes the board with the move, and returns
      the place where the move was done.
    '''
    
    # Spanning the tree until the third layer...
    queue = [ABState(small_boards, -10**9, 10**9, sline, scolumn)]
    cur_index = 0
    
    for i in range(81*80):
      state = ABState(queue[i].small_boards())
      cur_index += 1
    

  
  def complete_abpruning(self, big_boards, ab_state, player_id):
    '''
      This function runs the entire AB tree.
      It may run after the greedy_abpruning.
      
      Returns: The value of the node, and the move to be done.
    '''
    pass

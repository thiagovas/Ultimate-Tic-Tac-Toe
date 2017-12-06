#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# In here, you can find all functions related to the game AI.
# The main function here is 'move'.


from ptable.ptable1 import PTable1
from copy import deepcopy
from base import BaseAI
from ..board import Board




class ABState:
  '''
    The ABState represents a node of the alpha-beta pruning.
    It carries the current board and the current payoff.
  '''

  def __init__(self, psmall_boards, palpha, pbeta, psline, pscolumn, pplayer_id):
    '''
      Constructor of ABState's class.
    '''
    ptable = PTable1()
    self.s_boards = deepcopy(psmall_boards)
    self.pvalue = ptable.payoff(self.s_boards, pplayer_id)
    self.alphavalue = palpha
    self.betavalue = pbeta
    self.slinevalue = psline
    self.scolumnvalue = pscolumn

    self.big_board = Board()
    for i in range(3):
      for j in range(3):
        state = self.s_boards[i][j].check_state()
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
        small_state = self.s_boards[i][j].check_state()
        if small_state == -1 or small_state == 2:
          if not self.s_boards[i][j].board_fulfilled():
            return -1
    return 2


  def payoff(self):
    '''
      This function just returns the payoff of this state.
    '''
    return self.pvalue
  

  def set_payoff(self, value):
    self.pvalue = value


  def alpha(self):
    '''
      This function just returns the alpha of this state.
    '''
    return self.alphavalue


  def set_alpha(self, value):
    self.alphavalue = value


  def beta(self):
    '''
      This function just returns the beta of this state.
    '''
    return self.betavalue


  def set_beta(self, value):
    self.betavalue = value


  def small_boards(self):
    '''
      This function returns the set of small boards.
    '''
    return self.s_boards


  def sline(self):
    return self.slinevalue


  def scolumn(self):
    return self.scolumnvalue






class AlphaBetaAI(BaseAI):
  '''
    This class is the base class for all AI's one may create to
    this game.
  '''

  def __init__(self):
    '''
      Constructor of AlphaBeta's class.
    '''
    self.INF = 10**9



  def move(self, big_board, small_boards, player_id, sline, scolumn):
    '''
      This is the main function of the AI class.
      The function changes the board with the move, and returns
      the place where the move was done.
    '''

    filled_positions = 0
    for i in range(3):
      for j in range(3):
        for k in range(3):
          for l in range(3):
            if small_boards[i][j].get_value(k, l) != '':
              filled_positions += 1

    depth = 2
    if filled_positions >= 61:
      depth = 4
    
    state = ABState(small_boards, -self.INF, self.INF, sline, scolumn,
                    player_id)
    value, ret = self.complete_abpruning(state, True, player_id, depth)


    self.update_boards(big_board, small_boards, ret, player_id)
    return ret



  def update_boards(self, big_board, small_boards, op, player_id):
    '''
      ...
    '''
    if player_id == 0:
      small_boards[op[0]][op[1]].fill(op[2], op[3], 'X')
    else:
      small_boards[op[0]][op[1]].fill(op[2], op[3], 'O')
    
    new_state = small_boards[op[0]][op[1]].check_state()
    if new_state == 0:
      big_board.fill(op[0], op[1], 'X')
    elif new_state == 1:
      big_board.fill(op[0], op[1], 'O')





  def complete_abpruning(self, ab_state, maximizer, player_id, max_depth=2):
    '''
      This function runs the entire AB tree.

      Returns: The value of the node, and the move to be done.
    '''

    if max_depth == 0 or ab_state.state() != -1:
      return ab_state.payoff(), [-1, -1, -1, -1]

    children = []
    ret_move = [-1, -1, -1, -1]
    sline = ab_state.sline()
    scolumn = ab_state.scolumn()

    
    value = self.INF
    if maximizer:
      value = -self.INF


    if (sline != -1 and scolumn != -1 and
        (not ab_state.small_boards()[sline][scolumn].board_fulfilled())):
      for i in range(3):
        for j in range(3):
          if ab_state.small_boards()[sline][scolumn].get_value(i, j) == '':
            # A new child of this state
            children.append((sline, scolumn, i, j))
    else:
      for i in range(3):
        for j in range(3):
          for k in range(3):
            for l in range(3):
              if ab_state.small_boards()[i][j].get_value(k, l) == '':
                # A new child of this state
                children.append((i, j, k, l))

    for v in children:      
      if player_id == 0:
        ab_state.small_boards()[v[0]][v[1]].fill(v[2], v[3], 'X')
      else:
        ab_state.small_boards()[v[0]][v[1]].fill(v[2], v[3], 'O')
      
      new_state = ABState(ab_state.small_boards(), ab_state.alpha(),
                          ab_state.beta(), v[2], v[3], player_id)
      ab_state.small_boards()[v[0]][v[1]].fill(v[2], v[3], '')

      
      if maximizer:
        # - Update value
        ret_value, cur_move = self.complete_abpruning(new_state, False, 1-player_id, max_depth-1)
        # - Update alpha
        ab_state.set_alpha(max(ab_state.alpha(), value))
        if ret_value > value:
          value = ret_value
          ret_move = v
      else:
        # - Update value
        ret_value, cur_move = self.complete_abpruning(new_state, True, 1-player_id, max_depth-1)

        # - Update beta
        ab_state.set_beta(min(ab_state.beta(), value))
        if ret_value < value:
          value = ret_value
          ret_move = v
      
      if ab_state.beta() <= ab_state.alpha():
        break
    return value, ret_move


#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#


def PTable2():
  '''
    This class 
  '''

  def __init__(self):
    pass
  
  
  def payoff(self, small_boards, player_id):
    '''
      This method calculates the payoff of a given board.
      
      
       20 |  5  | 20
      ---------------
       5  |  10 | 5
      ---------------
       20 |  5  | 20
    '''
    p_values = [[20, 5, 20],
                [5, 10, 5],
                [20, 5, 20]]
    psum = 0
    for i in range(3):
      for j in range(3):
        state = small_boards[i][j].check_state()
        if state  == 0 or state == 1:
          if state == player_id:
            psum += p_values[i][j]
          else;
            psum -= p_values[i][j]
    return psum

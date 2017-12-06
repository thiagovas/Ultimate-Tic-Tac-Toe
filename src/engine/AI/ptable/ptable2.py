#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# In here, you can find one representation of the payoff table.
# There is just one class in this file: PTable2


class PTable2:
  '''
    This class just serves to calculate the payoff of a given board.
  '''

  def __init__(self):
    pass
  


  def mount_big_board(self, small_boards):
    self.big_board = Board()
    for i in range(3):
      for j in range(3):
        state = small_boards[i][j].check_state()
        if state == 0:
          self.big_board.fill(i, j, 'X')
        elif state == 1:
          self.big_board.fill(i, j, 'O')



  def state(self, small_boards):
    '''
      This function returns the state of the game.
      The standard is the same of every other function.

      Returns:
      0 if player 0 has won the game,
      1 if player 1 has won the game,
      2 if it ended in a draw,
      -1 if the game has not ended yet.
    '''
    self.mount_big_board(small_boards)
    
    big_state = self.big_board.check_state()
    if big_state != -1:
      return big_state

    for i in range(3):
      for j in range(3):
        small_state = small_boards[i][j].check_state()
        if small_state == -1 or small_state == 2:
          if not small_boards[i][j].board_fulfilled():
            return -1
    return 2


  
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
    big_state = self.state(small_boards)

    if big_state == -1:
      psum = 0
      for i in range(3):
        for j in range(3):
          state = small_boards[i][j].check_state()
          if state  == 0 or state == 1:
            if state == player_id:
              psum += p_values[i][j]
            else:
              psum -= p_values[i][j]
      return psum
    elif big_state == 2:
      return 0
    else:
      if big_state == player_id:
          return 10**9
      else:
          return -10**9

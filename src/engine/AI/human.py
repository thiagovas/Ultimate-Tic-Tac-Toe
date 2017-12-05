#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# In here, you can find the human class.
# It's responsible for the interaction between the input and the
# game.


from base import BaseAI


class Human(BaseAI):
  '''
    Class that represents a human player.
    The move function just reads the player's movement and execute it.
  '''
  
  # TODO: Consider changing this class from this folder
  #       Or change the folder's name, from AI to anything else.
  #       In here just temporarily.
  def __init__(self):
    pass
  
  
  def move(self, big_board, small_boards, player_id, sline, scolumn):
    '''
      This is the main function of the AI class.
      The function changes the board with the move, and returns
      the place where the move was done.

      For this class (Human), it just executes the command received from the stdin.
    '''
    raise NotImplementedError('Should have implemented this function.')




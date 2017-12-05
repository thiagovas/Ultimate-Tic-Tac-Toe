#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# In here, you can find all functions related to the game AI.
# The main function here is 'move'.


class BaseAI:
  '''
    This class is the base class for all AI's one may create to
    this game.
  '''
  
  def __init__(self):
    '''
      Constructor of BaseAI's class.
    '''
    pass
  
  
  def move(self, big_board, small_boards, player_id, sline, scolumn):
    '''
      This is the main function of the AI class.
      The function changes the board with the move, and returns
      the place where the move was done.
    '''
    raise NotImplementedError('Should have implemented this function.')


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# This is the main file of the engine of the game.
# In here, the commands are received and the response are sent back
# to whoever sent the command.


from board import Board
from AI.base import BaseAI
from AI.randomai import RandomAI


class Game:
  '''
    This is the main function of the game.
    Here is where the magic happens.
    
    Definitions:
      - Player 0 = Player X
      - Player 1 = Player O
      - Upper-case X and O !!
  '''
  

  def __init__(self, player_id, starting_player, small_boards, big_board):
    '''
      Constructor of Game class.
      [player_id] is the id number of the bot.
      [starting_player] is the id of the player that will start the game.
      
      [player_id] must be 0 or 1.
      [starting_player] must be 0 or 1.
    '''
    self.small_boards = small_boards
    self.big_board = big_board
    self.bot_id = player_id
    self.AI = RandomAI()
  
  
  
  def move(self, last_move):
    if self.check_state() >= 0:
      return [-1, -1, -1, -1]
      
    # Making sure the move made by the other player is updated in this instance.
    if last_move[0] != -1:
      if self.bot_id == 0:
        self.small_boards[last_move[0]][last_move[1]].fill(last_move[2],
                                                               last_move[3], 'O')
      else:
        self.small_boards[last_move[0]][last_move[1]].fill(last_move[2],
                                                           last_move[3], 'X')
      
      new_state = self.small_boards[last_move[0]][last_move[1]].check_state()
      if new_state == 0:
        self.big_board.fill(last_move[0], last_move[1], 'X')
      elif new_state == 1:
        self.big_board.fill(last_move[0], last_move[1], 'O')
    
    return self.AI.move(self.big_board, self.small_boards,
                        self.bot_id, last_move[2],
                        last_move[3])
  
 
  
  def check_state(self):
    '''
      This function returns an integer value.
      0 if player 0 has won the game,
      1 if player 1 has won the game,
      2 if it ended in a draw,
      -1 if the game has not ended yet.
    '''
    state = self.big_board.check_state()
    if state != -1:
      return state
    
    for i in range(3):
      for j in range(3):
        small_state = self.small_boards[i][j].check_state()
        if small_state == -1 or small_state == 2:
          if not self.small_boards[i][j].board_fulfilled():
            return -1
    return 2

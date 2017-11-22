#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# This is the main file of the engine of the game.
# In here, the commands are received and the response are sent back
# to whoever sent the command.


from board import Board
from AI import AI


class Game:
  '''
    This is the main function of the game.
    Here is where the magic happens.
    
    Definitions:
      - Player 1 = Player X
      - Player 2 = Player O
  '''
  

  def __init__(self, player_id, starting_player):
    '''
      Constructor of Game class.
      [player_id] is the id number of the bot.
      [starting_player] is the id of the player that will start the game.
      
      [player_id] must be 0 or 1.
      [starting_player] must be 0 or 1.
    '''
    self.small_boards = []
    for i in range(3):
      self.small_boards.append([Board(), Board(), Board()])
    self.big_board = Board()
    
    self.bot_id = player_id
    self.current_player = starting_player
    self.AI = AI()
  
  
  def move(self, ):
    if self.game_has_ended():
      return [-1, -1]
    move_done = mode(self.big_board
    self.current_player = 1 - self.current_player
    return move_done
    
  
  def game_has_ended(self):
    '''
      This function returns an integer value.
      0 if player 0 has won the game,
      1 if player 1 has won the game,
      2 if it ended in a draw,
      -1 if the game has not ended yet.
    '''
    if self.big_board.check_old_lady():
      return 2
    
    
    wl = self.big_board.check_winner_lines()
    wc = self.big_board.check_winner_column()
    wd = self.big_board.check_winner_diagonals()
    
    if wl != -1:
      return wl
    
    if wc != -1:
      return wc

    if wd != -1:
      return wd
    
    return -1
  




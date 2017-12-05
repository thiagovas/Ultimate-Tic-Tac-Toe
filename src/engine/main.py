#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Here be main!

# TODO: Consider moving this piece of code to UI/

from game import Game
from board import Board

def main():
  small_boards = []
  for i in range(3):
    small_boards.append([Board(), Board(), Board()])
  big_board = Board()
  
  player1 = Game(0, 0, small_boards, big_board)
  player2 = Game(1, 0, small_boards, big_board)
  
  last_move = [-1, -1, -1, -1]
  last_log = -14
  
  while True:
    last_move = player1.move(last_move)
    last_log = player1.check_state()
    if last_log >= 0:
      break
    
    last_move = player2.move(last_move)
    last_log = player2.check_state()
    if last_log >= 0:
      break
  
  if last_log == 0:
    print "Player 1"
  elif last_log == 1:
    print "Player 2"
  else:
    print "Draw"


if __name__ == '__main__':
  main()

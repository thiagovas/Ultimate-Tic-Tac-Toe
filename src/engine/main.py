#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Here be main!

from game import Game

def main():
  player1 = Game(0, 0)
  player2 = Game(1, 0)
  
  last_move = [-1, -1, -1, -1]
  last_log = -14
  
  while True:
    last_move = player1.move(last_move)
    last_log = player1.game_has_ended()
    if last_log >= 0:
      break
    
    last_move = player2.move(last_move)
    last_log = player2.game_has_ended()
    if last_log >= 0:
      break
  
  if last_log == -1:
    print "Draw"
  elif last_log = 0:
    print "Player 1"
  else:
    print "Player 2"


if __name__ == '__main__':
  main()

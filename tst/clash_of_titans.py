#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Here be the CLASH OF TITANS!!!
# Two AIs will face each other A HUNDRED TIMES!
# And whoever beats the other more will be THE FUCKING WIIINNEEEERRR!!!!
# 
# Play this before executing the test: https://www.youtube.com/watch?v=iBdxZFO3gOA


import sys
sys.path.append('../src')

from engine.game import Game
from engine.board import Board
from engine.AI.alphabeta import AlphaBetaAI
from engine.AI.randomai import RandomAI
from engine.AI.ptable.ptable1 import PTable1
from engine.AI.ptable.ptable2 import PTable2



def clean_the_blood_from_the_floor():
  '''
    Function to prepare the octogon to another round.
  '''
  small_boards = []
  for i in range(3):
    small_boards.append([Board(), Board(), Board()])
  big_board = Board()
  
  
  # Setting a random start game...
  player1 = Game(0, 0, small_boards, big_board, RandomAI())
  player2 = Game(1, 0, small_boards, big_board, RandomAI())
  
  last_move = [-1, -1, -1, -1]
  last_log = -14
  
  for i in range(20):
    last_move = player1.move(last_move)
    last_log = player1.check_state()
    if last_log >= 0:
      break
    
    last_move = player2.move(last_move)
    last_log = player2.check_state()
    if last_log >= 0:
      break
  return big_board, small_boards



def fight(big_board, small_boards, rev=False):
  p1AI = AlphaBetaAI()
  p1AI.set_payoff_table(PTable1())
  
  p2AI = RandomAI()

  if rev:
    p1AI, p2AI = p2AI, p1AI

  player1 = Game(0, 0, small_boards, big_board, p1AI)
  player2 = Game(1, 0, small_boards, big_board, p2AI)
  
  last_move = [-1, -1, -1, -1]
  last_log = -14
  n_moves = 0
  
  while True:
    last_move = player1.move(last_move)
    last_log = player1.check_state()
    n_moves += 1
    if last_log >= 0:
      break
    
    last_move = player2.move(last_move)
    last_log = player2.check_state()
    n_moves += 1
    if last_log >= 0:
      break
  
  if last_log == 0:
    return 1, n_moves
  elif last_log == 1:
    return 2, n_moves
  else:
    return 0, n_moves



def main():
  p1 = 0
  p2 = 0
  draws = 0
  mean_moves = 0
  for i in range(500):
    print i
    big_board, small_boards = clean_the_blood_from_the_floor()
    result, n_moves = fight(big_board, small_boards, False)
    mean_moves += n_moves
    if result == 0:
      draws += 1
    elif result == 1:
      p1 += 1
    else:
      p2 += 1
    
    result, n_moves = fight(big_board, small_boards, True)
    mean_moves += n_moves
    if result == 0:
      draws += 1
    elif result == 1:
      p2 += 1
    else:
      p1 += 1

  print p1, p2, draws, '  #Avg Moves:', (float(mean_moves)/(10**3))

if __name__ == '__main__':
  main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('../src')


from engine.board import Board

def main():
  board = Board()
  board.fill(1, 2, 'X')
  board.fill(2, 2, 'X')
  board.fill(2, 1, 'O')
  board.print_board()


if __name__ == '__main__':
  main()

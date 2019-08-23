# -*- coding: utf-8 -*-

"""
A script that can be used to debug the legal move generator of an engine.

Requirements:
    Python 3
    
Tested on:
    Windows 7
    Python 3.7.3
"""

import time
import shogi

def start_perft_divide(board, depth):
    total = 0  
    t0 = time.perf_counter()
    
    for move in board.pseudo_legal_moves:
        board.push(move)
        
        if not board.was_suicide() and not board.was_check_by_dropping_pawn(move):
            count = perft(board, depth - 1)
            total += count
            
        board.pop()
        
        print('{:5s}: {}'.format(str(move), count))
    
    print('\nPerf divide result')
    print('sfen   : {}'.format(board.sfen()))
    print('Depth  : {}'.format(depth))
    print('Total  : {}'.format(total))
    print('elapsed: {:0.2f}s'.format(time.perf_counter() - t0))

def perft(board, depth):
    total = 0
    
    if depth == 0:
        return 1

    for move in board.pseudo_legal_moves:
        board.push(move)

        if not board.was_suicide() and not board.was_check_by_dropping_pawn(move):
            count = perft(board, depth - 1)
            total += count

        board.pop()
        
    return total

def main():
    # Sample sfens
    # 7lk/9/8S/9/9/9/9/7L1/8K b P 1
    # 7k1/9/9/9/l2s5/6snb/9/9/8K b 2G 1
    # ln1g5/1r2k2g1/p2ppp3/3s1+bpP1/9/P1pS1P1p1/1PGPP1P2/3K2S1R/L4G1N1 b SN2L4Pbn 73
    
    # Data input
    depth = max(1, int(input('input depth? ')))
    sfen = input('input sfen [startpos | <your sfen>]? ')
    
    if sfen == 'startpos':
        sfen = shogi.STARTING_SFEN
    
    try:
        board = shogi.Board(sfen)    
    except ValueError:
        print('Illegal sfen')
        return
    except Exception as e:
        print('Unexpected error: {}'.format(e))
        return

    start_perft_divide(board, depth)

if __name__ == '__main__':
    main()

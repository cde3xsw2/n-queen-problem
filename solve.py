
from __future__ import print_function
import sys
from dao import Solution, save_solutions,delete_solutions, list_solutions

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print('x' if board[i] == j else '0',end='')
        print()
    print()

class Board:

    def __init__(self, n):
        self.n = n


    def is_valid_pos(self, pos_0_x, pos_0_y, pos_1_x, pos_1_y):
        if (pos_0_x + pos_1_y == pos_1_x + pos_0_y):
            return False
        if  (pos_0_x - pos_1_y == pos_1_x - pos_0_y):
            return False
        return True

    def is_valid_board(self, board):
        length = len(board)
        for i in range(length):
            for j in range(i+1,length):
                if not self.is_valid_pos( i,board[i], j, board[j] ):
                    return False
        return True

    def next_pos(self, current_val,nv,current_conf):
        if current_val == None:
            for i in nv:
                if i not in current_conf:
                    return i
        else:
            for i in nv:
                if i > current_val and i not in current_conf:
                    return i
                
    def find_solutions(self):
        count = 0
        count1 = 0
        current_line = 0
        current_conf = []
        nv = range(self.n)[:]
        while True:
            try:
                count1 = count1 + 1
                current_val_line = current_conf[current_line]
                next_p = self.next_pos(current_val_line,nv,current_conf)
                if next_p != None:
                    current_conf[-1] = next_p
                    current_line = current_line + 1
                else:
                    if current_line == 0:
                        break
                    current_conf.pop()
                    current_line = current_line - 1 
            except:
                next_p = self.next_pos(None,nv,current_conf)
                if next_p != None:
                    current_conf.append(next_p)
                    current_line = current_line + 1
                else:
                    current_conf.pop()
                    current_line = current_line - 1
            if self.is_valid_board(current_conf):
                if  current_line == self.n:
                    yield current_conf
                    count = count + 1
                    current_line = current_line - 1
                    continue
            else:
                if current_line > 1:
                    current_line = current_line - 1
                    continue

def print_help():
    print(''' 
        Solves the n-queen problem.
                Options:
                    calculate num-of-queens(i.e. calculate 8)
                    save-in-db num-of-queens (i.e. save-in-db 8)
                    list-results num-of-queens (i.e. list-results 8)
                    find-first num-of-queens (i.e.find-first 8)
            ''')

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        option = sys.argv[1]
        try:
            board_size = int(sys.argv[2])
        except:
            print_help()
            exit()
        if option == 'calculate':
            print(len(list(Board(n=board_size).find_solutions())))
        elif option == 'find-first':
            try:
                print_board(next(Board(n=board_size).find_solutions()))
            except:
                print("Solution not found for %d" % (board_size))
        elif option == 'save-in-db':
            delete_solutions(n=board_size)
            board = Board(n=board_size)
            find_solutions = iter(board.find_solutions())
            solutions = []
            while True:
                try:
                    next_solution = next(find_solutions)
                except:
                    if solutions:
                        save_solutions(n=board_size,solutions=solutions)
                    break
                solutions.append(next_solution[:])
                if len(solutions) >= 100:
                    save_solutions(n=board_size,solutions=solutions)
                    solutions = []
            print("Info saved for board : %d" % (board_size) )
        elif option == 'list-results':
            solutions = list_solutions(n=board_size)
            print("Total of solutions: %d " %(len(solutions)))
            if len(solutions) > 0:
                for solution in solutions:
                    print_board(solution.result)
            else:
                print("Result for solutions %d not found. First execute 'save-in-db ' "% (board_size))
                print_help()

        else:
            print_help()
        
    else:
        print_help()

#import timeit
#print(timeit.timeit(lambda: solve(n=8),number=1))
#print(timeit.timeit(lambda: solve(n=9),number=1))
#print(timeit.timeit(lambda: solve(n=10),number=1))
#print(timeit.timeit(lambda: solve(n=11),number=1))
#print(timeit.timeit(lambda: solve(n=12),number=1))
#print(timeit.timeit(lambda: solve(n=13),number=1))
#print(timeit.timeit(lambda: solve(n=14),number=1))
#print(timeit.timeit(lambda: solve(n=15),number=1))


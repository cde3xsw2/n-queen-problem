from solve import  Board


def test_size_8():
    assert len(list(Board(n=8).find_solutions())) == 92

def test_valid_position():
    board = Board(n=8)
    first_solution = next(board.find_solutions())
    assert board.is_valid_board(first_solution) == True

def test_invalid_position():
    board = Board(n=8)
    assert board.is_valid_board([0,1,2,3,4,5,6,7]) == False

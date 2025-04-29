class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []

    def is_safe(self, row, col):
        for r in range(row):
            if self.board[r] == col or abs(self.board[r] - col) == abs(row - r):
                return False
        return True

    def branch_and_bound(self, row=0, column_choices=None):
        if column_choices is None:
            column_choices = list(range(self.n))
        if row == self.n:
            self.solutions.append(self.board[:])
            return
        for col in column_choices:
            if self.is_safe(row, col):
                self.board[row] = col
                next_choices = column_choices.copy()
                next_choices.remove(col)  # Remove used column for the next row
                self.branch_and_bound(row + 1, next_choices)
                self.board[row] = -1

    def print_solutions(self):
        for sol in self.solutions:
            print(" ".join(str(col + 1) for col in sol))  # 1-based output

def solve_nqueens(n):
    nq = NQueens(n)
    nq.branch_and_bound()
    print(f"\nTotal Solutions: {len(nq.solutions)}")
    nq.print_solutions()

n = int(input("Enter n for N-Queens: "))
solve_nqueens(n)






####
class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []

    def is_safe(self, row, col):
        for r in range(row):
            if self.board[r] == col or abs(self.board[r] - col) == row - r:
                return False
        return True

    def backtrack(self, row=0):
        if row == self.n:
            self.solutions.append(self.board[:])  # Solution found
            return
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col  # Place queen
                self.backtrack(row + 1)  # Move to the next row
                self.board[row] = -1  # Backtrack (remove queen)

    def print_solutions(self):
        for sol in self.solutions:
            print(" ".join(str(col + 1) for col in sol))  # Convert 0-based to 1-based index

def solve_nqueens(n):
    nq = NQueens(n)
    nq.backtrack()
    nq.print_solutions()

n = int(input("Enter n for N-Queens: "))
solve_nqueens(n)
####

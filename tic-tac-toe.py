#!/usr/bin/env python3
"""
Simple text-based 2-player Tic Tac Toe.
Player 1 is 'X', Player 2 is 'O'.
Enter positions 1-9 as shown on the board:
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
"""

def print_board(board):
    """Print the board. board is a list of 9 items."""
    rows = [
        f" {board[0]} | {board[1]} | {board[2]} ",
        f" {board[3]} | {board[4]} | {board[5]} ",
        f" {board[6]} | {board[7]} | {board[8]} ",
    ]
    sep = "\n---+---+---\n"
    print("\n" + sep.join(rows) + "\n")

def check_winner(board):
    """Return 'X' or 'O' if there's a winner, or None otherwise."""
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def board_full(board):
    return all(cell != " " for cell in board)

def get_move(player, board):
    """Prompt the player for a move and return 0-based index."""
    while True:
        try:
            s = input(f"Player {player} — enter position (1-9): ").strip()
            if s.lower() in ("q","quit","exit"):
                print("Game aborted by user.")
                raise SystemExit
            pos = int(s)
            if pos < 1 or pos > 9:
                print("  Invalid position. Choose a number 1-9.")
                continue
            idx = pos - 1
            if board[idx] != " ":
                print("  That position is already taken. Choose another.")
                continue
            return idx
        except ValueError:
            print("  Please enter a number from 1 to 9 (or 'q' to quit).")

def play_round():
    board = [" "] * 9
    current = "X"  # X always starts
    print("Positions are numbered like this:")
    print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9\n")
    while True:
        print_board(board)
        idx = get_move(current, board)
        board[idx] = current
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Player {winner} wins! Congratulations!")
            return winner
        if board_full(board):
            print_board(board)
            print("It's a draw!")
            return "Draw"
        # switch player
        current = "O" if current == "X" else "X"

def main():
    print("Welcome to Tic Tac Toe (2-player).")
    while True:
        result = play_round()
        # Ask for replay
        while True:
            again = input("Play again? (y/n): ").strip().lower()
            if again in ("y","yes"):
                break
            if again in ("n","no"):
                print("Thanks for playing — goodbye!")
                return
            print("Please answer 'y' or 'n'.")

if __name__ == "__main__":
    main()

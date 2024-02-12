def pawn(pawn_column_letter, pawn_row_number, black_letter, black_row_number):
    black_letter_numeric = ord(black_letter)
    pawn_row_number = int(pawn_row_number)
    black_row_number = int(black_row_number)

    if (black_letter_numeric == ord(pawn_column_letter) + 1 or
            black_letter_numeric == ord(pawn_column_letter) - 1) and black_row_number == pawn_row_number + 1:
        return True
    else:
        return False

def king(king_column_letter, king_row_number, black_letter, black_row_number):
    black_letter_numeric = ord(black_letter)
    king_row_number = int(king_row_number)
    black_row_number = int(black_row_number)

    if (black_letter_numeric == ord(king_column_letter) or
        black_letter_numeric == ord(king_column_letter) - 1 or
        black_letter_numeric == ord(king_column_letter) + 1) and (
        black_row_number == king_row_number + 1 or
        black_row_number == king_row_number or
        black_row_number == king_row_number - 1):
        return True
    else:
        return False



def empty_chess_board():
    return [
        ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"],
        ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
        ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"],
        ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"],
        ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"],
        ["a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3"],
        ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
        ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"],
    ]
correct_pieces = "king", "pawn"

def main():
    chess_board = empty_chess_board()
    for row in chess_board:
        print(row)

    valid_columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
    valid_rows = [1, 2, 3, 4, 5, 6, 7, 8]
    correct_pieces = True

    # Initialize counters for each type of black piece
    black_pawn_count = 0
    black_queen_count = 0
    black_king_count = 0
    black_bishop_count = 0
    black_knight_count = 0
    black_rook_count = 0

    while correct_pieces:
        user_input = input("Please enter white piece (king or pawn) and coordinates (Example: king a5): ")

        # Split the input into pieces
        input_pieces = user_input.split()

        # Check if there are enough pieces
        if len(input_pieces) >= 2:
            white_figure, white_coordinates = input_pieces
        else:
            print("Invalid input format. Please enter both white piece and coordinates.")
            continue

        if white_figure in ["pawn", "king"]:
            column_white = white_coordinates[0]
            row_white = int(white_coordinates[1:])

            if column_white in valid_columns and row_white in valid_rows:
                chess_board[8 - row_white][ord(column_white) - ord("a")] = white_figure
                print("Correct input. Piece placed on the chessboard.")
                break
            else:
                print("Invalid coordinates. Please enter correct coordinates.")
        else:
            print("Invalid input. Please enter either 'pawn' or 'king'.")



    counter = 0
    black_pieces_taken = 0
    valid_black_pieces = ["king", "queen", "bishop", "knight", "rook", "pawn"]
    while counter < 16:
        user_input = input("Please enter black piece (king, queen, bishop, knight, rook, pawn) and coordinates (example: queen e5) (type 'done' to finish): ")

        if user_input.lower().strip() == "done":
            break

        input_pieces = user_input.split()
        if len(input_pieces) >= 2:
            black_piece, black_piece_coordinates = input_pieces

            if black_piece in valid_black_pieces:
                print("Correct piece name")
            else:
                print("Invalid piece name")
                continue

            column_black = black_piece_coordinates[0]
            row_black = int(black_piece_coordinates[1:])

            if column_black == column_white and row_black == row_white:
                    print("You can't place black piece here.")
                    continue
            if column_black in valid_columns and 1 <= row_black <= 8:






                if black_piece == "pawn":
                    black_pawn_count += 1
                elif black_piece == "queen":
                    black_queen_count += 1
                elif black_piece == "king":
                    black_king_count += 1
                elif black_piece == "bishop":
                    black_bishop_count += 1
                elif black_piece == "knight":
                    black_knight_count += 1
                elif black_piece == "rook":
                    black_rook_count += 1

                if (
                    black_pawn_count <= 8
                    and black_queen_count <= 1
                    and black_king_count <= 1
                    and black_bishop_count <= 2
                    and black_knight_count <= 2
                    and black_rook_count <= 2
                    ):
                    if white_figure == "king" and king(column_white, row_white, column_black, row_black):
                        chess_board[8 - row_black][ord(column_black) - ord("a")] = black_piece
                        print(f"King can take this {user_input}")
                        black_pieces_taken += 1
                    elif white_figure == "pawn" and pawn(column_white, row_white, column_black, row_black):
                        chess_board[8 - row_black][ord(column_black) - ord("a")] = black_piece
                        print(f"Pawn can take this {user_input}")
                        black_pieces_taken += 1
                else:
                    print("Maximum limit for some type of black pieces exceeded.")



            counter += 1
        else:
            print("Invalid input. Please enter both piece and coordinates.")

    for row in chess_board:
        print(row)

    print(f"The white {white_figure} can take {black_pieces_taken} black pieces.")


main()

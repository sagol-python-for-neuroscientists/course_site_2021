import warnings
from typing import Union
from enum import Enum
import random

import numpy as np


class Signal(Enum):
    """Signals transmitted between the pieces at play and the 'runtime' that
    checks the status of the game."""

    HIT = "hit"
    MISS = "miss"
    DESTROYED = "destroyed"
    END = "end"


class Plane(Enum):
    """The board game contains these levels as possible
    piece locations."""

    DEEPSEA = 0
    SEALEVEL = 1
    AIR = 2


class GamePiece:
    """Base class for all game pieces.

    Parameters
    ----------
    piece_id : int
        Unique ID for each piece of that type
    plane : Plane
        The plane at which the piece is located

    Attributes
    ----------
    outline : np.ndarray
        A 2D array describing the way the current piece looks.
        0s are places where it doesn't exist, and 1s are places
        it does.
    locs : list of lists
        Remaining on-board coordinates for that pieces that weren't hit.
        The length of the list is the length of the shape's outline, and
        each item is a list of length 3 that contains the actual coordinate
        values.

    """

    def __init__(self, piece_id: int, plane: Plane):
        self.piece_id = piece_id
        self.plane = plane
        self.outline = np.array([0])
        self.locs = None

    @property
    def shape(self):
        return self.outline.shape

    @property
    def filled_outline(self):
        return self.outline * self.piece_id

    def __repr__(self):
        return f"{self.__class__.__name__}{self.piece_id}"


class General(GamePiece):
    """The deciding piece of the game, piece_id is given as input for
    compatability """

    def __init__(self, piece_id: int):
        plane = random.choice(list(Plane))
        super().__init__(piece_id, plane)
        self.piece_id = 1
        self.outline = np.array([[1]], dtype=np.int16)

    def hit(self, coord):
        return Signal.END


class Jet(GamePiece):
    """ A flying piece in the "sky" plane """

    def __init__(self, piece_id: int):
        super().__init__(piece_id, Plane.AIR)
        self.outline = np.array(
            [[0, 1, 0], [1, 1, 1], [0, 1, 0], [0, 1, 0]], dtype=np.int16
        )

    def hit(self, coord):
        return Signal.DESTROYED


class Destroyer(GamePiece):
    """ A big battle ship """

    def __init__(self, piece_id: int):
        super().__init__(piece_id, Plane.SEALEVEL)
        self.outline = np.array([[1], [1], [1], [1]], dtype=np.int16)

    def hit(self, coor_to_pop: tuple):
        coor_to_pop = list(coor_to_pop)
        try:
            self.locs.remove(coor_to_pop)
        except ValueError:
            print(
                f"Problem with the coordinate {coor_to_pop} - it wasn't found, or was already targeted."
            )
            return Signal.MISS
        else:
            if len(self.locs) == 0:
                return Signal.DESTROYED
            else:
                return Signal.HIT


class Submarine(GamePiece):
    """ Submerged vessel, a single hit sinks it """

    def __init__(self, piece_id: int):
        super().__init__(piece_id, Plane.DEEPSEA)
        self.outline = np.array([[1, 1, 1]], dtype=np.int16)

    def hit(self, coord):
        return Signal.DESTROYED


class SubmarinesPieces(Enum):
    """ Allowed types of pieces in the Submarines game"""

    GENERAL = General
    JETS = Jet
    DESTROYERS = Destroyer
    SUBMARINES = Submarine


class ThreeDSubmarinesBoard(np.ndarray):
    """A 3D board to hold the pieces.

    Inherits from numpy.ndarray to allow for easy indexing, but one
    could've easily used an array as an attribute of the class
    instead. Instructions on how to subclass a numpy ndarray are found here:
    https://numpy.org/doc/stable/user/basics.subclassing.html?highlight=subclassing#module-numpy.doc.subclassing

    There are 3 "planes" to the board, which are represented by the third dimension.
    Plane 0 is under the sea, plane 1 is at sea-level, and plane 2 is the air.

    The pieces attribute is a list containing all active pieces on the board. Once it's empty
    the game is over.
    """

    def __new__(
        subtype,
        shape: tuple = (10, 10, 3),
        dtype: np.dtype = np.object,
        *,
        pieces: list,
    ):
        if len(shape) != 3:
            return ValueError(
                f"Shape received was {shape}, but it must have exactly 3 items."
            )

        obj = super(ThreeDSubmarinesBoard, subtype).__new__(subtype, shape, dtype)
        obj.pieces = pieces
        obj[:] = 0
        return obj

    def __array_finalize__(self, obj):
        """ A unique method which is run after initialization """
        if obj is None:
            return
        default_pieces = [
            piece.value(piece_id) for piece_id, piece in enumerate(SubmarinesPieces)
        ]
        self.pieces = getattr(obj, "pieces", default_pieces)

    def _create_random_slice_for_piece(self, piece: GamePiece):
        """For a given game piece, generate a random slice
        on the board.

        The slice is a rectangular chunk from the array that could
        potentially host the given piece.

        Parameters
        ----------
        piece : GamePiece
            The current piece to place
        """
        row_idx = np.random.choice(self.shape[0])
        col_idx = np.random.choice(self.shape[1])
        cur_slice = (
            slice(row_idx, row_idx + piece.shape[0]),
            slice(col_idx, col_idx + piece.shape[1]),
            slice(piece.plane.value, piece.plane.value + 1),
        )
        return cur_slice

    def _place_piece(self, slice_for_piece: tuple, piece: GamePiece) -> bool:
        """Try to place pieces in the given slice, i.e.
        see if it fits inside the board and that it's
        empty.

        Parameters
        ----------
        slice_for_piece : 3-tuple of slice
            The slice in each dimension where the piece
            should be placed.
        piece : GamePiece
            Current game piece to place

        Returns
        -------
        bool
            True if successful

        Raises
        ------
        IndexError
            If slice is out of bounds
        AssertionError
            If the pieces is malformed or that
            the designated place isn't empty.
        """
        cur_subboard = self[slice_for_piece].copy()
        assert cur_subboard.shape[:2] == piece.shape
        assert np.all(cur_subboard == 0)  # empty part of the sub-board
        return True

    def _update_board_on_successful_attempt(
        self, slice_for_piece: tuple, piece: GamePiece
    ):
        """Once the placement was successful, both the board and the piece
        should be notified.

        The method inserts the pieces into the board and updates their
        "locs" attributes accordingly.

        Parameters
        ----------
        slice_for_piece : 3-tuple of slices
            Slice in each place to place the piece
        piece : GamePiece
            Currently placed piece
        """
        self[slice_for_piece] += np.atleast_3d(piece.filled_outline)
        piece.locs = np.argwhere(self == piece.piece_id).tolist()
        self[self == piece.piece_id] = piece

    def place_pieces(self):
        """Place pieces on the board.
        ahecks that the piece wasn't placed outside the boundaries of the board,
        and that the cells were empty.
        If indeed so, it places views of the piece object in each cell.
        """
        MAX_NUMBER_OF_TRIALS_FOR_ALL_PIECES = 200
        for piece in self.pieces:
            placed = False
            trial = 0
            while not placed and trial < MAX_NUMBER_OF_TRIALS_FOR_ALL_PIECES:
                slice_for_piece = self._create_random_slice_for_piece(piece)
                try:
                    placed = self._place_piece(slice_for_piece, piece)
                except (IndexError, AssertionError):  # outside of board boundary
                    pass
                finally:
                    trial += 1
            if trial >= MAX_NUMBER_OF_TRIALS_FOR_ALL_PIECES:
                raise UserWarning("Board is too small for all pieces.")

            # If we reached here then the piece fits this location
            self._update_board_on_successful_attempt(slice_for_piece, piece)

    def check_if_hit(self, coord: tuple) -> Signal:
        """
        Receive a 3D coordinate of the location that was targeted.
        Then check the board which piece is there and return the signal.
        :param coord: Tuple of 3 coordinates
        :return: Signal
        """
        cell = self[coord]
        if cell == 0:
            return Signal.MISS
        sig = cell.hit(coord)
        if sig is Signal.DESTROYED:
            try:
                self.pieces.remove(cell)
            except ValueError:  # already killed
                pass
            if len(self.pieces) == 1:
                sig = Signal.END
        return sig


class SubmarinesGame:
    """
    Play a Submarines game for two players. Run it with the start() method.
    Supply a tuple defining the 3D board size, and adictionary of unit names (from SubmarinesPieces) and values,
    corresponding to the number of units you wish to have of that size.
    At each turn you're prompted to enter a length-3 tuple with the coordinate you're targeting.
    You'll be notified if you missed, hit or killed a unit. You can also write "show" to show the board,
    and "quit" to stop the game.
    """

    def __init__(self, board_shape: tuple = (10, 10, 3), pieces: dict = None):
        self.board_shape = board_shape
        self.pieces = pieces
        self.piece_list_1 = []
        self.piece_list_2 = []

        self.__validate_input()
        self.__generate_pieces_list()

        self.board1 = ThreeDSubmarinesBoard(self.board_shape, pieces=self.piece_list_1)
        self.board2 = ThreeDSubmarinesBoard(self.board_shape, pieces=self.piece_list_2)

        self.players = ("Player 1", "Player 2")
        self.boards = (self.board2, self.board1)
        self.move = 0

    def __validate_input(self):
        assert len(self.board_shape) == 3
        assert self.board_shape[2] == 3  # only 3D inputs
        assert self.board_shape[0] >= 4 and self.board_shape[1] >= 4
        if self.pieces is not None:
            for piece, val in self.pieces.items():
                assert piece in SubmarinesPieces
                assert isinstance(val, int)
                assert val >= 0 and val <= 50
            assert SubmarinesPieces.GENERAL in self.pieces
            assert self.pieces[SubmarinesPieces.GENERAL] == 1

    def __generate_pieces_list(self):
        """ Populate the list of pieces """
        if self.pieces is not None:
            piece_id = 1
            for piece, num in self.pieces.items():
                for cur_instance in range(num):
                    self.piece_list_1.append(piece.value(piece_id))
                    self.piece_list_2.append(piece.value(piece_id))
                    piece_id += 1

    def _parse_coord_user_str_into_tuple(self, coord: str) -> tuple:
        """Takes the given string and parses it into a coordinate tuple.

        This function doesn't deal with the verification of the actual
        number of coordinates, it only transforms strings to tuples.

        Parameters
        ----------
        coord : str
            The given coordinate to parse

        Returns
        -------
        coord : 3-tuple
            A tuple of the current coordinate in (x, y, z) format
        """
        coor_list = []
        multi_digit_chars = ''
        for char in coord:
            if char.isdigit():
                multi_digit_chars += char
            elif char == '-':
                warnings.warn('The character "-" is not allowed, parsing might have failed.')
                multi_digit_chars += char
            else:
                if len(multi_digit_chars) > 0:
                    coor_list.append(int(multi_digit_chars))
                    multi_digit_chars = ''
        try:
            last_digit = int(multi_digit_chars)
        except ValueError:
            pass
        else:
            coor_list.append(last_digit)
        coord = tuple(coor_list)
        return coord

    def _assert_coor_in_board(self, coord: str) -> Union[bool, tuple]:
        """Parses the user's input into a workable coordinate."""
        coord = self._parse_coord_user_str_into_tuple(coord)
        try:
            assert len(coord) == 3
            assert all(
                0 <= user_coord < shape
                for user_coord, shape in zip(coord, self.board1.shape)
            )
        except AssertionError:
            print(
                f"Coordinate {coord} is located outside the board. Board shape is {self.board1.shape}."
            )
            return False
        else:
            return coord

    def _process_show(self, board: np.ndarray):
        """Prints the current status of the given board."""
        print("Deep:\n", board[..., 0])
        print("Sea-level:\n", board[..., 1])
        print("Air:\n", board[..., 2])

    def _get_and_parse_input(self) -> Union[bool, tuple]:
        """ Helper function to parse the input from the user.

        Returns
        -------
        coor : bool or 3-tuple
            False if no coordinate was given, or a 3-tuple of the
            values per axis otherwise.
        """
        coor = input(
            f"{self.players[self.move % 2]}, what is the coordinate you're targeting (x, y, z)? "
        )
        if coor == "quit":
            raise SystemExit("Quitting")
        if coor == "show":
            self._process_show(self.boards[(self.move - 1) % 2])
            return False
        coor = self._assert_coor_in_board(coor)
        return coor

    def start(self):
        """ Start a Submarines game """

        print("Welcome to another game of Submarines!\n")
        print(f"The shape of today's board is {self.board1.shape}.")
        print(
            "You can type 'show' to show your board, and 'quit' to exit the game prematurely."
        )
        for board in self.boards:
            board.place_pieces()
        print("The pieces were set (randomly), let the game begin!")

        ret_signal = 0

        while ret_signal != Signal.END:
            coor = False
            while not coor:
                coor = self._get_and_parse_input()

            ret_signal = self.boards[self.move % 2].check_if_hit(coor)
            print(ret_signal)
            self.move += 1

        print(f"The game is over! The winner is {self.players[(self.move - 1) % 2]}.")


if __name__ == "__main__":
    pieces = {
        SubmarinesPieces.GENERAL: 1,
        SubmarinesPieces.JETS: 1,
        SubmarinesPieces.DESTROYERS: 1,
        SubmarinesPieces.SUBMARINES: 1,
    }
    subgame = SubmarinesGame(board_shape=(4, 4, 3), pieces=pieces)

    subgame.start()

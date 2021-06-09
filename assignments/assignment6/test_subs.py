import pytest

from submarines import *

all_planes = list(Plane)


class TestEnums:
    """A group of tests that assert that nothing changes with the basic
    enumerations of the game."""

    def test_enum_signal(self):
        """Actual values may change, but their number shouldn't"""
        assert len(list(Signal)) == 4

    def test_enum_plane(self):
        """Actual values may change, but their number shouldn't"""
        assert len(list(Plane)) == 3

    def test_enum_submarinepieces(self):
        """Actual values may change, but their number shouldn't"""
        assert len(list(SubmarinesPieces)) == 4


class TestGamePieces:
    """A group of tests for the game pieces"""

    def test_pieces_baseclass_includes_outline_and_locs(self):
        pid = 10
        gp = GamePiece(pid, Plane.DEEPSEA)
        getattr(gp, "outline")
        getattr(gp, "locs")

    def test_pieces_baseclass_filled_outline(self):
        pid = 2
        gp = GamePiece(pid, Plane.AIR)
        np.testing.assert_array_equal(gp.filled_outline, np.array([0]))

    def test_pieces_general_pid_is_always_1(self):
        pid = 2
        g = General(pid)

    @pytest.mark.parametrize("plane", all_planes)
    def test_pieces_general_hit_is_end(self, plane):
        g = General(0)
        assert Signal.END is g.hit(0)

    @pytest.mark.parametrize("plane", all_planes)
    def test_pieces_general_constant_outline(self, plane):
        g = General(7)
        np.testing.assert_array_equal(np.array([[1]], dtype=np.int16), g.outline)

    def test_pieces_jet_hit_is_kill(self):
        j = Jet(1)
        assert Signal.DESTROYED is j.hit(1)

    def test_pieces_jet_pid_in_outline(self):
        pid = 31
        j = Jet(pid)
        np.testing.assert_array_equal(
            np.unique(j.filled_outline), np.array([0, pid], dtype=np.int16)
        )

    def test_pieces_destroyer_pid_in_outline(self):
        pid = 33
        d = Destroyer(pid)
        np.testing.assert_array_equal(
            np.unique(d.filled_outline), np.array([pid], dtype=np.int16)
        )

    def test_pieces_destroyer_hit_results_in_hit(self):
        d = Destroyer(3)
        d.locs = [[0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1]]
        sig = d.hit([0, 1, 1])
        assert sig is Signal.HIT

    def test_pieces_destroyer_miss_results_in_miss(self):
        d = Destroyer(3)
        d.locs = [[0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1]]
        sig = d.hit([0, 1, 2])
        assert sig is Signal.MISS

    def test_pieces_destroyer_last_hist_results_in_kill(self):
        d = Destroyer(3)
        d.locs = [[0, 1, 1]]
        sig = d.hit([0, 1, 1])
        assert sig is Signal.DESTROYED

    def test_pieces_submarine_hit_results_in_kill(self):
        s = Submarine(10)
        assert Signal.DESTROYED is s.hit(1)


@pytest.fixture()
def submarines_game():
    pieces = {
        SubmarinesPieces.GENERAL: 1,
        SubmarinesPieces.JETS: 1,
        SubmarinesPieces.DESTROYERS: 1,
        SubmarinesPieces.SUBMARINES: 1,
    }
    return SubmarinesGame(board_shape=(4, 4, 3), pieces=pieces)


class TestSubmarinesGame:
    """Tests for the executer class"""

    parsing_inputs = [
        ("(1, 2, 3)", (1, 2, 3)),
        ("0, 0, 0", (0, 0, 0)),
        ("((10, 20, 30))", (10, 20, 30)),
        ("1 1 1 1", (1, 1, 1, 1)),
        ("[6, 7, 8]", (6, 7, 8)),
        ("[6, 7, 8]]", (6, 7, 8)),
    ]

    coords_in_boards = [
            ((1, 1, 1), (1, 1, 1)),
            ((3, 3, 2), (3, 3, 2)),
            ((0, 0, 0), (0, 0, 0)),
            ((-1, 0, 0), False),
            ((1, 1, 1, 1), False),
            ((5, 1, 1), False),
            ]

    @pytest.mark.parametrize("inp, truth", parsing_inputs)
    def test_game_user_parsing(self, submarines_game, inp, truth):
        parsed = submarines_game._parse_coord_user_str_into_tuple(inp)
        assert parsed == truth

    def test_game_user_parsing_raises_userwarning(self, submarines_game):
        with pytest.warns(UserWarning):
            submarines_game._parse_coord_user_str_into_tuple('1-2-2')

    @pytest.mark.parametrize("inp, truth", coords_in_boards)
    def test_game_coord_in_board_valid_coord(self, submarines_game, inp, truth):
        returned = submarines_game._assert_coor_in_board(str(inp))
        assert truth == returned

    def test_game_too_small_of_a_board(self):
        with pytest.raises(AssertionError):
            SubmarinesGame(pieces={SubmarinesPieces.GENERAL: 1}, board_shape=(0, 0, 3))
    
    def test_game_too_small_of_a_board_incompatible_num_layers(self):
        with pytest.raises(AssertionError):
            SubmarinesGame(pieces={SubmarinesPieces.GENERAL: 1}, board_shape=(5, 5, 2))


class TestThreeDBoard:
    """Tests for the board class."""

    def test_board_place_pieces(self, submarines_game):
        submarines_game.board1.place_pieces()
        submarines_game.board2.place_pieces()


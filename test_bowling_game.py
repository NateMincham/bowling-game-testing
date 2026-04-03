import pytest
from bowling_game import BowlingGame


def roll_many(game, rolls):
    for pins in rolls:
        game.roll(pins)


def test_new_game_score_is_zero():
    game = BowlingGame()
    assert game.score() == 0


def test_gutter_game():
    game = BowlingGame()
    roll_many(game, [0] * 20)
    assert game.score() == 0


def test_all_ones():
    game = BowlingGame()
    roll_many(game, [1] * 20)
    assert game.score() == 20


def test_one_spare():
    game = BowlingGame()
    roll_many(game, [5, 5, 3] + [0] * 17)
    assert game.score() == 16


def test_one_strike():
    game = BowlingGame()
    roll_many(game, [10, 3, 4] + [0] * 16)
    assert game.score() == 24


def test_perfect_game():
    game = BowlingGame()
    roll_many(game, [10] * 12)
    assert game.score() == 300


def test_all_spares():
    game = BowlingGame()
    roll_many(game, [5] * 21)
    assert game.score() == 150


def test_regular_game():
    game = BowlingGame()
    rolls = [3, 4, 2, 5, 1, 6, 4, 2, 8, 1, 7, 1, 5, 3, 2, 3, 4, 3, 2, 6]
    roll_many(game, rolls)
    assert game.score() == 72


def test_example_game():
    game = BowlingGame()
    rolls = [10, 3, 6, 5, 5, 8, 1, 10, 10, 10, 9, 0, 7, 3, 10, 10, 8]
    roll_many(game, rolls)
    assert game.score() == 190


def test_tenth_frame_spare():
    game = BowlingGame()
    roll_many(game, [0] * 18 + [5, 5, 7])
    assert game.score() == 17


def test_tenth_frame_strike():
    game = BowlingGame()
    roll_many(game, [0] * 18 + [10, 10, 8])
    assert game.score() == 28


def test_double_strike():
    game = BowlingGame()
    roll_many(game, [10, 10, 4, 2] + [0] * 14)
    assert game.score() == 46


def test_negative_pins_invalid():
    game = BowlingGame()
    with pytest.raises(ValueError):
        game.roll(-1)


def test_more_than_ten_pins_invalid():
    game = BowlingGame()
    with pytest.raises(ValueError):
        game.roll(11)


def test_frame_total_cannot_exceed_ten():
    game = BowlingGame()
    game.roll(8)
    with pytest.raises(ValueError):
        game.roll(5)


def test_cannot_roll_after_game_is_complete():
    game = BowlingGame()
    roll_many(game, [0] * 20)
    with pytest.raises(ValueError):
        game.roll(1)
"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    """
    Represents a standard ten-pin bowling game.
    Records rolls, validates input, and calculates bowling scores.
    """

    def __init__(self):
        """Initialize a new bowling game."""
        self.rolls = []

    def roll(self, pins):
        """
        Record a roll in the game.

        Args:
            pins (int): Number of pins knocked down.

        Raises:
            ValueError: If the roll is invalid or the game is complete.
        """
        if not isinstance(pins, int):
            raise ValueError("Pins must be an integer.")

        if pins < 0:
            raise ValueError("Pins cannot be negative.")

        if pins > 10:
            raise ValueError("Pins cannot be greater than 10.")

        if self._is_game_complete():
            raise ValueError("Cannot roll after game is complete.")

        self._validate_frame_rules(pins)
        self.rolls.append(pins)

    def score(self):
        """
        Calculate the total score for the game.

        Returns:
            int: Total score.
        """
        if not self.rolls:
            return 0

        score = 0
        frame_index = 0

        for _ in range(10):
            if frame_index >= len(self.rolls):
                break

            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self._frame_score(frame_index)
                frame_index += 2

        return score

    def _is_strike(self, frame_index):
        """Return True if the frame is a strike."""
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        """Return True if the frame is a spare."""
        return (
            frame_index + 1 < len(self.rolls)
            and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10
        )

    def _strike_bonus(self, frame_index):
        """Return the strike bonus."""
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _spare_bonus(self, frame_index):
        """Return the spare bonus."""
        return self.rolls[frame_index + 2]

    def _frame_score(self, frame_index):
        """Return the score of an open frame."""
        return self.rolls[frame_index] + self.rolls[frame_index + 1]

    def _validate_frame_rules(self, pins):
        """
        Validate that the roll does not break bowling frame rules.

        Raises:
            ValueError: If the roll creates an illegal frame state.
        """
        frame = 1
        i = 0

        # Work through frames 1-9
        while frame <= 9:
            if i >= len(self.rolls):
                # Start of a new frame, so any single roll 0-10 is valid
                return

            first_roll = self.rolls[i]

            if first_roll == 10:
                # Strike frame
                i += 1
                frame += 1
            else:
                # If only first roll exists in this frame, validate second roll
                if i == len(self.rolls) - 1:
                    if first_roll + pins > 10:
                        raise ValueError("Frame total cannot exceed 10 pins.")
                    return

                # Frame already complete, move to next
                i += 2
                frame += 1

        # 10th frame validation
        tenth_rolls = self.rolls[i:]

        if len(tenth_rolls) == 0:
            return

        if len(tenth_rolls) == 1:
            first = tenth_rolls[0]
            if first != 10 and first + pins > 10:
                raise ValueError(
                    "10th frame total cannot exceed 10 unless first roll is a strike."
                )
            return

        if len(tenth_rolls) == 2:
            first, second = tenth_rolls[0], tenth_rolls[1]

            # No third roll unless strike or spare
            if first != 10 and first + second != 10:
                raise ValueError("No bonus roll allowed without strike or spare in 10th frame.")

            # If first roll was strike and second was not strike,
            # then second + third must not exceed 10
            if first == 10 and second != 10 and second + pins > 10:
                raise ValueError("Invalid bonus roll total in 10th frame.")

            return

        # Already 3 rolls in 10th frame -> game should be complete
        raise ValueError("Cannot roll after game is complete.")

    def _is_game_complete(self):
        """
        Return True if the game is complete.
        """
        frame = 1
        i = 0

        # Frames 1-9
        while frame <= 9:
            if i >= len(self.rolls):
                return False

            if self.rolls[i] == 10:
                i += 1
            else:
                if i + 1 >= len(self.rolls):
                    return False
                i += 2

            frame += 1

        # 10th frame
        remaining = self.rolls[i:]

        if len(remaining) < 2:
            return False

        first, second = remaining[0], remaining[1]

        if first == 10 or first + second == 10:
            return len(remaining) >= 3

        return len(remaining) >= 2
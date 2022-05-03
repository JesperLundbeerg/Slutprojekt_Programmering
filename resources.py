#Jesper Lundberg
#TEINF20
#Wordle a fun game - resources

class Wordle:

    Max_attempts = 6
    Word_length = 5

    def __init__(self, secretw : str):
        self.secretw = secretw
        self.attempts = []
        pass

    def attempt(self, word : str):
        self.attempts.append(word)

    def guess(self, word: str):
        result = []

        for i in range(self.Word_length):
            character = word[i]
            letter = LetterCondition(character)
            letter.in_word = character in self.secretw
            letter.in_position = character == self.secretw[i]
            result.append(letter)

        return result

    # Denna talar om, om du vunnit eller inte
    @property
    def correct_guess(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secretw


    # Denna talar om hur många försök du har kvar
    @property
    def attempts_left(self) -> int:
        return self.Max_attempts - len(self.attempts)


    # Denna talar om, om du får gissa igen
    @property
    def can_attempt(self):
        return self.attempts_left > 0 and not self.correct_guess


class LetterCondition:
    def __init__(self, character : str):
        self.character = character
        self.in_word: bool = False
        self.in_position: bool = False

    # Talar om bokstaven finns i ordet (början på det iaf)
    def __repr__(self):
        return f"[{self.character} in_word: {self.in_word} in_position: {self.in_position}]"
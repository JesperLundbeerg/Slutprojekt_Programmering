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


    # Denna talar om, om du vunnit eller inte
    @property
    def correct_guess(self):
        return self.attempts[-1] == self.secretw


    # Denna talar om hur många försök du har kvar
    @property
    def attempts_left(self) -> int:
        return self.Max_attempts - len/self.attempts


    # Denna talar om, om du får gissa igen
    @property
    def can_attempt(self):
        return self.attempts_left == 0 and not self.correct_guess

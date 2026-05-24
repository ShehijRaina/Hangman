MAX_LIVES = 6

class Hangman():
    # Constructor
    def __init__(self, string_to_guess, author="", lives=MAX_LIVES):
        self.max_lives       = lives
        self.remaining_lives = self.max_lives
        self.string_to_guess = string_to_guess.upper()
        self.author          = author
        self.guessed_letters = set()

    # Get the string displayed to the player, with unguessed letters as underscores
    def get_guessed_string(self):
        displayed_string = ""

        for char in self.string_to_guess:
            if char.isalpha():
                if char in self.guessed_letters:
                    displayed_string += char
                else:
                    displayed_string += "_"
            else:
                displayed_string += char

        return displayed_string 

    # Handle keyboard input from the player
    def handle_guess(self, letter):
        if (not letter.isalpha()) or (len(letter) != 1):
            raise ValueError("Input must be a single letter!")
        letter = letter.upper()

        # Letter has already been guessed, ignore it
        if letter in self.guessed_letters:
            return
        
        self.guessed_letters.add(letter)

        if letter not in self.string_to_guess:
            self.remaining_lives -= 1

    # Check for victory
    def did_win(self):
        if self.remaining_lives <= 0:
            return False
        
        for char in self.string_to_guess:
            if char.isalpha() and char not in self.guessed_letters:
                return False
            
        return True
    
    # Check for defeat
    def did_lose(self):
        return self.remaining_lives <= 0

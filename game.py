from hangman import Hangman
from image   import HangmanImage
from quotes  import load_quotes

import random
from PyQt6.QtCore    import Qt
from PyQt6.QtGui     import QKeyEvent
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QMessageBox


class Game(QWidget):

    # Constructor
    def __init__(self, quotes=load_quotes()):
        super().__init__()
        
        self.quotes = quotes
        self.init_game()
        self.setup_ui()

    # Pick a quote and initialize the game state
    def init_game(self):
        quote, author = random.choice(self.quotes)
        self.game = Hangman(quote, author)

    # Set up the user interface
    def setup_ui(self):
        self.setWindowTitle("HANGMAN")
        self.setGeometry(200, # x-coordinate of window
                        200,  # y-coordinate of window
                        800,  # width of window
                        600)  # height of window

        # Apply some styling
        stylesheet = 'data/stylesheet.txt'
        with open(stylesheet, 'r') as file:
            content = file.read()
            self.setStyleSheet(content)

        # Align content to center
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Window content
        title_label = QLabel("HANGMAN")
        title_label.setObjectName("title")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        self.quote_display = QLabel()
        self.quote_display.setObjectName("quote")
        self.quote_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.quote_display.setWordWrap(True)
        layout.addWidget(self.quote_display)

        self.lives_display = QLabel()
        self.lives_display.setObjectName("lives")
        self.lives_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.lives_display)

        self.hangman_image = HangmanImage()
        self.hangman_image.setObjectName("image")
        self.hangman_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.hangman_image, stretch=1)

        self.setLayout(layout)
        self.update_ui()

    # Update the user interface based on the current game state
    def update_ui(self):
        self.quote_display.setText(self.game.get_guessed_string())
        self.lives_display.setText(f'Lives Remaining: {self.game.remaining_lives}')
        self.hangman_image.set_stage(self.game.max_lives - self.game.remaining_lives)
        self.check_game_status()

    # Handle keyboard input for guessing letters
    def keyPressEvent(self, event: QKeyEvent):
        if event.text().isalpha() and len(event.text()) == 1:
            letter = event.text().upper()
            self.game.handle_guess(letter)
            self.update_ui()

    def check_game_status(self):
        if self.game.did_win():
            QMessageBox.information(self,
                                    "VICTORY!",
                                    f"Congratulations!, You've guessed it!\n\"{self.game.string_to_guess}\"\n~ {self.game.author}")
            self.restart_game()
        elif self.game.did_lose():
            QMessageBox.information(self, 
                                    "TRY AGAIN!",
                                    f'The quote was: "{self.game.string_to_guess }"\n~ {self.game.author}')
            self.restart_game()

    def restart_game(self):
        self.init_game()
        self.update_ui()
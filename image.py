from PyQt6.QtWidgets import QSizePolicy, QLabel
from PyQt6.QtCore import Qt

# Hangman ASCII Art from 
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']



# Hangman Image Widget
class HangmanImage(QLabel):

    # Constructor
    def __init__(self):
        super().__init__()

        # Initialize stage to 0 (no parts drawn)
        self.stage = 0
        self.setText(HANGMANPICS[self.stage])
        
		#  Never wrap ASCII Art
        self.setTextFormat(Qt.TextFormat.PlainText)
        self.setWordWrap(False)
        self.setSizePolicy(
				QSizePolicy.Policy.Expanding,
				QSizePolicy.Policy.Expanding)

    # Set stage 0-6
    def set_stage(self, stage):
        if stage < 0 or stage >= len(HANGMANPICS):
            raise ValueError(f'Stage must be between 0 and {len(HANGMANPICS) - 1}')

        self.stage = stage
        self.setText(HANGMANPICS[self.stage])
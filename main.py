from game import Game

import sys
from PyQt6.QtWidgets import QApplication

# Run App
if __name__ == "__main__":
    app    = QApplication(sys.argv)
    window = Game()
    window.show()
    sys.exit(app.exec())
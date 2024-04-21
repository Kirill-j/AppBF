from PySide6.QtWidgets import QApplication
from app import Application
import sys

app = QApplication(sys.argv)

window = Application()
window.show()

app.exec()

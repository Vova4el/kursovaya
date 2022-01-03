from PyQt5.QtWidgets import QApplication
from log_window import *
import sys
app = QApplication(sys.argv)
window = log_panel()
window.show()
sys.exit(app.exec_())

from Qt import *
from window_class import *
from Authentication import *
import sys
app = QApplication(sys.argv)
window = log_panel()
window.show()
sys.exit(app.exec_())

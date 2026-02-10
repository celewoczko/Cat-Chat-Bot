import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle("Qt Test")
w.resize(200, 150)
w.show()
sys.exit(app.exec_())
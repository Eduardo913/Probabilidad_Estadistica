import sys
from PyQt5.QtWidgets import QApplication
from Controller.ControllerPrincipal import ControllerPrincipal


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ControllerPrincipal()
    widget.show()
    sys.exit(app.exec_())





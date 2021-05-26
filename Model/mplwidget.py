from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

from matplotlib.figure import Figure

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT

class MplWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        fig = Figure(dpi=60)
        gs = fig.add_gridspec(10, 10)
        fig.tight_layout()
        self.canvas = FigureCanvasQTAgg(fig)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        vertical_layout.addWidget(self.toolbar)
        self.canvas.axes = self.canvas.figure.add_subplot(gs[:-1, 0:])
        # self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
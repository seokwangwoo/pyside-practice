# main.py

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('PySide6 Example')
        
        # Set the central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        # Add a button to open file explorer
        self.open_file_button = FileExplorerButton(self)
        layout.addWidget(self.open_file_button)
        
        # Set the layout to the central widget
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

class FileExplorerButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__("Open File", parent)
        self.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open File")
        if file_path:
            print("Selected file:", file_path)

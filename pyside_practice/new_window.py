from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QLabel

class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Window")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()
        label = QLabel("This is a new window")
        layout.addWidget(label)
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        self.new_window_button = QPushButton("Open New Window")
        self.new_window_button.clicked.connect(self.show_new_window)
        
        layout.addWidget(self.new_window_button)
        self.setLayout(layout)
        
        self.new_window = None  # Placeholder for the new window instance

    def show_new_window(self):
        if self.new_window is None:
            self.new_window = NewWindow()
        self.new_window.show()

if __name__ == "__main__":
    # Initialize the application
    app = QApplication([])

    # Create and show the main window
    main_window = MainWindow()
    main_window.show()

    # Run the application's event loop
    app.exec()

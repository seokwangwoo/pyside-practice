"""Main module."""

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import sys

# Step 1: Create the main application
app = QApplication(sys.argv)

# Step 2: Create the main window
main_window = QMainWindow()
main_window.setWindowTitle('PySide6 Example')

# Step 3: Set the central widget and layout
central_widget = QWidget()
layout = QVBoxLayout()

# Step 4: Add a button to the layout
button = QPushButton('Click Me')
layout.addWidget(button)

# Step 5: Set the layout to the central widget
central_widget.setLayout(layout)
main_window.setCentralWidget(central_widget)

# Step 6: Show the main window
main_window.show()

# Step 7: Execute the application
sys.exit(app.exec())

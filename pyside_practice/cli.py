"""Console script for pyside_practice."""

import sys

import click
from PySide6.QtWidgets import QApplication
from pyside_practice.main_window import MainWindow

@click.command()
def main():
    # Step 1: Create the main application
    app = QApplication(sys.argv)

    # Step 2: Create and show the main window
    main_window = MainWindow()
    main_window.show()

    # Step 3: Execute the application
    sys.exit(app.exec())


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

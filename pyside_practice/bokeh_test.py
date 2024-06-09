import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QPushButton, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from bokeh.plotting import figure
from bokeh.embed import file_html
from bokeh.resources import CDN

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        # Generate initial Bokeh plot HTML content
        self.html_content = self.generate_bokeh_html()

        # Create a central widget with a vertical layout
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        # Create a QStackedWidget and add it to the layout
        self.stacked_widget = QStackedWidget()
        layout.addWidget(self.stacked_widget)

        # Create a QWebEngineView and add it to the QStackedWidget
        self.web_view = QWebEngineView()
        self.stacked_widget.addWidget(self.web_view)

        # Load initial HTML content into the QWebEngineView
        self.web_view.setHtml(self.html_content)

        # Create a button to update the HTML content
        update_button = QPushButton("Update Content")
        update_button.clicked.connect(self.update_content)
        layout.addWidget(update_button)

        # Set the central widget
        self.setCentralWidget(central_widget)

    def generate_bokeh_html(self):
        # Create a Bokeh plot
        plot = figure(title="Bokeh Plot Example")
        plot.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

        # Generate HTML content
        html = file_html(plot, CDN, "Bokeh Plot")
        return html

    def update_content(self):
        # Generate new Bokeh plot HTML content
        new_html_content = self.generate_bokeh_html()

        # Load new HTML content into the QWebEngineView
        self.web_view.setHtml(new_html_content)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create the main window
    window = MyApp()
    window.show()
    
    sys.exit(app.exec())
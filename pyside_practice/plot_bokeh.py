import sys
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from bokeh.plotting import figure, show
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.themes import Theme
from bokeh.io import curdoc

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window with Bokeh Plot")
        self.setGeometry(100, 100, 800, 600)
        
        self.layout = QVBoxLayout()
        
        self.show_plot_button = QPushButton("Show Bokeh Plot")
        self.show_plot_button.clicked.connect(self.show_bokeh_plot)
        
        self.layout.addWidget(self.show_plot_button)
        
        self.web_view = QWebEngineView()
        styled_html = f"""
        <html>
        <head>
            <style>
                body {{
                    background-color: lightblue;
                }}
            </style>
        </head>
        <body>
        </body>
        </html>
        """
        self.web_view.setHtml(styled_html)
        self.layout.addWidget(self.web_view)
        
        self.setLayout(self.layout)
        
    def show_bokeh_plot(self):
        curdoc().theme = 'dark_minimal'

        # Create a Bokeh plot
        plot = figure(title="Bokeh Plot Example", x_axis_label='x', y_axis_label='y')

        plot.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], legend_label="Line", line_width=2)
        
        # Convert the Bokeh plot to an HTML format
        html = file_html(plot, CDN, "Bokeh Plot")
        
        # Set the HTML content of the QWebEngineView to display the Bokeh plot
        self.web_view.setHtml(html)

# Initialize the application
app = QApplication(sys.argv)

# Create and show the main window
main_window = MainWindow()
main_window.show()

# Run the application's event loop
sys.exit(app.exec())

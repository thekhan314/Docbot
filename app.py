import sys
import random
import numpy as np
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QDialog, QInputDialog

class ScreenshotClicker(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Screenshot Clicker")
        self.resize(600, 400)

        # Layouts
        layout = QVBoxLayout(self)
        config_layout = QHBoxLayout()
        
        # Screenshot list
        self.screenshot_list = QListWidget()
        self.screenshot_list.itemClicked.connect(self.display_full_screenshot)
        layout.addWidget(QLabel("Select Screenshots:"))
        layout.addWidget(self.screenshot_list)
        
        # Config inputs
        self.repeat_label = QLabel("Repetitions per Hour:")
        self.repeat_input = QtWidgets.QLineEdit()
        self.repeat_input.setPlaceholderText("Enter the target repetitions per hour")

        self.deviation_label = QLabel("Interval Deviation (seconds):")
        self.deviation_input = QtWidgets.QLineEdit()
        self.deviation_input.setPlaceholderText("Enter deviation in seconds")

        # Take Screenshot button
        self.screenshot_button = QtWidgets.QPushButton("Take Screenshot")
        self.screenshot_button.clicked.connect(self.start_screenshot_selection)
        
        # Click button
        self.start_button = QtWidgets.QPushButton("Start Clicking")
        self.start_button.clicked.connect(self.start_clicking)

        # Assemble layouts
        config_layout.addWidget(self.repeat_label)
        config_layout.addWidget(self.repeat_input)
        config_layout.addWidget(self.deviation_label)
        config_layout.addWidget(self.deviation_input)
        layout.addLayout(config_layout)
        layout.addWidget(self.screenshot_button)
        layout.addWidget(self.start_button)

        self.screenshots = []
        self.selection_rect = None
        self.is_selecting = False

    def start_screenshot_selection(self):
        # Initialize full-screen transparent overlay for selection
        self.overlay = ScreenshotOverlay(self)
        self.overlay.show()

    def save_screenshot(self, screenshot):
        """Prompt for a name, save the screenshot, create a thumbnail, and add it to the screenshot list."""
        # Prompt the user for a name for the screenshot
        name, ok = QInputDialog.getText(self, "Screenshot Name", "Enter a name for this screenshot:")
        
        if ok and name:
            self.screenshots.append(screenshot)

            # Create a thumbnail for display in the QListWidget
            thumbnail = screenshot.scaled(100, 100, QtCore.Qt.AspectRatioMode.KeepAspectRatio, 
                                          QtCore.Qt.TransformationMode.SmoothTransformation)

            item = QListWidgetItem(name)
            item.setIcon(QtGui.QIcon(thumbnail))
            item.setData(QtCore.Qt.ItemDataRole.UserRole, screenshot)  # Store full-size screenshot for later
            self.screenshot_list.addItem(item)

    def display_full_screenshot(self, item):
        """Show the full-size screenshot in a dialog window when a list item is clicked."""
        screenshot = item.data(QtCore.Qt.ItemDataRole.UserRole)
        
        # Create a dialog to display the full screenshot
        dialog = QDialog(self)
        dialog.setWindowTitle("Screenshot Preview")
        dialog.resize(screenshot.width(), screenshot.height())

        label = QLabel(dialog)
        label.setPixmap(screenshot)
        dialog_layout = QVBoxLayout(dialog)
        dialog_layout.addWidget(label)

        dialog.exec()

    def start_clicking(self):
        # Collect parameters
        try:
            repetitions_per_hour = float(self.repeat_input.text())
            mean_interval = (60 / repetitions_per_hour) * 60
            deviation = float(self.deviation_input.text())
        except ValueError:
            QtWidgets.QMessageBox.critical(self, "Input Error", "Please enter valid numbers.")
            return

        selected_items = [item.text() for item in self.screenshot_list.selectedItems()]
        selected_indices = [int(text.split()[-1]) - 1 for text in selected_items]

        if not selected_indices:
            QtWidgets.QMessageBox.warning(self, "Selection Error", "Please select at least one screenshot.")
            return

        # Set up clicking repetitions
        for i in range(int(repetitions_per_hour)):
            for index in selected_indices:
                screenshot = self.screenshots[index]
                # Locate screenshot on screen and click if found
                loc = QtGui.QGuiApplication.primaryScreen().grabWindow(0).toImage().copy()
                if screenshot == loc:
                    pyautogui.click(loc)
            interval = np.random.normal(mean_interval, deviation)
            QtCore.QThread.msleep(int(max(0, interval)) * 1000)


class ScreenshotOverlay(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint |
            QtCore.Qt.WindowType.Tool
        )
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(QtGui.QGuiApplication.primaryScreen().geometry())
        self.parent = parent
        self.origin = QtCore.QPoint()
        self.end = QtCore.QPoint()

    def mousePressEvent(self, event):
        self.origin = event.pos()
        self.end = event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()
        # Capture the screenshot from the selected area
        x1 = min(self.origin.x(), self.end.x())
        y1 = min(self.origin.y(), self.end.y())
        x2 = max(self.origin.x(), self.end.x())
        y2 = max(self.origin.y(), self.end.y())
        rect = QtCore.QRect(x1, y1, x2 - x1, y2 - y1)
        screenshot = QtGui.QGuiApplication.primaryScreen().grabWindow(0, rect.x(), rect.y(), rect.width(), rect.height())
        self.parent.save_screenshot(screenshot)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)
        painter.setPen(QtGui.QPen(QtCore.Qt.GlobalColor.green, 2))
        painter.setBrush(QtGui.QColor(0, 0, 0, 50))  # Semi-transparent overlay

        # Draw the selection rectangle
        if not self.origin.isNull() and not self.end.isNull():
            painter.drawRect(QtCore.QRect(self.origin, self.end))


app = QtWidgets.QApplication(sys.argv)
window = ScreenshotClicker()
window.show()
sys.exit(app.exec())

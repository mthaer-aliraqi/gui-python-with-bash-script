import sys
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (
    QApplication,QWidget,
    QVBoxLayout,QPushButton,
    QRadioButton,QCheckBox,QLabel
    )

class Gui(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(450,320) # or u can add it outside with __main__

        # elements
        layout = QVBoxLayout()

        label = QLabel("Check Box")

        self.check_box = QCheckBox("my check box")
        self.check_box.checkStateChanged.connect(self.on_checked)

        self.label2 = QLabel("Radio Button")

        self.rb1 = QRadioButton("Radio button 1")
        self.rb1.toggled.connect(self.on_radio)

        self.rb2 = QRadioButton("Radio button 2")
        self.rb2.toggled.connect(self.on_radio)

        self.bt1 = QPushButton("save changes")

        # add to screen
        layout.addWidget(label)
        layout.addWidget(self.check_box)
        layout.addWidget(self.label2)
        layout.addWidget(self.rb1)
        layout.addWidget(self.rb2)
        layout.addWidget(self.bt1)
        self.setLayout(layout)
        

    def on_checked(self):
        check_box_state = self.check_box.isChecked()  
        self.bt1.setVisible(check_box_state)    # widnow will rhink when hide
        self.label2.setHidden(check_box_state)     # when hide will not shrink the wiindow

    def on_radio(self):
        if (self.rb1.isChecked()):
            self.bt1.setText("RB1")
        elif (self.rb2.isChecked()):
             self.bt1.setText("RB2")
            
        


# runs this block only if it is main not imported by another file
# python doesnot have main function like java/kotlin
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Gui()
    window.setWindowTitle("Structure of python")
    # widndow.resize(600,400)
    window.show()
    sys.exit(app.exec())
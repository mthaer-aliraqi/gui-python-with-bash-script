import os , sys
from PySide6.QtWidgets import (
    QApplication,
    QWidget,QMessageBox,
    QFileDialog,QPushButton,
    QVBoxLayout,QLabel
)
# import image to show on dialog
from PySide6.QtGui import QPixmap


class MainGui(QWidget):
    def __init__(self):
        super().__init__()

        #elements
        layout = QVBoxLayout()

        self.label = QLabel("this is create to show how to show dialog and popup")

        #buttons
        self.bt1 = QPushButton("show succsess")
        self.bt1.clicked.connect(self.on_click1)
        
        self.bt2 = QPushButton("show warning")
        self.bt2.clicked.connect(self.on_click2)
        
        self.bt3 = QPushButton("show error")
        self.bt3.clicked.connect(self.on_click3)
        
        self.bt4 = QPushButton("show question")
        self.bt4.clicked.connect(self.on_click4)

        self.bt5 = QPushButton("show custom dialog")
        self.bt5.clicked.connect(self.show_custom_dialog)
        
        self.bt6 = QPushButton("show file picker dialog")
        self.bt6.clicked.connect(self.show_file_picker)

        layout.addWidget(self.label)
        layout.addWidget(self.bt1)
        layout.addWidget(self.bt2)
        layout.addWidget(self.bt3)
        layout.addWidget(self.bt4)
        layout.addWidget(self.bt5)
        layout.addWidget(self.bt6)
        self.setLayout(layout)

    # functions
    def on_click1(self):
        # shows dialog for messages
        self.msg_box1 = QMessageBox()
        self.msg_box1.information(self,"Success","Blue icon")
    
    def on_click2(self):
        # shows dialog for messages
        self.msg_box2 = QMessageBox()   #not required for short dialog u can do as next def it will work
        self.msg_box2.information(self,"Careful","Yellow triangle icon")
    
    def on_click3(self):
        # shows dialog for messages
        QMessageBox().information(self,"Error","Red error icon")

    def on_click4(self):
        #show question answer with yes/no
        reply = QMessageBox.question(
              self,
              "Confirmation",
              "take an option",
                QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No
            )
         
        # take answer and check if it is equals yes or no
        if (reply == QMessageBox.StandardButton.Yes):
              self.label.setText("yes clicked")
        else:
            self.label.setText("no clicked")

    def show_custom_dialog(self):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("window title")
        msg_box.setText("This dialog uses my own image!")
        
        # 2. Get the exact folder directory where this python script lives
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 3. Join that folder path with your image's file name
        # Make sure "image_466805.png" is in the same folder as this script
        icon_path = os.path.join(script_dir, "image_466805.png") 
        
        # 4. Load the image using the full generated path
        custom_icon = QPixmap(icon_path) 
        msg_box.setIconPixmap(custom_icon)
        
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def show_file_picker(self):
        # open file picker
        file_path,_ = QFileDialog.getOpenFileName(self,"1st","2nd","3rd")
        # if user select file and didnot hit cancel
        if (file_path):
            QMessageBox.information(self,"File selected",f"you picked:\n{file_path}")
        else:
            QMessageBox.information(self,"file picker canceled","file canceled")
         



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainGui()
    window.setWindowTitle("python - gui 3")
    window.resize(450,320)
    window.show()
    sys.exit(app.exec())
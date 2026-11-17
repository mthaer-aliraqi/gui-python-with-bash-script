import os , sys , shlex
from PySide6.QtCore import QProcess
from PySide6.QtWidgets import (
    QApplication,QPushButton,QVBoxLayout,
    QWidget,QTextEdit,QLabel,QLineEdit
)

class BashGui(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(450,320)

        # elements
        layout = QVBoxLayout()

        label = QLabel("pick the bash script and click run to see the code running")

        self.path_field = QLineEdit()
        self.path_field.setPlaceholderText("paste your script full path")

        label2 = QLabel("Live Running Script")

        self.term = QTextEdit()
        self.term.setReadOnly(True)
        self.term.setMaximumHeight(160)
        self.term.setStyleSheet("background-color: #1e1e1e; color: #00ff66; font-family: monospace;")

        self.args = QLineEdit()
        self.args.setPlaceholderText("script arguments")

        self.bt = QPushButton("Run")
        self.bt.clicked.connect(self.on_bt_clicked)

        # add to screen
        layout.addWidget(label)
        layout.addWidget(self.path_field)
        layout.addWidget(label2)
        layout.addWidget(self.term)
        layout.addWidget(self.args)
        layout.addWidget(self.bt)
        self.setLayout(layout)

        #setup Qprocess which will run the script
        self.process = QProcess(self)
        # merge stdout and stderr both appears on screen
        self.process.setProcessChannelMode(QProcess.ProcessChannelMode.MergedChannels)
        # when terminl output line by line runs functon
        self.process.readyReadStandardOutput.connect(self.on_output_ready)
        #when script finished 
        self.process.finished.connect(self.on_finished)

    # functions
    def on_output_ready(self):
        # takes data from terminal
        raw_bytes = bytes(self.process.readAllStandardOutput().data())
        # convert it into string
        text = raw_bytes.decode("utf-8", errors="replace")
        # append to textField
        self.term.insertPlainText(text)
        # makes sure the textField scrolls to the bottom on text changed
        self.term.ensureCursorVisible()


    def on_finished(self,exit_code,exit_status):
        self.term.append(f"\n--- Done (Code: {exit_code}) ---")
        #enable button
        self.bt.setEnabled(True)


    def on_bt_clicked(self):

        # get script path
        script_path = self.path_field.text().strip()

        #saftey
        if (script_path == ""):
            self.term.setText("Err: no script path entered !")
            return
        
        if (not os.path.isfile(script_path)):
            self.term.setText("Err: file not exist !")
            return
        
        self.term.clear()

        user_args = shlex.split(self.args.text())
        # -x for print the code into terminal u can erase it
        cmd_args = ["-x", script_path] + user_args

        #disable button
        self.bt.setEnabled(False)
        # run script
        self.process.start("bash", cmd_args)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BashGui()
    window.show()
    sys.exit(app.exec())
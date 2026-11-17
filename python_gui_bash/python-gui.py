# sys gives me sys.argv (CLI args)
import sys
#required for the script of bash
import subprocess
# the tool create gui window
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QPushButton,QLineEdit,QTextEdit

# Python's from X import Y is like Kotlin's import X.Y.

# when buttons clicked

def on_click():
    output.setText("clicked")

def print_text():
    user_input = single_line_input.text()
    output2.setText(user_input)

def on_run():
    text1 = long_text_edit.toPlainText()

    result = subprocess.run(
        ["sh","hi.sh","arg1",text1],
        capture_output=True,
        text=True
    )

    long_text_edit.setText("stdout: "+result.stdout+"\n err: "+result.stderr+"\n runCode")
    print(result.returncode)


# app engine type
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("window title")

layout = QVBoxLayout()

button = QPushButton("button")
button.clicked.connect(on_click)

bt2 = QPushButton("print")
bt2.clicked.connect(print_text)

bt3 = QPushButton("run script")
bt3.clicked.connect(on_run)

output = QLabel("not clicked")
output2 = QLabel("not clicked")

long_text_edit = QTextEdit()
long_text_edit.setPlaceholderText("this is long hint")
# for long text use QTextEdit() with .setReadOnly(True)

single_line_input = QLineEdit()
single_line_input.setPlaceholderText("this is hint")

# add to layout
layout.addWidget(button)
layout.addWidget(bt2)
layout.addWidget(bt3)
layout.addWidget(output)
layout.addWidget(output2)
layout.addWidget(long_text_edit)
layout.addWidget(single_line_input)

# add layout to window
window.setLayout(layout)

# shows the window
window.show()

sys.exit(app.exec())

# What this means: app.exec() starts the event loop — it blocks and processes clicks/keys
#  until the window closes. sys.exit(...) makes Python exit with the loop's return code.
#  This line must be last.

# you can use qtdesigner app to build gui easily
# --------- basics -------------
# just method
def main():
    print("running")

# runs this block only if it is main not imported by another file
# python doesnot have main function like java/kotlin/gdscript
if __name__ == "__main__":
    main()
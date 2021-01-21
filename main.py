import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit, QProgressBar
from save import Download


win_width, win_height = 800, 400
win_x, win_y = 600, 400

txt_title = "App for downloading Sound & Video from YouTube"
txt_send = "Save MP3"
txt_send2 = "Save Video"
txt_line = "Enter URL from YouTube"
error_txt = "Error! Fill in the field!"
error_404 = "Error 404!"
success_text = "Upload successful."

CSS = '''
QLineEdit {
    font-size: 20px;
    width: 800px;
    height: 60px;
    padding: 0 10px;
    margin: 0;
    border: 4px solid #f00;
}
QPushButton {
    font-size: 32px;
    width: 400px;
    height: 55px;
    color: #fff;
    background: #f00;
}
'''

class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):

        super().__init__(parent=parent, flags=flags)

        self.opt = 'video'

        self.initUI()

        self.connects()

        self.set_appear()

        self.show()

    def initUI(self):
        self.btn_send = QPushButton(txt_send, self)
        self.btn_send2 = QPushButton(txt_send2, self)
        self.line = QLineEdit('https://www.youtube.com/watch?v=hS5CfP8n_js')
        self.line.setPlaceholderText(txt_line) 
        self.btn_send.setStyleSheet(CSS)
        self.btn_send2.setStyleSheet(CSS)
        self.line.setStyleSheet(CSS)
        self.status_text = QLabel(error_txt)
        self.status_text.setStyleSheet("color: red; font-size: 46px;")
        self.load_progress = QProgressBar(self)
        self.load_progress.setStyleSheet(f"width: {win_width}px; height: 40px;")
        self.status_text.hide()
        self.load_progress.hide()

        self.layout_line1 = QHBoxLayout()
        self.layout_line2 = QVBoxLayout()
        self.layout_line2.addWidget(self.status_text, alignment = Qt.AlignCenter)
        self.layout_line2.addWidget(self.load_progress, alignment = Qt.AlignBottom)
        self.layout_line2.addLayout(self.layout_line1)
        self.layout_line3 = QHBoxLayout()
        self.layout_line2.addLayout(self.layout_line3)
        self.layout_line3.addWidget(self.btn_send, alignment = Qt.AlignTop)
        self.layout_line3.addWidget(self.btn_send2, alignment = Qt.AlignTop)
        self.layout_line1.addWidget(self.line, alignment = Qt.AlignBottom)
        self.setLayout(self.layout_line2)

    
    def save(self):
        sender = self.sender()
        if sender.text() == txt_send2:
            self.opt = 'video'
        else:
            self.opt = 'audio'
        if len(self.line.text()) > 0:
            try:
                self.status_text.hide()
                self.load_progress.show()
                progress = Download(self.line.text(), self.opt)
                self.save_in_file()
                while progress: 
                    print(progress)
                    self.load_progress.setValue(i)
                    if i > 99:
                        self.load_progress.hide()
                        self.load_progress.setValue(0)
                        self.line.setText('')
                        self.status_text.setStyleSheet("color: green; font-size: 46px;")
                        self.status_text.setText(success_text)
                        self.status_text.show()
                        break
            except:
                self.load_progress.hide()
                self.status_text.setText(error_404)
                self.status_text.setStyleSheet("color: red; font-size: 46px;")
                self.status_text.show()
        else:
            self.status_text.setText(error_txt)
            self.status_text.setStyleSheet("color: red; font-size: 46px;")
            self.status_text.show()
    
    # def save_in_file(self):
    #     file = open('list/list.txt')
    #     read = file.read().split(";")
    #     count_url = len(read)
    #     file.close()
    #     url = f"{count_url} - {self.line.text()};\n"
    #     file = open('list/list.txt', 'a')
    #     file.write(url)
    #     file.close()

    def save_in_file(self):
        with open('list/list.txt', 'r+') as file:
            urls = file.read().split(";")
            url_count = len(urls)
            url = f"{url_count} - {self.line.text()};\n"
            file.write(url)

    def connects(self):
        self.btn_send.clicked.connect(self.save)
        self.btn_send2.clicked.connect(self.save)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.setFixedSize(win_width, win_height)
        self.move(win_x, win_y)

def main():
    app = QApplication([])
    mw = MainWindow()
    app.exec_()

if __name__ == '__main__':
    main()
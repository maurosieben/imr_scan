import scan, sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread, QMutex
from main import Ui_MainWindow
import Image
import ImageQt
import ImageEnhance


class MyMainwindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.scan.clicked.connect(self.start)
        
        # Gui objects
        self.scene = QtGui.QGraphicsScene()
        self.view_he = self.ui.hegraph
        self.box =self.ui.log_text
        self.cursor = self.ui.log_text.textCursor()
        
    def start(self):
        # clear text box
        self.box.clear()
        # creates and starts threads to run scan
        self.mpthread = Thread("mp")
        self.connect(self.mpthread, QtCore.SIGNAL("mp"), self.append)
        self.mpthread.start()
        self.chthread = Thread("ch")
        self.connect(self.chthread, QtCore.SIGNAL("ch"), self.append)
        self.chthread.start()
        self.display_image('images/he.png')
        self.view_he.setScene(self.scene)
        
    # append data on the text box        
    def append(self, text):
        self.cursor.movePosition(self.cursor.End)
        self.cursor.insertText(text)
        self.box.ensureCursorVisible()
        

    def display_image(self, img):
        self.scene.clear()
        #w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
        pixMap = QtGui.QPixmap.fromImage(self.imgQ)
        myScaledPixmap = pixMap.scaled(self.view_he.size(), QtCore.Qt.KeepAspectRatio)#, KeepAspectRatio)
        self.scene.addPixmap(myScaledPixmap)
        self.scene.update()
        
class Thread(QThread):
    def __init__(self, signal):
        QThread.__init__(self)
        self.signal = signal

    def __del__(self):
        self.wait()

    def run(self):
        self.append_mp(self.signal)

    def append_mp(self,signal):
        lines =scan.choose_scan(signal)
        #lines  = scan.read_f("mp.log")
        for line in lines:
            self.emit(QtCore.SIGNAL(signal),line)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyMainwindow()
    myapp.showMaximized()
    #    atexit.register(kill_child)
    sys.exit(app.exec_())

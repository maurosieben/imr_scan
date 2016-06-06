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
        self.scene = []
        for i in range(0,3):
            print i
            self.scene.append(QtGui.QGraphicsScene())
        self.view = []
        self.view.append(self.ui.hegraph)
        self.view.append(self.ui.phapgraph)
        self.view.append(self.ui.dpgraph)
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
        
        scan.plot(scan.get_data('data.csv', 12), "DP")
        scan.plot(scan.get_data('data.csv', 7), "PHAP")
        scan.plot_he(scan.get_data('data.csv', 2),scan.get_data('data.csv', 3))
        self.display_image('images/he.png',0)
        self.display_image('images/DP.png',2)
        self.display_image('images/PHAP.png',1)
        
    # append data on the text box        
    def append(self, text):
        self.cursor.movePosition(self.cursor.End)
        self.cursor.insertText(text)
        self.box.ensureCursorVisible()
        
    def display_image(self, img, item):
        self.scene[item].clear()
        #w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
        pixMap = QtGui.QPixmap.fromImage(self.imgQ)
        myScaledPixmap = pixMap.scaled(self.view[item].size(), QtCore.Qt.KeepAspectRatio)#, KeepAspectRatio)
        self.scene[item].addPixmap(myScaledPixmap)
        self.scene[item].update()
        self.view[item].setScene(self.scene[item])
        
class Thread(QThread):
    def __init__(self, signal):
        QThread.__init__(self)
        self.signal = signal

    def __del__(self):
        self.wait()

    def run(self):
        self.append(self.signal)

    def append(self,signal):
        lines =scan.choose_scan(signal)
        for line in lines:
            self.emit(QtCore.SIGNAL(signal),line)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyMainwindow()
    myapp.showMaximized()
    #    atexit.register(kill_child)
    sys.exit(app.exec_())

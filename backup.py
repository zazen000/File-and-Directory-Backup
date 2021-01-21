import sys, os, subprocess
from qtpy_cfg import qblack, qlabel
from PyQt5.QtGui import QFont, QMovie
from PyQt5.QtCore import Qt, QFileSystemWatcher
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


path = "C:/Users/mount/source/repos/MyDashboard/oo.txt"

class Spinner( QWidget ):
    '''

    Creates a window for blu_circ.gif, a spinning indicator
    that shows the backup operation is being performed

    '''

    def __init__(self):
        super().__init__()
        self.left = 315
        self.top = 1
        self.width = 20
        self.height = 23

        qblack( self )              # PyQt5 window initialization function
        center  = Qt.AlignCenter
        canda_8 = QFont( 'Candalara', 8 )
        q_label = qlabel( self )    # PyQt5 label stylesheet function

        self.gif = QMovie( r'PNG\blu_circ.gif' )
        self.lbl = QLabel( self )
        self.lbl.setStyleSheet( q_label )
        self.lbl.setAlignment( center )
        self.lbl.setFont( canda_8 )
        self.lbl.setGeometry( 0, 0, 25, 23 )
        self.lbl.setMovie( self.gif )
        self.gif.start()


    def xit(self):
        '''

        Resets the status-check file 'oo.txt'
        to a blank file and closes the spinner

        '''
        ub.write_txt_file('oo.txt', '', "w")
        self.close()


if __name__ == '__main__':
    watcher = QFileSystemWatcher()  # Watches a file for any change in contents
    watcher.addPath( path )         # Path to the watched file
    app = QApplication( [] )
    e = Spinner()
    e.show()
    watcher.fileChanged.connect( e.xit )  # When file is changed, run xit()
    sys.exit( app.exec_() )



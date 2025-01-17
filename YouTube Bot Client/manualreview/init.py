import os
import sys
currentPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentPath.replace("\manualreview", ""))
import rawscriptsmenu
from PyQt5 import QtWidgets
import client
import sys
import atexit
import datetime
import configparser
import settings
from datetime import timedelta
import videoscriptcore
currentPath = os.path.dirname(os.path.realpath(__file__))



def loadVideoScripts():
    pass

class App():
    def __init__(self):
        application = QtWidgets.QApplication(sys.argv)
        application.processEvents()
        loginWindow = client.LoginWindow()
        loginWindow.show()


        #new = rawscriptsmenu.ScriptsMenu()
        #new.show()
        sys.exit(application.exec_())
        client.safeDisconnect()


sys._excepthook = sys.excepthook
def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    print("loooooooooooool")
    sys.exit(1)
sys.excepthook = exception_hook

def init():

    os.chdir(currentPath)

    if not os.path.exists(settings.thumbnailpath):
        os.mkdir(settings.thumbnailpath)

    if not os.path.exists(settings.scriptsaves):
        os.mkdir(settings.scriptsaves)

    app = App()

def exit_handler():
    print("Safe Exit")
    client.sock.close()



if __name__ == "__main__":
    atexit.register(exit_handler)
    settings.generateConfigFile()
    init()


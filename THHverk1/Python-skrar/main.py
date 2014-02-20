import sys
import Application
from PyQt4.QtGui import QApplication


################# MAIN ENTRY POINT OF THE APPLICATION #########################  
def main():                   
    app = QApplication(sys.argv)
    form = Application.Dialog()
    form.show()
    app.exec_()
    
main()

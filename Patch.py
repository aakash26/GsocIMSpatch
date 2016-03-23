"""
A trasnparent PyQt4 GUI which is able to read attributes from PowerSupply Device Server on Tango and write aswell

"""
import sys  
from PyQt4.QtGui import *  
from PyQt4 import QtCore  
import PyTango
from PyQt4 import QtGui
import PyTango

power_supply = PyTango.DeviceProxy("test/power_supply/1")


qt_app = QApplication(sys.argv)
 
class TangoDevice(QWidget):
    ''' A PyQT4 Gui to read attributes(current, voltage) and write attributes(current) to the  Tango Server of PowerSupply Device'''
    #to write current to device on button 'write' click
    def writevalue(self):
        self.currwrite=self.write.text()
        power_supply.current=float(self.currwrite)
    #to turnon the device
    def turon(self):
        power_supply.TurnOn()
    #to turnoff the device 
    def turnoff(self):
        power_supply.TurnOff()
    def valueread(self):
        self.currattribute= self.attribute.currentText()#to get the attribute selected by user in the dropdown.
        if(self.currattribute=="Current"):
            self.readvalue=str(power_supply.current)
            self.value.setPlaceholderText(self.readvalue)#setting the 'value' textbox read from tango server and displaying
        if(self.currattribute=="Voltage"):
            self.readvalue=str(power_supply.voltage)
            self.value.setPlaceholderText(self.readvalue)
        if(self.currattribute=="Status"):
            self.readvalue=str(power_supply.status())
            self.value.setPlaceholderText(self.readvalue)
        
    def __init__(self):
        # Initialize the object as a QWidget
        QWidget.__init__(self)
        self.setWindowOpacity(0.8)
        # We have to set the size of the main window
        self.setMinimumSize(600, 400)
        self.setWindowTitle('TangoDevice')
        self.greeting_lbl = QLabel('Please choose the attribute to read from the Power Supply Device Server:', self)
        # Create the controls with this object as their parent and set
        # their position individually; each row is a label followed by
        # another control
 
        # Label for the attribute chooser
        self.attribute_lbl = QLabel('attribute:', self)
        self.attribute_lbl.move(5, 50) # offset the first control 5px
                                       # from top and left
        self.attributes = ['Current','Voltage','Status']
        # Create and fill the combo box to choose the attribute
        self.attribute = QComboBox(self)
        self.attribute.addItems(self.attributes)
 
        self.attribute.setMinimumWidth(285)
        self.attribute.move(110, 50)
 
        # The label for the value control
        self.value_lbl = QLabel('value:', self)
        self.value_lbl.move(5, 130)
        self.readvalue=''
        # The value control is an entry textbox
        self.value = QLineEdit(self)
        # Add some ghost text to indicate what sort of thing to enter
        self.value.setPlaceholderText("value")
        # Same width as the attribute
        self.value.setMinimumWidth(285)
        self.value.move(110, 130)

	#the write label and write control which is an entry textbox
        self.write_lbl = QLabel('Write Current :',self)
        self.write_lbl.move(5,170)
        self.write =QLineEdit(self)
        self.write.setPlaceholderText("enter value")
        self.write.setMinimumWidth(285)
        self.write.move(110,170)
        self.write_button = QPushButton('Write Current', self)
 
        #write button with clicked.connect function to create an Onclick event to the writevalue function.
        self.write_button.setMinimumWidth(145)
        self.write_button.move(350, 170)
        self.write_button.clicked.connect(self.writevalue) # connect to writevalue()
 	
	#on and off button to turn the device on and off
        self.on_button = QPushButton('Turn Device On', self)
        self.off_button = QPushButton('Turn Device off', self) 
        self.on_button.setMinimumWidth(50)
        self.on_button.move(250, 250)
        self.on_button.clicked.connect(self.turon)
        self.off_button.setMinimumWidth(50)
        self.off_button.move(100, 250)
        self.off_button.clicked.connect(self.turnoff)
        # The read button is a push button
        self.read_button = QPushButton('Read Value', self)
 
        # Place it at the bottom right, narrower than
        # the other interactive widgets
        self.read_button.setMinimumWidth(145)
        self.read_button.move(350, 130)
        self.read_button.clicked.connect(self.valueread)
    
    def run(self):
        self.show()
        # Run the Qt application
        qt_app.exec_()
 
# Create an instance of the application window and run it
app = TangoDevice()
app.run()


"""Demo power supply tango device server"""

import time
import numpy

from PyTango import AttrQuality, AttrWriteType, DispLevel, DevState, DebugIt
from PyTango.server import Device, DeviceMeta, attribute, command, server_run
from PyTango.server import device_property


class PowerSupply(Device):
    __metaclass__ = DeviceMeta
    #attribute voltage only read
    voltage = attribute(label="Voltage", dtype=float,
                        display_level=DispLevel.OPERATOR,
                        access=AttrWriteType.READ,
                        unit="V",format="8.4f",
                        doc="the power supply voltage")
   #attribute current read and write both
    current = attribute(label="Current", dtype=float,
                        display_level=DispLevel.EXPERT,
                        access=AttrWriteType.READ_WRITE,
                        unit="A",format="8.4f",
                        min_value=0.0, max_value=8.5,
                        min_alarm=0.1, max_alarm=8.4,
                        min_warning=0.5, max_warning=8.0,
                        fget="get_current",
                        fset="set_current",
                        doc="the power supply current")


    host = device_property(dtype=str)
    port = device_property(dtype=int, default_value=9788)
    
    def init_device(self):
        Device.init_device(self)
        self.__current = 0.0
        self	.set_state(DevState.STANDBY)
    
    def read_voltage(self):
        self.info_stream("read_voltage(%s, %d)", self.host, self.port)
        return 9.99, time.time(), AttrQuality.ATTR_WARNING
    
    def get_current(self):
        return self.__current

    def set_current(self, current):
        # should set the power supply current
        self.__current = current

    @command
    def TurnOn(self):
        self.set_state(DevState.ON)

    @command
    def TurnOff(self):
        # turn off the actual power supply here
        self.set_state(DevState.OFF)
    
if __name__ == "__main__":
    server_run([PowerSupply])

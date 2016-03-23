import PyTango

power_supply = PyTango.DeviceProxy("test/power_supply/1")
print power_supply.state()
power_supply.TurnOn()
power_supply.current=3
print power_supply.current
print power_supply.voltage
print str(power_supply.status())

import PyTango

dev_info = PyTango.DbDevInfo()
dev_info.server = "PowerSupplyDS/test"
dev_info._class = "PowerSupply"
dev_info.name = "test/power_supply/1"

db = PyTango.Database()
db.add_device(dev_info)

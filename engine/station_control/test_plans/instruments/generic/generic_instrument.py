class Instrument(object):
    # import pyvisa
    def __init__(self, *args, **kwargs):
        self.visa = None
        self.address = None
        self.rm = None
        if "address" in kwargs: self.address = kwargs["address"]
        if "rm" in kwargs: self.rm = kwargs["rm"]
        # print(kwargs)

    def add_address(self, address):
        self.address = address

    def add_resource_manager(self, rm):
        self.rm = rm
    
    def open_resource(self):
        if (self.address != None) | (self.rm != None):
            self.visa = self.rm.open_resource(self.address)

    def idendification_query(self):
        if self.visa != None:
            print(self.visa.query('*IDN?'))
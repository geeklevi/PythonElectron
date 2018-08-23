from .generic_test import GenericTestPlan
from .instruments import Keithley2602B, Agilent86140B
from .tests import liv

class PprTestPlan(GenericTestPlan):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        print("pprtest")
        # print(args)
        # print(kwargs)
        self.smu1 = Keithley2602B()
        self.osa = Agilent86140B()

        if 'smu1' in kwargs:
            self.smu1.add_address(kwargs['smu1'])
        if 'osa' in kwargs: 
            self.osa.add_address(kwargs['osa'])
        if 'rm' in kwargs:
            self.smu1.add_resource_manager(kwargs['rm'])
            self.osa.add_resource_manager(kwargs['rm'])
            # then open the visa in the file
            
            self.smu1.open_resource()
            self.osa.open_resource()
        print(self.smu1.address)
        print(self.osa.address)

        self.liv = liv(self.smu1)
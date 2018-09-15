from .generic_test import GenericTestPlan
from .instruments import Keithley2602B, Agilent86140B
from .tests import liv
import time
class PprTestPlan(GenericTestPlan):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        print("pprtest")
        # print(args)
        # print(kwargs)
        self.smu1 = Keithley2602B()
        self.osa1 = Agilent86140B()

        if 'smu1' in kwargs:
            self.smu1.add_address(kwargs['smu1'])
        if 'osa1' in kwargs: 
            self.osa1.add_address(kwargs['osa1'])
        if 'rm' in kwargs:
            self.smu1.add_resource_manager(kwargs['rm'])
            # self.osa1.add_resource_manager(kwargs['rm'])
            # then open the visa in the file
            
            self.smu1.open_resource()
            # self.osa1.open_resource()
        print(self.smu1.address)
        # print(self.osa1.address)
        self.smu1.initialization()
        self.smu1.idendification_query()
        
        liv_initialization = self.read_txt_to_list("keithley_2602B_liv_test.txt", 'keithley2602b')
        for cmd in liv_initialization:
            # print(cmd)
            self.smu1.visa.write(cmd)
            time.sleep(0.1)
        liv_read_buffer = self.read_txt_to_list("keithley_2602B_liv_read_buffer.txt", 'keithley2602b')
        print(liv_read_buffer[0])
        data = self.smu1.visa.query(liv_read_buffer[0])
        print("woxiangtuichu")
        print(data)
        print(type(data))
        print(kwargs['rm'].session)
        self.liv = liv(self.smu1)

        self.smu1.visa.close()
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
            self.osa1.add_resource_manager(kwargs['rm'])
            # then open the visa in the file
            
            self.smu1.open_resource()
            self.osa1.open_resource()
        print(self.smu1.address)
        print(self.osa1.address)
        self.smu1.initialization()
        self.smu1.idendification_query()
        
        liv_comment_list = self.read_txt_to_list("keithley_2602B_liv_test.txt", 'keithley2602b')
        for cmd in liv_comment_list:
            print(cmd)
            self.smu1.visa.write(cmd)
            time.sleep(0.1)

        self.liv = liv(self.smu1)
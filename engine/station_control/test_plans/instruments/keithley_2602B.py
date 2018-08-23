from .generic import Smu

class Keithley2602B(Smu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    def initialization(self):
        self.reset_channel_a()
        self.reset_channel_b()

    def reset_channel_a(self):
        self.visa.write('''
        smua.reset()
        waitcomplete()
        ''')

    def reset_channel_b(self):
        self.visa.write('''
        smub.reset()
        waitcomplete()
        ''')
    
    def set_channel_a_compliance_v(self):
        self.visa.write('''
        smub.reset()
        waitcomplete()
        ''')
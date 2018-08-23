from .generic import Smu

class Keithley2400(Smu):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    
from .generic_instrument import Instrument

class Osa(Instrument):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print(args)
        # print(kwargs)
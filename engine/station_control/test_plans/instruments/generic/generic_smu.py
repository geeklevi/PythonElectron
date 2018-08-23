from .generic_instrument import Instrument

class Smu(Instrument):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print("'what is this")
        # print(args)
        # print("'what is this")
        # print(kwargs)
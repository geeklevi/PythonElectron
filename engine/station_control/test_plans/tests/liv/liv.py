class liv(object):
    from ...instruments import Keithley2602B, Keithley2400
    def __init__(self, smu):
        print(smu)
        # smu.write()
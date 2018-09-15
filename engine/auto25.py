import visa
import time
import matplotlib.pyplot as plt
import numpy as np
import os, sys, json

from station_control import PprTestPlan
def read_in():
    lines = sys.stdin.readlines()
    # Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])

if __name__ == '__main__':
    # runliv()
    # smu1 = keithley2400({'1':'sdf'})
    # print('yes')

    # print(__file__)
    # dir_name = os.path.dirname(os.path.realpath(__file__))
    # path = os.path.join(dir_name, "scripts", "keithley2400_liv_sweep.txt")
    # l = load_txt(path)
    # print(l)

    # smu1 Channel A is for current input
    # smu1 Channel B is for pd voltage bias and pd current reading
    smu1_address = "GPIB0::26::INSTR"

    # smu2 Channel B is for another current input, share same address with smu1 using node to connect

    # osa address()
    osa1_address = "GPIB0::20::INSTR"

    # data save address
    data_sv_address = r'O:\engineering\TEST\Lihua\2018-07-30 HSTest Data Saving\test_data'

    # resource manager
    rm = visa.ResourceManager()
    print(rm.list_resources())


    try:
        ppr_test = PprTestPlan(smu1 = smu1_address, osa1 = osa1_address, rm = rm)
        # ppr_test = PprTestPlan(rm=rm)
        ppr_test.start(data_sv_address)
    except Exception as e:
        print(e)

    rm.close()
    
    i = 0
    while(True):
        print(i)
        lines = sys.stdin.readlines()
        print(lines)
        sys.stdout.flush()
        time.sleep(1)
        i += 1
        try:
            if lines[0] == "whatdoesfoxsay\n":
                break
        except Exception as e:
            print(e)

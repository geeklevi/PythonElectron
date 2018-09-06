import visa
import time
import matplotlib.pyplot as plt
import numpy as np
# import importlib.util
# spec = importlib.util.spec_from_file_location("module.name", "/path/to/file.py")
# foo = importlib.util.module_from_spec(spec)
# spec.loader.exec_module(foo)
# foo.MyClass()
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,currentdir)
print(currentdir)
print(parentdir)
# if __name__ == '__main__':
#     from O.engineering.TEST.Software.HS.Levi_Hu.MultiProbeTest.PythonElectron.engine.station_control.test_plans import PprTestPlan   # assuming the package is in the current working directory or a subdirectory of PYTHONPATH
# else:
#     from .test_plans import PprTestPlan
# import sys
# import os

# PACKAGE_PARENT = '.'
# SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
# parent_path = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT))
# print(parent_path)
# sys.path.append(parent_path)
try:
    sys.path.remove(currentdir)
except ValueError: # Already removed
    pass
from .test_plans import PprTestPlan


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
    smu1_address = "GPIB0::20::INSTR"

    # smu2 Channel B is for another current input, share same address with smu1 using node to connect

    # osa address()
    osa1_address = "GPIB0::26::INSTR"

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
    
import visa, os
class GenericTestPlan(object):
    def __init__(self, *args, **kwargs):
        # print("testgeneric")
        print("")
    
    def start(self, save_folder):
        self.save_folder = save_folder
        print("Saving data to folder: ")
        print(save_folder)

    def read_txt_to_list(self, file_name, instrument_name=None, folder_path=None):
        # print(__file__)
        # textfile_abs_path = os.path.dirname(os.path.realpath(__file__))
        # print(textfile_abs_path)
        if folder_path == None:
            test_plan_path = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
            folder_path = os.path.join(test_plan_path, 'scripts')
            if instrument_name != None:
                folder_path = os.path.join(folder_path, instrument_name)
        print(folder_path)
        try:
            with open(os.path.join(folder_path, file_name), 'r') as f:
                c = f.readlines()
                c = [l.strip() for l in c]
                print(c)
                return c
        except Exception as e:
            print(e)
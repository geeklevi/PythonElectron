import visa

class GenericTestPlan(object):
    def __init__(self, *args, **kwargs):
        # print("testgeneric")
        print("")
    
    def start(self, save_folder):
        self.save_folder = save_folder
        print("Saving data to folder: ")
        print(save_folder)
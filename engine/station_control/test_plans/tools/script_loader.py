# @staticmethod
def load_txt(path):
    txt_lists = []
    with open(path,'r') as fin:
        for line in fin:
            txt_lists.append(line)
    return txt_lists

# @staticmethod
def edit_txt(path):
     with open(path, "a") as f:
        f.write("new line\n")
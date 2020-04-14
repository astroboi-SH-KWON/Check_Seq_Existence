

class Valid:
    def __init__(self):
        self.tmp = ""

    def is_unique(self, tmp_list):
        flag = True
        for element_str in tmp_list:
            if element_str in tmp_list:
                flag = False
                print("[" + element_str + "] is already in the list")

        if flag:
            print("these elements are unique")

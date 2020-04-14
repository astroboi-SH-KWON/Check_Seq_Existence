

class Logics:
    def __init__(self):
        self.tmp = ""

    def chck_seq_existence(self, pd_trns_01, pd_trns_02, col_target, taget_val, col_both):
        trg_val_dict = {}
        anti_trg_val_dict = {}
        for idx in pd_trns_02.keys():
            if pd_trns_02[idx][col_target] == taget_val:
                # print(pd_trns_02[idx])
                for i in pd_trns_01.keys():
                    if pd_trns_01[i][col_both] == pd_trns_02[idx][col_both]:
                        # print(pd_trns_01[i])
                        trg_val_dict[pd_trns_01[i][col_both]] = [pd_trns_01[i]['Target_region'], pd_trns_01[i]['Reference_sequence'], pd_trns_02[idx]['Total'], pd_trns_02[idx][col_target]]
            else:
                for i in pd_trns_01.keys():
                    if pd_trns_01[i][col_both] == pd_trns_02[idx][col_both]:
                        # print(pd_trns_01[i])
                        anti_trg_val_dict[pd_trns_01[i][col_both]] = [pd_trns_01[i]['Target_region'], pd_trns_01[i]['Reference_sequence'], pd_trns_02[idx]['Total'], pd_trns_02[idx][col_target]]
        return trg_val_dict, anti_trg_val_dict

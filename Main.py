from time import clock

import Utils
import Logics
import Valid
############### start to set env ################
DIR_PATH = "D:/000_WORK/SangYeon/20200310/20200406_Input/"

NEW_BARCODE_REF = "new_barcode_ref.txt"
RESULT_PATH = "Output/terry/meta_human_project/1_S1_L001_R1_001/Result/"
INDEL_RESULT = "1_S1_L001_R1_001_Final_indel_result.tsv"
INDEL_SUMMARY = "1_S1_L001_R1_001_Summary_result.tsv"

EXCEL_PATH01 = "seq_existence"
EXCEL_PATH02 = "anti_seq_existence"
############### end setting env  ################

def main():
    util = Utils.Utils()
    chk_valid = Valid.Valid()
    logic = Logics.Logics()

    barcd_ref_pd = util.get_df_by_sep(DIR_PATH + NEW_BARCODE_REF, "\t")
    summary_pd = util.get_df_by_sep(DIR_PATH + RESULT_PATH + INDEL_SUMMARY, "\t")

    chk_valid.is_unique(barcd_ref_pd['Barcode'])
    chk_valid.is_unique(summary_pd['Barcode'])

    print("find 'IND/TOT' is 0 ")
    trg_val_dict, anti_trg_val_dict = logic.chck_seq_existence(barcd_ref_pd.T, summary_pd.T, 'IND/TOT', 0, 'Barcode')
    util.make_excel(DIR_PATH + EXCEL_PATH01, trg_val_dict)
    util.make_excel(DIR_PATH + EXCEL_PATH02, anti_trg_val_dict)

start_time = clock()
print("start >>>>>>>>>>>>>>>>>>")
main()
print("::::::::::: %.2f seconds ::::::::::::::" % (clock() - start_time))
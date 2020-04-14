from time import clock
import pandas as pd

import Utils
import Logics
import Valid
############### start to set env ################
DIR_PATH = "D:/000_WORK/SangYeon/20200310/20200406_Input/"

NEW_BARCODE_REF = "new_barcode_ref.txt"
RESULT_PATH = "Output/terry/meta_human_project/1_S1_L001_R1_001/Result/"
INDEL_RESULT = "1_S1_L001_R1_001_Final_indel_result.tsv"
INDEL_SUMMARY = "1_S1_L001_R1_001_Summary_result.tsv"


############### end setting env  ################

def test_main1():
    util = Utils.Utils()
    logic = Logics.Logics()
    barcd_ref_list = util.read_file_by_line_to_list(DIR_PATH + NEW_BARCODE_REF)
    result_list = util.read_file_by_line_to_list(DIR_PATH + RESULT_PATH + INDEL_SUMMARY)

    tmp_brcd_list = util.split_by_tab(barcd_ref_list)

    print(barcd_ref_list)
    # print(result_list)



    print(tmp_brcd_list)

def test_main2():
    util = Utils.Utils()
    chk_valid = Valid.Valid()
    logic = Logics.Logics()

    barcd_ref_pd = util.get_df_by_sep(DIR_PATH + NEW_BARCODE_REF, "\t")
    summary_pd = util.get_df_by_sep(DIR_PATH + RESULT_PATH + INDEL_SUMMARY, "\t")

    chk_valid.is_unique(barcd_ref_pd['Barcode'])
    chk_valid.is_unique(summary_pd['Barcode'])
    # print(barcd_ref_pd.T[0])
    # print(result_pd['Barcode'])

    print("find Total is 0 ")
    logic.chck_seq_existence(barcd_ref_pd.T, summary_pd.T, 'IND/TOT', 0, 'Barcode')
    # barcd_ref_pd_trns = barcd_ref_pd.T
    # summary_pd_trns = summary_pd.T
    # for idx in summary_pd_trns.keys():
    #     if summary_pd_trns[idx]['IND/TOT'] == 0:
    #         print(summary_pd_trns[idx])
    #         # print(summary_pd_trns[idx]['Barcode'])
    #         for i in barcd_ref_pd_trns.keys():
    #             if barcd_ref_pd_trns[i]['Barcode'] == summary_pd_trns[idx]['Barcode']:
    #                 print(barcd_ref_pd_trns[i])
    #
    #         print("::::::::::::::::::::::::::::::::::::::::::")





start_time = clock()
print("start >>>>>>>>>>>>>>>>>>")
# test_main1()
test_main2()
print("::::::::::: %.2f seconds ::::::::::::::" % (clock() - start_time))

from numpy import save
import pandas as pd


def read_differences_file() -> dict:
    df = pd.read_csv("original_sources/differences.csv")
    return df.to_dict(orient="records")


def replace_pat_sbs_file():
    diff_dict = read_differences_file()
    
    with open("original_sources/PAT_SBS.txt", "r") as pat_sbs_file:
        pat_sbs_data = pat_sbs_file.read()

    for word in diff_dict:
        pat_sbs_data = pat_sbs_data.replace(word["now"], word["result"])

    with open("curated_sources/PAT_SBS_REPLACED.txt", "w") as pat_sbs_replaced_file:
        pat_sbs_replaced_file.write(pat_sbs_data)


def replace_pat_ods_file():
    diff_dict = read_differences_file()
    df = pd.read_excel("original_sources/Pātimokkha Word by Word.ods", engine="odf")

    for word in diff_dict:
        df = df.replace(to_replace=word["now"], value=word["result"])

    df.to_excel("curated_sources/Pātimokkha Word by Word Replaced.ods")


replace_pat_sbs_file()
replace_pat_ods_file()
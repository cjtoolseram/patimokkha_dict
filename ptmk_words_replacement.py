import pandas as pd
import csv


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


def replace_inflections_file():
    df = pd.read_csv("frequency/all_inflections.csv", sep="\t")
    data = df.to_dict(orient="records")

    csvheader = ["inflection", "headwords"]
    with open("curated_sources/all_inflections_curated.csv", "w") as csvwriter:
        writer = csv.writer(csvwriter, delimiter="\t")
        writer.writerow(csvheader)
        for row in data:
            non_numeric_str = ''.join([i for i in row["headwords"] if not i.isdigit()])
            non_numeric_str = non_numeric_str.replace(" ", "").replace("[", "").replace("]", "").replace("'", "")
            headwords_list = list(non_numeric_str.split(","))
            headwords_list = pd.unique(headwords_list).tolist()
            row["headwords"] = ','.join(map(str, headwords_list))
            csvrow = [row["inflection"], row["headwords"]]
            writer.writerow(csvrow)


replace_pat_sbs_file()
replace_pat_ods_file()
replace_inflections_file()
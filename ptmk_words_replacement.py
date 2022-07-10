import pandas as pd
import csv
import re


def read_differences_file() -> dict:
    df = pd.read_csv("original_sources/differences.csv")
    return df.to_dict(orient="records")

def read_inflections_file() -> dict:
    df = pd.read_csv("curated_sources/all_inflections_modified.csv")
    return df.to_dict(orient="records")


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
    with open("curated_sources/all_inflections_modified.csv", "w") as csvwriter:
        writer = csv.writer(csvwriter, delimiter=",")
        writer.writerow(csvheader)
        for row in data:
            #process inflections
            row["inflection"] = row["inflection"].replace(" ", "")
            #process headwords
            headwords_non_numeric_str = "".join([i for i in row["headwords"] if not i.isdigit()])
            headwords_non_numeric_str = headwords_non_numeric_str.replace(" ", "").replace("[", "").replace("]", "").replace("'", "")
            headwords_list = list(headwords_non_numeric_str.split(","))
            headwords_list = pd.unique(headwords_list).tolist()
            row["headwords"] = " ".join(map(str, headwords_list))
            csvrow = [row["inflection"], row["headwords"]]
            writer.writerow(csvrow)
    replace_pat_sbs_file()
    replace_pat_ods_file()


def replace_pat_sbs_file():
    diff_dict = read_differences_file()
    inflections_dict = read_inflections_file()
    
    with open("original_sources/PAT_SBS.txt", "r") as pat_sbs_file:
        pat_sbs_data = pat_sbs_file.read()

    for word in diff_dict:
        pat_sbs_data = pat_sbs_data.replace(word["now"], word["result"])

    pat_sbs_data = pat_sbs_data.replace("\n\n", " \n\n ").replace(".", " . ").replace(":", " : ")
    pat_sbs_data = pat_sbs_data.replace("?", " ? ").replace(",", " , ").replace("'", " ' ").replace("`", " ` ")
    pat_sbs_data_list = list(pat_sbs_data.split(" "))

    for inflection_words in inflections_dict:
        for pat_sbs_data_word in pat_sbs_data_list:
            if inflection_words["inflection"] == pat_sbs_data_word.lower():
                index = pat_sbs_data_list.index(pat_sbs_data_word)
                pat_sbs_data_list[index] = inflection_words["headwords"]
                print(f"{pat_sbs_data_word} -> {pat_sbs_data_list[index]} REPLACED!")

    pat_sbs_data = " ".join(pat_sbs_data_list)
    pat_sbs_data = pat_sbs_data.replace(" \n\n ", "\n\n").replace(" . ", ".").replace(" : ", ":")
    pat_sbs_data = pat_sbs_data.replace(" ? ", "?").replace(" , ", ",").replace(" ' ", "'").replace(" ` ", "`")

    with open("curated_sources/PAT_SBS_REPLACED.txt", "w") as pat_sbs_replaced_file:
        pat_sbs_replaced_file.write(pat_sbs_data)


replace_inflections_file()

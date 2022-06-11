import pandas as pd
import json

df = pd.read_excel("Pātimokkha Word by Word.ods", engine="odf")
sentences_file = open("ptmk_sentences.txt", "w")

sentence_json = (df[["sentence"]].ffill().drop_duplicates()).to_json(force_ascii=False, orient='records', indent=2)
sentence_json = json.loads(sentence_json)

for stc in sentence_json:
    sentences_file.write(stc["sentence"] + "\n")

sentences_file.close()
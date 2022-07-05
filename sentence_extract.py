import pandas as pd
import json

MAIN_DIR="Bhikkhu Patimokkha"
DB_DIR=MAIN_DIR + "/json"

sentences_file = open("curated_sources/ptmk_sentences.txt", "w")

json_file = open(DB_DIR + "/sources.json")
sources_json = json.load(json_file)

for source_file in sources_json:
    sentences_file.write(source_file["abbrev"]+ "\t" + source_file["source"] + "\n")

    source_df = pd.read_json(DB_DIR + "/" + source_file["source"] + ".json")
    line_df = source_df[source_file["source"] == source_df["source"]]
    line_json = (line_df[["sentence"]].drop_duplicates().ffill()).to_json(force_ascii=False, orient='records', indent=2)
    line_json = json.loads(line_json)
    
    for ln in line_json:
        sentences_file.write(ln["sentence"] + "\n") 
    sentences_file.write("\n\n") 

sentences_file.close()
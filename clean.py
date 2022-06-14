import pandas as pd
import re

def clean_machine(text):
	text = text.lower()
	text = re.sub("\d", "", text)
	text = re.sub("\.", "\n", text)
	text = re.sub(" ", "\n", text)
	text = re.sub("/", "", text)
	text = re.sub("\:", "", text)
	text = re.sub("\;", "", text)
	text = re.sub(",", " ", text)
	text = re.sub("‘", "", text)
	text = re.sub("'", "", text)
	text = re.sub(";", "", text)
	text = re.sub("’", "", text)
	text = re.sub("“", "", text)
	text = re.sub("”", "", text)
	text = re.sub(" ̓ ", " ", text)
	text = re.sub("\’", "", text)
	text = re.sub("\"", "", text)
	text = re.sub("!", "", text)
	text = re.sub("\?", "", text)
	text = re.sub("\+", "", text)
	text = re.sub("=", "", text)
	text = re.sub("﻿", "", text)
	text = re.sub("§", " ", text)
	text = re.sub("\(", "", text)
	text = re.sub("\)", "", text)
	text = re.sub("-", "", text)
	text = re.sub("–", "", text)	
	text = re.sub("\—", " ", text)	
	text = re.sub("\t", " ", text)
	text = re.sub("…", " ", text)
	text = re.sub("–", "", text)
	text = re.sub("\n", " \n ", text)
	text = re.sub("  ", " ", text)
	text = re.sub("^ ", "", text)
	text = re.sub("^ ", "", text)
	text = re.sub("^ ", "", text)
	text = re.sub("\[", "", text)
	text = re.sub("\]", "", text)
	text = re.sub("ṁ", "ṃ", text)

	return text

with open(f"patimokkhaSBS.txt", 'r') as input_file :
	text = input_file.read()
	
clean_text = clean_machine(text)

with open(f"clean_patimokka.txt", 'w') as save_file :
	save_file.write(clean_text)

input_file.close()
save_file.close()

with open(f"ptmk_sentences.txt", 'r') as ptmk_ods :
	ptmk_ods_text = ptmk_ods.read()
	
ptmk_ods_text_clean = clean_machine(ptmk_ods_text)

with open(f"clean_patimokka_ods.txt", 'w') as ptmk_ods_save :
	ptmk_ods_save.write(ptmk_ods_text_clean)

ptmk_ods.close()
ptmk_ods_save.close()
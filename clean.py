import pandas as pd
import re

def clean_machine(text):
	text = text.lower()
	# text = re.sub("\d", "", text)
	# text = re.sub("( ti )", "(ti )", text)
	# text = re.sub("( ti,)", "(ti,)", text)
	# text = re.sub("( ti.)", "(ti.)", text)
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
	text = re.sub("`", "", text)
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
	# text = re.sub("\t", " ", text)
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

with open(f"source/PAT_Dhammayuttika.txt", 'r') as input_file :
	text = input_file.read()
	
clean_text = clean_machine(text)

with open(f"output/clean_Dhammayuttika.txt", 'w') as save_file :
	save_file.write(clean_text)

input_file.close()
save_file.close()

with open(f"source/PAT_Dvemātikāpāḷi.txt", 'r') as ptmk_ods :
	ptmk_ods_text = ptmk_ods.read()
	
ptmk_ods_text_clean = clean_machine(ptmk_ods_text)

with open(f"output/clean_Dvemātikāpāḷi.txt", 'w') as ptmk_ods_save :
	ptmk_ods_save.write(ptmk_ods_text_clean)

ptmk_ods.close()
ptmk_ods_save.close()

with open(f"source/PAT_Nyanatusita.txt", 'r') as ptmk_THAI :
	ptmk_THAI_text = ptmk_THAI.read()
	
ptmk_THAI_text_clean = clean_machine(ptmk_THAI_text)

with open(f"output/clean_Nyanatusita.txt", 'w') as ptmk_THAI_save :
	ptmk_THAI_save.write(ptmk_THAI_text_clean)

ptmk_THAI.close()
ptmk_THAI_save.close()

with open(f"source/PAT_Yogashrama.txt", 'r') as ptmk_Nyanatusita :
	ptmk_Nyanatusita_text = ptmk_Nyanatusita.read()
	
ptmk_Nyanatusita_text_clean = clean_machine(ptmk_Nyanatusita_text)

with open(f"output/clean_Yogashrama.txt", 'w') as ptmk_Nyanatusita_save :
	ptmk_Nyanatusita_save.write(ptmk_Nyanatusita_text_clean)

ptmk_Nyanatusita.close()
ptmk_Nyanatusita_save.close()

with open(f"ptmk_sentences.txt", 'r') as ptmk_sentences :
	ptmk_sentences_text = ptmk_sentences.read()
	
ptmk_sentences_text_clean = clean_machine(ptmk_sentences_text)

with open(f"output/clean_sentences.txt", 'w') as ptmk_sentences_save :
	ptmk_sentences_save.write(ptmk_sentences_text_clean)

ptmk_sentences.close()
ptmk_sentences_save.close()

with open(f"source/PAT_Mahāsaṅgīti.txt", 'r') as maha_sentences :
	maha_sentences_text = maha_sentences.read()
	
maha_sentences_text_clean = clean_machine(maha_sentences_text)

with open(f"output/clean_Mahāsaṅgīti.txt", 'w') as maha_sentences_save :
	maha_sentences_save.write(maha_sentences_text_clean)

maha_sentences.close()
maha_sentences_save.close()
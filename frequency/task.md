 **calculation of frequency of words in pātimokkha**

Input:
1. PAT_SBS_REPLACED.txt - pātimokkha with corrections
2. "all_inflections.csv" - table of declinations.

All pāli words have declinations - words have different form in different gender and cases - example: word "buddha" have different forms: "buddhassa" buddhena" "buddhaṃ" and so on. For this example see file "considering declination.jpg"
When we will count frequency of words we need to consider declination tables.

Steps:

 - 1.1. "all_inflections.csv" need some modification

- 1.1.1. in the second column we get rid of all numbers and duplicate (in one cell). But keep unique words.

see examples in example.xlsx (see sheets before and after)

- 1.1.2. save all_inflections_modified.csv

- 1.2. replace all words in "PAT_SBS_REPLACED.txt" according to all_inflections_modified.csv and save it as  PAT_SBS_modified.txt
but we need to replace only individual words - words inside compounds no need to replace:
example: "buddhassa saṇgho" will become "buddha saṇgha"; but buddhassasaṇgha will remine the same.

- 2. calculate the frequency, using code 

https://github.com/bdhrs/frequency-maps/blob/main/corpus%20counter.py

just this code as an input have a folder with many txt. In our case we need to reduce it up to one file input - PAT_SBS_modified.txt
output = PAT_friquency.txt

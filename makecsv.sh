echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "making csv with bold"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

#cd "/home/deva/Documents/sasanarakkha/patimokkha-analysis/original_sources"

# python3 ods_to_csv.py "Pātimokkha Word by Word.ods" Sheet1 20

# mv "original_sources/Pātimokkha Word by Word.ods" "Pātimokkha Word by Word.ods"

python3 ods-to-csv-headers.py "original_sources/Pātimokkha Word by Word.ods" Sheet1 20

# mv "Pātimokkha Word by Word.ods" "original_sources/Pātimokkha Word by Word.ods"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "filtering words that have been done"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

python3 "patimokkha filter.py"

echo "process completed"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
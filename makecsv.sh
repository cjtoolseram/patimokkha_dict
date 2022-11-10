echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "moving Patimokkha ods from Downloads"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

mv "/home/deva/Downloads/Pātimokkha Word by Word.ods" "/home/deva/Documents/dps/patimokkha_dict/original_sources/Pātimokkha Word by Word.ods"

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "making Patimokkha csv with bold - ods-to-csv-headers.py"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

python3 ods-to-csv-headers.py "original_sources/Pātimokkha Word by Word.ods" Sheet1 20

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "filtering words that have been done"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

python3 "patimokkha filter.py"

echo "process completed"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
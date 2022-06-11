import pandas as pd
import json, os

MAIN_DIR="Bhikkhu Patimokkha"
DB_DIR=MAIN_DIR + "/json"

## Read ods files and generate DF
df = pd.read_excel("Pātimokkha Word by Word.ods", engine="odf")

#Create main dir 
os.makedirs(MAIN_DIR, exist_ok=True)

#Create DB folder for json
os.makedirs(DB_DIR, exist_ok=True)

#store sources db as json format in "Bhikkhu Patimokkha/json"
sources_json = (df[["source", "abbrev"]].ffill().drop_duplicates()).to_json(DB_DIR + "/sources.json", force_ascii=False, orient='records', indent=2)
json_file = open(DB_DIR + "/sources.json")
sources_json = json.load(json_file)

for sj in sources_json:
    os.makedirs(MAIN_DIR + "/" + sj["source"], exist_ok=True)
    result_df = df[df["source"] == sj["source"]]
    filtered_result_df = result_df[["abbrev", "source", "sentence", "bhikkhupātimokkhapāḷi", "pos", "grammar", "+case", "meaning", 
        "lit. meaning", "root", "base", "construction", "compound type", "compound construction"]].fillna("")
    filtered_result_df.to_json(DB_DIR + "/" + sj["source"] + ".json", force_ascii=False, orient='records', indent=2)

## Create a content table
content_table = open(MAIN_DIR + "/main.html", "w")
content_table.write("<!DOCTYPE html>\n")
content_table.write("<html>\n")
content_table.write("<head><link rel=\"stylesheet\" href=\"scripts/main.css\"></head>\n")
content_table.write("<body>\n")

content_table.write("<div class=\"topnav\">\n")
content_table.write("<a class=\"active\" href=\"main.html\">[SBS] Bhikkhu Patimokkha</a>\n")
content_table.write("</div>\n")

for sj in sources_json:
    content_table.write("<h3><a href=\"./" + sj["source"] + "/" + sj["source"] + ".html" + "\">" + sj["abbrev"] + " " + sj["source"] + "</a></h3>\n")

content_table.write("</body>\n")
content_table.write("</html>\n") 
content_table.close()

## READ FILE FROM JSON AND BUILD SENTENCE PAGE BY REMOVING DUPLICATES FROM JSON
for source_file in sources_json:
    file = open(MAIN_DIR + "/" + source_file["source"]+ "/" + source_file["source"]+ ".html", "w")
    file.write("<!DOCTYPE html>\n")
    file.write("<html>\n")
    file.write("<head>\n")
    file.write("<link rel=\"stylesheet\" href=\"../scripts/main.css\">\n")
    file.write("</head>\n")
    file.write("<body>\n")
    file.write("<button onclick=\"topFunction()\" id=\"topBtn\" title=\"Go to top\">Top</button>\n")
    file.write("<div class=\"topnav\">\n")
    file.write("<a class=\"active\" href=\"../main.html\">Home</a>\n")
    file.write("<a href=\"#" + source_file["source"] + "\"><b>[" + source_file["abbrev"] + "] " + source_file["source"] + "</b></a>\n")
    file.write("</div>\n")

    file.write("<h1>" + source_file["abbrev"]+ "\t" + source_file["source"] + "</h1>\n")
    
    ## Print sentences for each source & definition from each line
    source_df = pd.read_json(DB_DIR + "/" + source_file["source"] + ".json")
    line_df = source_df[source_file["source"] == source_df["source"]]
    line_json = (line_df[["sentence"]].drop_duplicates().ffill()).to_json(force_ascii=False, orient='records', indent=2)
    line_json = json.loads(line_json)
    
    file.write("<div class=\"sentence\">")
    for ln in line_json:
        if ln["sentence"] != "":
            file.write("<a href=\"#" + ln["sentence"].replace(" ", "_") + "\">" + ln["sentence"] + "</a><br>\n") 
    file.write("</div>")
    file.write("<br><br><hr>\n")

    for ln in line_json:
        if ln["sentence"] != "":
            file.write("<b style=\"font-size:20px\" id=\"" + ln["sentence"].replace(" ", "_") + "\">" + ln["sentence"] + "</b><br>\n")
            define_df = (line_df[line_df["sentence"] == ln["sentence"]])[["bhikkhupātimokkhapāḷi", "pos", "grammar", "+case", "meaning", 
        "lit. meaning", "root", "base", "construction", "compound type", "compound construction"]].fillna("")
            definition_table = define_df.to_html(justify='left', index=False).replace("0", "")
            definition_table = definition_table.replace("bhikkhupātimokkhapāḷi", "pāḷi")
            file.write(definition_table)
            file.write("<br><br>\n")

    file.write("<script src=\"../scripts/main.js\"></script>\n") 
    file.write("</body>\n")
    file.write("</html>\n") 
    file.close()
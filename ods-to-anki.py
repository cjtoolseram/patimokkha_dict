import zipfile
from bs4 import BeautifulSoup
import pandas as pd
from timeis import timeis, green, yellow, line, white, tic, toc


class ReadOds:

    def __init__(self, filename, sheets_name):
        print(f"{timeis()} {green}opening ods")
        # get content xml data from OpenDocument file
        ziparchive = zipfile.ZipFile(filename, "r")
        xmldata = ziparchive.read("content.xml")
        ziparchive.close()
        

        #find bold styles
        self.soup = BeautifulSoup(xmldata, 'xml')
        self.sheets_name = sheets_name
        self.df = {}
        self.bold_names = self.get_bold_styles()
        
        if isinstance(sheets_name, str):
            self.sheets_name = [sheets_name]
            
        for sheet_name in sheets_name:
            sheet_rows = self.get_rows_in_sheet(sheet_name)
            header = self.get_columns_in_row(sheet_rows[0])
            # header = [it for it in header if it]
            
            n_row = len(header)
            data = [dict(zip(header, (self.get_columns_in_row(row)[:n_row]))) for row in sheet_rows[1:]]
        
            self.df[sheet_name] = pd.DataFrame(data)
        

    def process_and_save_csv(self):
        print(f"{timeis()} {green}processing for anki")
            
        test1 = self.df['analysis']['#'] == "1"
        test2 = self.df['analysis']['meaning'] != ""
        filter = test1 & test2
        self.df['analysis'] = self.df['analysis'][filter]
        self.df['analysis'].drop(["#", "x", "comments"], axis = 1, inplace=True)
        self.df['analysis'].drop(self.df['analysis'].iloc[:, 20:], axis = 1, inplace=True)
        self.df['analysis']['GoogleForm'] = f"""Spot a mistake? <a class="link" href="https://docs.google.com/forms/d/e/1FAIpQLSdG6zKDtlwibtrX-cbKVn4WmIs8miH4VnuJvb7f94plCDKJyA/viewform?usp=pp_url&entry.438735500=""" + self.df['analysis'].pali + """&entry.1433863141=Anki">Fix it here</a>."""

        rows = self.df['analysis'].shape[0]
        columns = self.df['analysis'].shape[1]
        self.df['analysis'].to_csv(f'Pātimokkha Word by Word.csv', sep='\t', index=False, header=True, quoting=1)
        print(f"{timeis()} {green}saving {white}{rows} {green}rows {white}{columns} {green}columns")
        # print(self.df['analysis'])

    def get_bold_styles(self):
        ''' 
        in xml has office:automatic-styles to configure automatic styles for document
        each style name is under style:style > style:text-properties [@fo:font-weight="bold"]
        '''
        all_auto_styles = self.soup.find_all('office:automatic-styles')
        all_text_properties = all_auto_styles[0].find_all('style:text-properties')
        all_bolds = [item for item in all_text_properties if item.has_attr('fo:font-weight') and item['fo:font-weight'] == 'bold']
        bold_names = [item.parent['style:name'] for item in all_bolds]
        return bold_names

    def get_rows_in_sheet(self, sheet_name):
        print(f"{timeis()} {green}processing cell data")
        current_sheet = self.soup.find('table:table', {'table:name':sheet_name})
        if current_sheet == None:
            print('could not find sheet', sheet_name)
            return None
        rows = current_sheet.find_all('table:table-row')
        #ignore first row
        return rows[:]


    def get_columns_in_row(self, row):
        ret_cells = []
        cells = row.find_all('table:table-cell')
        for cell in cells:
            cell_value = self.process_text(cell)

            if cell.has_attr('table:number-columns-repeated'):
                num_repeate = 0
                try:
                    num_repeate = int(cell['table:number-columns-repeated'])
                except ValueError:
                    print('failed to parse repeated cell under', cell)
                for _ in range(num_repeate - 1):
                    ret_cells.append(cell_value)
            ret_cells.append(cell_value)
        return ret_cells


    def process_text(self, cell):
        '''tex process for each column go here'''

        p_texts = cell.find_all('text:p')
        if p_texts == None:
            return ''

        ret_str = ''
        for p_text in p_texts:
            styled_texts = p_text.find_all('text:span')
            for styled_text in styled_texts:

                #find bold styles and replace with b tag
                if styled_text.has_attr('text:style-name'):
                    if styled_text['text:style-name'] in self.bold_names:
                        new_b_tag = self.soup.new_tag('b')
                        new_b_tag.string = styled_text.string
                        styled_text.replace_with(new_b_tag)
                    else:
                        styled_text.replace_with(styled_text.string)
                else:
                    styled_text.replace_with(styled_text.string)

            #implement for <text:s text:c="5"> //5 spaces
            styled_texts = p_text.find_all('text:s')
            for styled_text in styled_texts:
                if styled_text.has_attr('text:c'):
                    styled_text.replace_with(' '*int(styled_text['text:c']))
                else:
                    styled_text.replace_with(' ')

            #convert tags to text
            ret_str += ''.join([str(it) for it in p_text.contents]) + '<br/>'

        return ret_str.removesuffix('<br/>')

    
if __name__ == '__main__':
    tic()
    print(f"{timeis()} {line}")
    print(f"{timeis()} {yellow}converting ods to csv")
    print(f"{timeis()} {line}")
    a = ReadOds("original_sources/Pātimokkha Word by Word.ods", ['analysis'])
    a.process_and_save_csv()
    toc()



    




    
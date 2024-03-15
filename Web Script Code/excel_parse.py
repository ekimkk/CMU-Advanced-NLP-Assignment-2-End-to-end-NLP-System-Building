import pandas as pd
import os

def excel_to_text(input_excel_path, output_txt_path, separator='\t'):
    xls = pd.ExcelFile(input_excel_path)
    
    # Iterate through each sheet in the Excel file
    with open(output_txt_path, 'w', encoding='utf-8') as output_file:
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(input_excel_path, sheet_name=sheet_name)
            output_file.write(f"Sheet: {sheet_name}\n")
            df.to_csv(output_file, sep=separator, index=False)
            output_file.write('\n' + '-'*40 + '\n\n')

def convert_multiple_excels_to_txt(excel_folder, output_folder, separator='\t'):
    for excel_file in os.listdir(excel_folder):
        if excel_file.endswith('.xlsx'):
            excel_path = os.path.join(excel_folder, excel_file)
            output_path = os.path.join(output_folder, excel_file.replace('.xlsx', '.txt'))
            excel_to_text(excel_path, output_path, separator)

# Convert all Excel files in the 'excels' folder to text
convert_multiple_excels_to_txt('excel_data', 'txt_data')
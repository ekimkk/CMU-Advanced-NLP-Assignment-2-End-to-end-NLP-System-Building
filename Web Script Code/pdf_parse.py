from pypdf import PdfReader
import os

def pdf_to_text(input_pdf_path, output_txt_path):
    try:
        reader = PdfReader(input_pdf_path)
        # Open the output text file
        with open(output_txt_path, 'w', encoding='utf-8') as output_file:
            for page in reader.pages:
                text = page.extract_text()
                # Write the text to the output file
                if text:
                    output_file.write(text.encode('utf-8', 'ignore').decode('utf-8'))
                    output_file.write('\n\n')
    except Exception as e:
        print(f"An error occurred with {input_pdf_path}: {e}. Skipping file.")

def convert_multiple_pdfs(pdf_folder, output_folder):
    for pdf_file in os.listdir(pdf_folder):
        if pdf_file.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, pdf_file)
            output_path = os.path.join(output_folder, pdf_file.replace('.pdf', '.txt'))
            pdf_to_text(pdf_path, output_path)

# Convert all PDFs in the 'pdfs' folder to text
convert_multiple_pdfs('pdf_data', 'txt_data')
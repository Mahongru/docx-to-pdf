import os
from docx2pdf import convert

# specify the file path for the input and output files
input_folder = "docs/word/"
output_folder = "docs/pdf/"

# loop through all the files in the input folder
for input_file in os.listdir(input_folder):
    if input_file.endswith(".docx"):
        # generate the input and output file paths
        input_file_path = os.path.join(input_folder, input_file)
        output_file = os.path.splitext(input_file)[0] + ".pdf"
        output_file_path = os.path.join(output_folder, output_file)

        # convert the file to PDF
        convert(input_file_path, output_file_path)
from nicegui import ui, run, app
import os
import glob
from contract_to_txt import convert_to_txt
from flag_FAR_clauses import annotate_contract

FAR_CLAUSE_MATRIX_PATH = "supplementary_files\\2023-03-20_FAR Matrix.xls"

@ui.page("/")
def index():
    # link to stylesheet
    ui.add_head_html("<link rel='stylesheet' href='/static/style.css'/>")

    ui.upload(multiple=True, label="Upload Contracts", auto_upload=True, on_upload=handle_upload).props(add="accept='.docx,.pdf'")


def handle_upload(e):
    name = e.name
    binary = e.content.read()
    upload_filepath = write_binary_to_temp_file(name, binary)
    output_filepath = f"temp/{getFilenameStringNoExtension(name)}_scanned.docx"
    annotate_contract(FAR_CLAUSE_MATRIX_PATH, upload_filepath, output_filepath)
    ui.download(output_filepath)

def getFilenameStringNoExtension(filename):
    temp_list = filename.split(".")
    if (len(temp_list) == 1):
        return temp_list[0]
    else:
        temp_list.pop()
        return '.'.join(temp_list)

def write_binary_to_temp_file(name, binary):
    filepath = f"temp/{name}"
    with open(file=filepath, mode="wb") as file:
        file.write(binary)
    return filepath


def clear_temp_files():
    files = glob.glob('temp/*')
    for f in files:
        os.remove(f)


clear_temp_files()
app.add_static_files("/static", "static")
app.add_static_files("/temp", "temp")
ui.run()
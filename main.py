from nicegui import ui, run
import os
import glob
from contract_to_txt import convert_to_txt
from flag_FAR_clauses import annotate_contract

FAR_CLAUSE_MATRIX_PATH = ""

@ui.page("/")
def index():
    ui.upload(multiple=True, label="Upload Contracts", auto_upload=True, on_upload=handle_upload).props(add="accept='.docx,.pdf'")


def handle_upload(e):
    name = e.name
    binary = e.content.read()
    write_binary_to_temp_file(name, binary)
    

def write_binary_to_temp_file(name, binary):
    with open(file=f"temp/{name}", mode="wb") as file:
        file.write(binary)


def clear_temp_files():
    files = glob.glob('temp/*')
    for f in files:
        os.remove(f)


clear_temp_files()
ui.run()
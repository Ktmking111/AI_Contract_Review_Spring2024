import os
import subprocess
from pathlib import Path
import nicegui

"""
This file can be used to create an executable version of the code by just running 

py build.py

Along with the executable there will need to be the following folders in the same directory as the executable:

static										- automatically stores the css file for nicegui
supplementary_files					- the intended location for the nltk_data folder and any matrices needed, you will need to provide these
temp										- automatically stores a temporary copy of any uploaded documents

"""

cmd = [
    'python',
    '-m', 'PyInstaller',
    'main.py',
    '--name', 'AI_Contract_Scanner',
    '--onefile',
    #'--windowed', # prevents console from appearing
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui'
]
subprocess.call(cmd)

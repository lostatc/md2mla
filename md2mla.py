#!/usr/bin/env python3
import sys
import os
import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import List

# The path of the MLA LaTeX template.
SOURCE_DIR = Path(os.path.realpath(__file__)).resolve().parent
MLA_TEMPLATE = SOURCE_DIR / "mla-template.tex"


def chain_processes(process_args: List[List[str]]):
    """Run a process for each given argument list and raise if one fails."""
    for args_list in process_args:
        process = subprocess.Popen(args_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in iter(process.stdout.readline, ""):
            print(line)
        if process.wait() != 0:
            raise subprocess.CalledProcessError()


with TemporaryDirectory() as temp_directory:
    for input_path in sys.argv[1:]:
        input_file = Path(input_path).resolve()
        output_file = input_file.with_suffix(".pdf")
        tex_file = Path(temp_directory) / input_file.with_suffix(".tex").name
        pdf_file = Path(temp_directory) / output_file.name

        chain_processes([
            ["pandoc", input_file, "-o", tex_file, "--biblatex", "--template", MLA_TEMPLATE],
            ["latexmk", f"-outdir={temp_directory}", "-pdf", tex_file],
        ])

        pdf_file.replace(output_file)

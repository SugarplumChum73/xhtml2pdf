#!/usr/bin/python3
import sys
import atheris

with atheris.instrument_imports():
    from xhtml2pdf import pisa

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    
    str_len = fdp.ConsumeIntInRange(0, 100)
    source_html = fdp.ConsumeUnicodeNoSurrogates(str_len)

    pisa.CreatePDF(source_html)

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()

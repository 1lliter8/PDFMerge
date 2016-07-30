from PyPDF2 import PdfFileMerger, PdfFileReader
import sys

files = [i for i in sys.argv[2:]]
name = str(sys.argv[1]) + ".pdf"
merger = PdfFileMerger()

for filename in files:
	x = PdfFileReader(file(filename, 'rb'))
	merger.append(x)

merger.write(name)
import PyPDF2
import pyttsx3

pdfdocument = input("Please enter the full path of the PDF document that you would like to be read out aloud: ")
book = open(pdfdocument,'rb')
pdf_reader = PyPDF2.PdfReader(book)
num_pages = len(pdf_reader.pages)

play = pyttsx3.init()
print('Reading the PDF File aloud: ')

for num in range(0, num_pages):
	page = pdf_reader.pages[num]
	data = page.extract_text()

	play.say(data)
	play.runAndWait()

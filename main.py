
#page starts from 0 not 1,here for example i had used, the index no. 24,it will read the page 25!
#it neglectys brackets,<,> sign and spaces and also neglects dots

# importing the modules
import PyPDF2
import pyttsx3


# path of the PDF file
path = open('100.pdf', 'rb')

# creating a PdfFileReader object
pdfReader = PyPDF2.PdfFileReader(path)

# the page with which you want to start
# this will read the page of 25th page.
from_page = pdfReader.getPage(24)

# extracting the text from the PDF
text = from_page.extractText()



engine = pyttsx3.init()
#decreasing and reading the text
engine.setProperty("rate", 132)
engine.say(text)
engine.runAndWait()

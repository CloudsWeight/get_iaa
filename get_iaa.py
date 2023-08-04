from PyPDF2 import PdfReader
import requests
url = 'https://www.cia.gov/readingroom/docs/DOC_0001247372.pdf'
r = requests.get(url)
chunk_size = 2000

def get_url(url = 'https://www.cia.gov/readingroom/docs/DOC_0001247372.pdf'):
    url = url
    r = requests.get(url)
    with open('test.pdf', 'wb') as fd:
        for chunk in r.iter_content(chunk_size):
            fd.write(chunk)
    fd.close()
    return 'test.pdf'

def read_pdf(pdf):
    pdf = pdf
    reader = PdfReader(pdf)
    length = (len(reader.pages))
    i = 0
    while i < length:
        file = f"page{i}.txt"
        page  = reader.pages[i]
        text = page.extract_text()
        with open (file, 'w') as fd:
            fd.write(text)
        i +=1



if __name__ == '__main__':
   # pdf = get_url()
    read_pdf('Prelimary-Assessment-UAP-20210625.pdf')

    
 

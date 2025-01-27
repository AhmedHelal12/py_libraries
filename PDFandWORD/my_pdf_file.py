from PyPDF2 import PdfReader,PdfWriter

####### Reading ##########3
reader = PdfReader("academy_3.pdf")
for page in reader.pages:
    print(page.extract_text())

print(reader.metadata)
print(f"Number of pages: {len(reader.pages)}")


######## Writing (Mergin) ##########

writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

with open("x.pdf",'wb') as f:
    writer.write(f)

###### Splitting PDF ############

writer = PdfWriter()
for page in reader.pages[0:2]:
    writer.add_page(page)

with open("splitted_pdf.pdf",'wb') as f:
    writer.write(f)
    
writer = PdfWriter()

#####  Rotating pdf #######
for page in reader.pages:
    page.rotate(90)  # Rotate 90 degrees clockwise
    writer.add_page(page)

with open("rotated.pdf", "wb") as f:
    writer.write(f)

###### Encrypting #####
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)

writer.encrypt("mypassword")

with open("encrypted.pdf", "wb") as f:
    writer.write(f)

###### Decrypting ######

reader = PdfReader("encrypted.pdf")
reader.decrypt("mypassword")

for page in reader.pages:
    print(page.extract_text())
import pytesseract
img = Image.open('text1.png')

# describes image format in the output
print(img)
# path where the tesseract module is installed
pytesseract.pytesseract.tesseract_cmd ='
# converts the image to result and saves it into result variable 

result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
with open('abc.txt',mode ='w') as file

                 file.write(result)

                 print(result)

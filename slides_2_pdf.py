import streamlit as st
import PyPDF2 
import io
import os

def fun(pdfFileObj,v,path_name):

# creating a pdf file object 
    try:
        #pdfFileObj = open(path, 'rb') 

  
# creating a pdf reader object 

        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
  
# printing number of pages in pdf file 

        #print(pdfReader)

        P=[]
        P2=[]
        l=pdfReader.numPages-1
        for i in range(l):
            pageObj = pdfReader.getPage(i)
  
     # extracting text from page 

            Text=pageObj.extractText()
            a=Text.split()[0:v]
            pageObj = pdfReader.getPage(i+1)

  
     # extracting text from page 

            Text2=pageObj.extractText()
            b=Text2.split()[0:v]
            P.append(a==b)
            if P[-1]==False :
                P2.append(i)
            #print(a==b) 
        from PyPDF2 import PdfWriter, PdfReader
        pages_to_keep = P2 # page numbering starts from 0
        infile = PdfReader(pdfFileObj) 
        output = PdfWriter()

        for i in pages_to_keep:
            p = infile.pages[i] 
            output.add_page(p)
        output.add_page(infile.pages[l])

        with open(path_name+'_new.pdf', 'wb') as f:
            output.write(f)
        return("done")
    except ValueError:
      print("Oops!  That was no valid number.  Try again...")





uploaded_files = st.file_uploader("upload pdf file",type=['pdf'],help="Charger une image au format jpg,jpeg,png", accept_multiple_files=True)

for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     name=uploaded_file.name
     #pdfFileObj = open(io.BytesIO(bytes_data))
     fun(io.BytesIO(bytes_data),5,name)
     with open(name.split(".")[0]+'_new.pdf', "rb") as fp:
        btn = st.download_button(
            label="Download PDF",
            data=fp,
            file_name=name+'_new.pdf'
            )
     os.remove(name+'_new.pdf')
    
     

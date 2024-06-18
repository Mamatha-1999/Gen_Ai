import streamlit as st
from PyPDF2 import PdfReader

def extrect_text_from_pdf(pdf_file):
    #open the uploaded pdf file
    pdf_reader = PdfReader(pdf_file)
    text=""

    #iterate through each page and extract text
    for page_num in range(len(pdf_reader.pages)):
        page=pdf_reader.pages[page_num]
        text += page.extract_text() + "\n"
    return text

def save_text_to_file(text, filename):
    with open(filename, 'w')as f:
        f.write(str(text))


        #streamlit app layout
st.title("pdf uploader and viewer")

uploaded_file=st.file_uploader("upload a pdf file", type=["pdf"])

if uploaded_file is not None:
    #extract the text from the uploaded pdf
    pdf_text=extrect_text_from_pdf(uploaded_file)


    #display the extracted text
    st.subheader("extracted text")
    st.text_area("pdf contents", pdf_text, height=300)

    #provide option to save the text to file
    if st.button("save as a text file"):
        save_text_to_file(pdf_text, "extracted_text.txt")
        st.success("text file saved successfully!")

# Load document from Text File

from langchain_community.document_loaders.directory import DirectoryLoader
from langchain_community.document_loaders.text import TextLoader  
from langchain_community.document_loaders.pdf import PyPDFLoader   

# Load the text file from the given directory
text_loader = DirectoryLoader(".", glob="*.txt", loader_cls=TextLoader)   

# Load the PDF file from the given directory
pdf_loader = DirectoryLoader(".", glob="*.pdf", loader_cls=PyPDFLoader)  

# Load the text documents
text_docs = text_loader.load()
print("Loaded Text Documents", len(text_docs))

# Load the PDF documents
pdf_docs = pdf_loader.load()
print("Loaded Text Documents", len(pdf_docs))

all_docs = text_docs + pdf_docs 

print('All Docs count : ', len(all_docs))

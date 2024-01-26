### Project Documentation: PDF and Web Data Scraping for Machine Learning (Research Paper Reference Extractor)

#### Purpose:
The purpose of this project is to automate the extraction of references from research papers, utilizing PDF file parsing and web scraping techniques via APIs. The goal is to enhance the accessibility of information within research papers by retrieving additional details about the listed references.

#### Description:
Research papers often include references that provide valuable information about the paper's context. However, manually searching for each reference on the internet can be tedious, especially when only the names of the references are available in the paper. This project streamlines this process by extracting references, searching for the corresponding research papers, and retrieving their abstracts using APIs.

#### How It Works:

##### Reference Extraction:
Utilizes the Docparser API to extract references from research papers by identifying the section containing references.
##### Paper Name Extraction:
Employs regular expressions in Python to extract the names of the papers from the extracted references.
##### Web Scraping:
Utilizes Beautiful Soup 4 for web scraping, searching for each paper on ResearchGate using its name.
##### Data Extraction:
Extracts the name, link, and abstract of the identified papers from ResearchGate.
##### Data Storage:
Compiles and formats all extracted data.
Stores the data in a MongoDB database.
#### User Interface:
Implements a basic UI using Streamlit, allowing users to interact with the project by uploading desired research papers.

#### How to Run:
##### Step 1:
Create and activate a virtual environment in Python.
##### Step 2:
Use the command *pip install -r requirements.txt* to download all project dependencies.
##### Step 3:
Use the command *streamlit run streamlitpage.py* to interact with the project. Note: The project is not deployed; files are saved and retrieved locally.

### Note:
This project is designed for local use, and Streamlit is used solely for testing purposes. Files are saved in local directories, and the MongoDB database stores the compiled data.
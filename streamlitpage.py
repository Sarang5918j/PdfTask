import streamlit as st
import base64
import main

def get_binary_file_downloader_html(bin_file, file_label='File'):
    """
    Create a download link for a binary file.

    Parameters:
    - bin_file (bytes): The binary file content.
    - file_label (str): The label for the file.

    Returns:
    (str): A string containing the HTML code for the download link.
    """
    b64 = base64.b64encode(bin_file).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{file_label}.csv">Download {file_label} CSV</a>'

st.title("Job Task: PDF and Web Data Scraping for Machine Learning")

file_path = st.file_uploader("Upload a PDF file", type=["pdf"])

# Assuming the CSV file path is "extracted_data/download_file.csv"
csv_file_path = "extracted_text/downloaded_file.csv"

if file_path:
        if st.button("Extract Data", key="extract_data"):
            st.info("Please wait a few minutes! Extracting data...")
            
            # Extract and store data
            extracted_data = main.make_data(file_path)
            main.database_integrator.store_data(extracted_data)
            main.database_integrator.retrieve_and_save_csv()
            csv_file_path = "extracted_text/downloaded_file.csv"
            
            st.success("Data extracted successfully.")

# Button to trigger the download
if st.button("Download CSV File", key="download_csv"):
    with open(csv_file_path, "rb") as csv_file:
        csv_content = csv_file.read()
        st.markdown(get_binary_file_downloader_html(csv_content, file_label='DownloadFile'), unsafe_allow_html=True)

import pydocparser
import requests
from bs4 import BeautifulSoup
import re

api_key = 'a97eb5d696857fea8bfa9e57fb9994017a3bb7da'
parser_id = 'paper_parser'


def convert_to_file(text, file_path):
    
    with open(file_path, 'w') as file:
        file.write(text)

    return file_path

def convert_to_plaintext(input_string):
    # Use regular expression to remove non-alphabetic characters
    clean_string = re.sub(r'[^a-zA-Z ]', '', input_string)
    return clean_string

def extract_words_in_quotes(input_string):
    clean = re.sub(r'\n', ' ', input_string)
    pattern = r'[“"]([^”"]*)[”"]'
    matches = re.findall(pattern, clean)
    
    return matches

#Pdf Extraction
def get_references(file_path):

    parser = pydocparser.Parser()
    parser.login(api_key)
    result = parser.ping()
    print("Connection success with docparser:",result)
    id = parser.upload_file_by_path(file_path, "paper_parser") 
    data = parser.get_one_result("paper_parser", id)
    # keywords = data[0]['keywords']
    references = data[0]['references']
    # abstract = data[0]['abstract']
    names = extract_words_in_quotes(references)

    return names

# Scraping

#function to scrape abstract of related papers on research gate
def get_abstract_from_paper_url(paper_page_url, headers):
    response = requests.get(paper_page_url, headers=headers)
    i = 1
    while i<-50:
        print(f"making attempt {i} to get abstract")
        response = requests.get(paper_page_url, headers=headers)
        if response.status_code==200:
            break
        else:
            i += 1
    if response.status_code == 200:
        paper_soup = BeautifulSoup(response.text, 'html.parser')

        abstract_element = paper_soup.find('div', {'class': 'nova-legacy-e-text nova-legacy-e-text--size-m nova-legacy-e-text--family-sans-serif nova-legacy-e-text--spacing-none nova-legacy-e-text--color-grey-800 research-detail-middle-section__abstract'})
        
        if abstract_element:
            abstract = abstract_element.get_text(strip=True)
            return abstract
        else:
            return "Abstract not found."
    else:
        print(f"Failed to retrieve paper page: {response.status_code}")
        return None


# function to open paper link by name and returns the name, link and abstract of refrences found
def open_paper_link_by_name(paper_name):
    base_url = "https://www.researchgate.net/search/publication?q="
    search_url = base_url + paper_name.replace(" ", "+")
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    i = 1
    while i<=50:
        print(f"making attempt {i} to open paper link")
        response = requests.get(search_url, headers=headers)
        if response.status_code==200:
            break
        else:
            i += 1

    # Make a request to the ResearchGate search page
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all search results
        result_links = soup.find_all('a', {'class':  ['nova-legacy-e-link', 'nova-legacy-e-link--color-inherit', 'nova-legacy-e-link--theme-bare']})

        if result_links:
            print("Resutls found")

            for link in result_links:
                result_name = link.get_text(strip=True)

                result_name = convert_to_plaintext(result_name)

                # Check if the result name matches the given paper name
                if paper_name.lower() in result_name.lower():
                    paper_page_url = "https://www.researchgate.net/" + link['href']
                    abstract = get_abstract_from_paper_url(paper_page_url, headers=headers)
                
                    return result_name, paper_page_url, abstract


            print(f"No exact match found for '{paper_name}' in the search results.")    
         
        else:
            return f"No results found for '{paper_name}'."
    else:
        print(f"Failed to perform the search: {response.status_code}")
        return None

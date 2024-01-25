import json
import os
import scraper

# Assuming you have a JSON file named 'output.json'
json_filename = 'extracted_text/output.json'

# Function to append information to the JSON file
def append_to_json(json_filename, input_paper):
    # Initialize an empty list to store references
    references_list = []

    # Check if the file exists
    if not os.path.exists(json_filename):
        # If it doesn't exist, create a new JSON file
        with open(json_filename, 'w') as json_file:
            json.dump([], json_file)

    # Load existing data from the JSON file
    with open(json_filename, 'r') as json_file:
        references_list = json.load(json_file)

    references = scraper.get_references(input_paper)
    total_references = len(references)
    print(f"Found {total_references} references.")

    for num_references in range(total_references):
        reference = scraper.convert_to_plaintext(references[num_references])
        print(reference, "reference")
        result = scraper.open_paper_link_by_name(reference)
        if result:
            name, link, abstract = result[:3]
            reference_info = {
                "Reference no": num_references + 1,
                "Name": name,
                "ResearchGate link": link,
                "Abstract": abstract
            }

            references_list.append(reference_info)
        else:
            continue

    # Save the updated data to the JSON file
    with open(json_filename, 'w') as json_file:
        json.dump(references_list, json_file, indent=2)

    print("--------------------- Job Done ---------------------")

# Example usage
if __name__ == "__main__":
    append_to_json(json_filename, 'data_samples/electricity-theft-detection-using-machine-learning-IJERTCONV10IS04024.pdf')

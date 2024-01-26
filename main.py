import database_integrator
import scraper
import tempfile

# Function to append information to the JSON file
def save_uploaded_file(uploaded_file):
    try:
        # Create a temporary file to store the uploaded content
        temp_file = tempfile.NamedTemporaryFile(delete=False)

        # Write the uploaded content to the temporary file
        temp_file.write(uploaded_file.read())

        # Return the path of the temporary file
        return temp_file.name

    except Exception as es:
        return None


def make_data(uploaded_file):
    try: 
        temp_file_path = save_uploaded_file(uploaded_file)
    # Initialize an empty list to store references
        references_dict = {}

        references = scraper.get_references(temp_file_path)
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

                references_dict[f"{num_references+1}"] = reference_info
            else:
                continue

        print("--------------------- Job Done ---------------------")

        return references_dict
    except Exception as es:
        return None

# Example usage
if __name__ == "__main__":

    # extracted_data = make_data(
        # 'data_samples/electricity-theft-detection-using-machine-learning-IJERTCONV10IS04024.pdf'
        # )

    # database_integrator.store_data(extracted_data)
    database_integrator.retrieve_and_save_csv()
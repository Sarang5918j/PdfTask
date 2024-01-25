import database_integrator
import scraper

# Function to append information to the JSON file
def make_data(input_paper):
    # Initialize an empty list to store references
    references_dict = {}

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

            references_dict[f"{num_references+1}"] = reference_info
        else:
            continue

    print("--------------------- Job Done ---------------------")

    return references_dict

# Example usage
if __name__ == "__main__":

    # extracted_data = make_data(
        # 'data_samples/electricity-theft-detection-using-machine-learning-IJERTCONV10IS04024.pdf'
        # )

    # database_integrator.store_data(extracted_data)
    database_integrator.retrieve_and_save_csv()
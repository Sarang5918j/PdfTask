import scraper
from reportlab.pdfgen import canvas
import os

# Assuming you have a PDF file named 'output.pdf'
pdf_filename = 'extracted_text/output.pdf'

# Function to append information to the PDF
def append_to_pdf(pdf_filename, input_paper):
    # Check if the file exists
    if not os.path.exists(pdf_filename):
        # If it doesn't exist, create a new PDF file
        with open(pdf_filename, 'wb'):
            pass

    with open(pdf_filename, 'ab') as pdf_file:
        # Create a canvas to draw on the PDF
        pdf_canvas = canvas.Canvas(pdf_file)

        # Set the font and size
        pdf_canvas.setFont("Helvetica", 12)

        references = scraper.get_references(input_paper)
        total_references = len(references)
        print(f"Found {total_references} references.")

        y_coordinate = 70
        for num_references in range(total_references):
            reference = scraper.convert_to_plaintext(references[num_references])
            print(reference,"reference")
            result = scraper.open_paper_link_by_name(reference)
            if result:
                name, link, abstract = result[:3]
                # print(f"Reference no: {num_references}, Name: {name}, ResearchGate link: {link}\
                #     ,Abstract: {abstract}")
                pdf_canvas.drawString(50, y_coordinate, f"Reference no: {num_references+1}")
                pdf_canvas.drawString(50, y_coordinate-20, f"Name: {name}")
                pdf_canvas.drawString(50, y_coordinate-40, f"ResearchGate link: {link}")
                pdf_canvas.drawString(50, y_coordinate-60, f"Abstract: {abstract}")

                y_coordinate -= 80
            else:
                continue

        # Save the canvas to the PDF
        pdf_canvas.save()
        print("--------------------- Job Done ---------------------")

# Example usage

# Append information to the PDF
if __name__ == "__main__":
    append_to_pdf(pdf_filename, 'data_samples\electricity-theft-detection-using-machine-learning-IJERTCONV10IS04024.pdf')

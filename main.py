from pypdf import PdfReader
import os
import pickle
def PDF_to_txt(file):
    # creating a pdf reader object
    DATA = {
        "pages": []
    }
    reader = PdfReader(file)
    page_count = 0

    for page in reader.pages:
        page_data = {
            "page_number": page_count + 1,
            "text": page.extract_text(),
        }
        page_count += 1
        DATA["pages"].append(page_data)
    # print(text)

    if not os.path.exists("./Extracted_Data"):
        os.mkdir("./Extracted_Data")
    with open(f"./Extracted_Data/{file}.bin", "wb") as file:
        pickle.dump(DATA, file)
    return DATA
PDF_to_txt("EASA_Concept_Paper_Guidance_for_Level_1and2_machine_learning_applications_Issue_02.pdf")
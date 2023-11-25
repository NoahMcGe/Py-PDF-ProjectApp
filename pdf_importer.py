#Noah McGehee 11/24/2023
from PyPDF2 import PdfReader
import re

def import_project_from_pdf(file_path):
    try:
        with open(file_path, "rb") as file:
            pdf_reader = PdfReader(file)
            num_pages = len(pdf_reader.pages)

            # Extract text from all pages
            text = ""
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

            # Use regex to extract project information
            project_title_match = re.search(r"Project Title:\s*(.+)", text)
            project_title = project_title_match.group(1).strip() if project_title_match else ""

            description_match = re.search(r"Description:\s*(.+?)Technologies Used:", text, re.DOTALL)
            description = description_match.group(1).strip() if description_match else ""

            technologies_used_match = re.search(r"Technologies Used:\s*(.+?)Challenges Faced:", text, re.DOTALL)
            technologies_used = technologies_used_match.group(1).strip() if technologies_used_match else ""

            challenges_faced_match = re.search(r"Challenges Faced:\s*(.+)", text, re.DOTALL)
            challenges_faced = challenges_faced_match.group(1).strip() if challenges_faced_match else ""

            return {
                "project_title": project_title,
                "description": description,
                "technologies_used": technologies_used,
                "challenges_faced": challenges_faced
            }

    except Exception as e:
        print(f"Error importing project from PDF: {e}")
        return None

import os
import re
import pandas as pd
from pdfminer.high_level import extract_text

# Define a function to extract the text from a PDF
def extract_text_from_pdf(file_path):
    return extract_text(file_path)

# Define a function to extract sections from the text
def extract_sections(text):
    text = text.lower()  # Convert text to lowercase
    abstract = re.search(r'(?i)(abstract|summary)[\s\S]*?(?=(\n\s*\n)|I\.|1\.|introduction|background|method)', text)
    abstract = abstract.group(0) if abstract else ''
    results = re.search(r'(?i)(results|findings)[\s\S]*?(?=(\n\s*\n)|discussion)', text)
    results = results.group(0) if results else ''
    conclusion = re.search(r'(?i)(conclusion|conclusions)[\s\S]*', text)
    conclusion = conclusion.group(0) if conclusion else ''
    return abstract, results, conclusion

# Create a list to hold the data
data = []

# Set the directory path
dir_path = 'src/google_scholar'

# Iterate over all PDFs in the directory
for file_name in os.listdir(dir_path):
    if file_name.endswith('.pdf'):
        # Extract text from the PDF
        file_path = os.path.join(dir_path, file_name)
        text = extract_text_from_pdf(file_path)
        # Extract sections from the text
        abstract, results, conclusion = extract_sections(text)
        # Append the data to the list
        data.append({
            'file_name': file_name,
            'abstract': abstract,
            'results': results,
            'conclusion': conclusion
        })

# Convert the list to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv('src/google_scholar/papers.csv', index=False)
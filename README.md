# Word Occurrences Per Page

This Python script analyzes the occurrences of a given list of words in a Word document and plots the occurrences per page in a bar chart. The script converts the Word document to a PDF file, then extracts the text from each page and counts the occurrences of each word. The resulting bar chart shows the word occurrences stacked on top of each other for easy visualization. The chart is saved as an image file, and the temporary PDF file created during the process is removed.
## Dependencies

The script requires the following Python libraries:

- docx2pdf: for converting Word documents to PDF files
- PyMuPDF: for reading and extracting text from PDF files
- matplotlib: for creating the bar chart

You can install the dependencies using the following command:

`pip install docx2pdf PyMuPDF matplotlib`

## Usage

- Place the Word document you want to analyze in the same directory as the script. In this example, the file name is tecnología_infraestructuras_mercados_financieros.docx. You can change the input_file variable in the script to match the name of your Word document.
- Update the words list in the script with the words you want to count.
- Run the script:

`python word_occurrences_per_page.py`

The script will create a bar chart image file named word_occurrences_per_page.png in the same directory. Open this file to see the occurrences of each word per page in the document.

## Customization

You can customize the following variables in the script to change the appearance and behavior of the plot:

`input_file`: the name of the Word document to analyze
`output_file`: the name of the temporary PDF file created during the process (default: same name as input_file with a .pdf extension)
`words`: a list of words to count in the document
`colors`: a list of colors to use for the bars in the chart
`num_ticks`: the number of x-axis ticks to display on the chart (default: 20)

## License

This project is released under the MIT License. See LICENSE for more information.

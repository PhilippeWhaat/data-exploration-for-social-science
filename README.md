# Word Occurrences Per Page

The Python `word_occurrences_per_page.py` script analyzes the occurrences of a given list of words in a Word document and plots the occurrences per page in a bar chart. The script converts the Word document to a PDF file, then extracts the text from each page and counts the occurrences of each word. The resulting bar chart shows the word occurrences stacked on top of each other for easy visualization. The chart is saved as an image file, and the temporary PDF file created during the process is removed.
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

- `input_file`: the name of the Word document to analyze
- `output_file`: the name of the temporary PDF file created during the process (default: same name as input_file with a .pdf extension)
- `words`: a list of words to count in the document
- `colors`: a list of colors to use for the bars in the chart
- `num_ticks`: the number of x-axis ticks to display on the chart (default: 20)

## License

This project is released under the MIT License. See LICENSE for more information.

# Classification of academic papers Using GPT 3.5 Turbo and Sentiment Analysis with NLTK and VADER

The script reads an Excel file named "liste_fichiers_completed.xlsx" that should contain the titles and abstract of the articles to be processed.

After running the script, it processes the content of the articles and generates feedback based on the relevance of the articles. The feedback is then stored back to a CSV file named "eval_sentiment.csv".

The evaluation feedback is generated based on whether the article addresses the following aspects:

- The challenges in interpreting and understanding the meaning of legal language, and how these impact the ability of AI models to analyze and make decisions based on legal texts.
- The relationship between causal inference algorithms and the process of legal language understanding.
- Methods to overcome the lack of empirical context in the causal analysis of legal texts, and suggestions for collecting data on a sufficient set of variables to block all the backdoor paths between the intervention and the outcome.
- The challenges and limitations in conducting automatic analysis of legal corpora and whether it proposes a theoretical framework to evaluate the causal links in the models produced.
- The potential impact of using causal AI techniques in the field of automatic legal language processing and its application in legal decision-making compared to traditional AI models relying on correlations.

The script expresses both the polarity (positive/negative) and the intensity (strength) of emotion in the feedback.

If there's an API rate limit error, the script will wait for 10 seconds before making the next request. If there's any other error, the script will also wait for 10 seconds before moving to the next row of data.

At the end, the script calculates and prints the total cost of the tokens that are necesary, so that you can predict how much it is going to cost.

Then, we use the NLTK library and the sentiment analysis tool called VADER (Valence Aware Dictionary and sEntiment Reasoner) to analyze the sentiment or the overall emotional tone of a given text. Specifically, we're leveraging sentiment analysis as a way to estimate the certainty or relevance of the text to a research question.

The sentiment analysis provided by VADER works by assigning a sentiment score to each word in the text and then aggregating those scores to provide an overall sentiment score. These scores are based on a pre-trained model that has been trained on a large corpus of texts.

The sentiment scores provided by VADER include four values: positive, negative, neutral, and compound. By multiplying the compound score by 100 and converting it to an integer, we obtain a certainty score between 0 and 100. Due to our data structure, we only evaluate the first sentence of each evaluation.

In this project, we use two kinds of sentiment score calculations: one that maintains the distinction between negative and positive sentiment scores and one that does not. We then compute Kendall's Tau to measure the similarity between these two rankings.

The code provided calculates these scores, performs ranking, computes Kendall's Tau and plots the score's cumulative average. It further identifies the point of stabilization using the derivative of the global average of certainty scores.

Finally, the code saves the classified data into an Excel file.

## Dependencies

This project requires Python along with the following libraries:

- pandas
- NLTK
- ast
- scipy
- matplotlib
- numpy
- openai
- tiktoken
- os
- time

Before running the script, make sure to install these libraries using pip:

`pip install pandas nltk ast scipy matplotlib numpy`

You also need OpenAI API key and OpenAI ORG key, which are expected to be defined in your environment variables.

After installation, you can run the scripts `1_list_documents.py` for creating the list of files, so that you can manually extract the abstract for each one. The files `2_litterature_relevance.ipynb` `3_processing_relevance.ipynb` are the script that execute the tasks listed in introduction of this description. Script `4_order_files.py` only aims to modify the PDFs names.

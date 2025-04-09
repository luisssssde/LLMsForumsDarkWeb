Overview

Please cite this paper: de-Marcos & Domínguez-Diaz (2025). LLM-Based Topic Modeling for Dark Web Q&A forums: A Comparative Analysis with Traditional Methods. IEEE Access.

This repository contains a set of Python scripts designed to process and analyze text data extracted from various sources, specifically focusing on forum posts from the dark web. The scripts perform cleaning, topic modeling, and keyword extraction using different methodologies, including TF-IDF, Gensim's LDA, and OpenAI's GPT.
Table of Contents

    Installation
    Usage
    Scripts Description
    Data Structure
    License

Installation

To run the scripts in this repository, you need to have Python installed on your machine. Additionally, you will need to install the required libraries. You can do this using pip:

    bash

    pip install pandas openai scikit-learn gensim nltk

Make sure to download the NLTK resources by running the following commands in a Python shell:

    python

    import nltk

    nltk.download('punkt')

    nltk.download('stopwords')


Usage

Data Preparation: Place your text files in the appropriate directories (data/Questions/onion1, data/Questions/onion2, data/Questions/onion3) as specified in the scripts.

Run the Cleaning Scripts: Execute the cleaning scripts to process the text files and save the cleaned data to Excel files.

    bash

    python 1extract_onion1.py
    
    python 1extract_onion2.py
    
    python 1extract_onion3.py

Topic Modeling: After cleaning, you can run the topic modeling scripts to extract topics from the cleaned text.

    bash
    
    python 2TopicsSkLearn_EN.py
    
    python 2TopicsGensim_EN.py
    
    python 2topicModeling_GPT.py


Scripts Description
1. Cleaning Scripts

    1extract_onion1.py: Cleans text files from the onion1 dataset by applying specific removal rules to extract relevant content.

    1extract_onion2.py: Similar to the first script but tailored for the onion2 dataset with different removal rules.

    1extract_onion3.py: Processes the onion3 dataset, applying its own set of cleaning rules.

2. Topic Modeling Scripts

    2TopicsSkLearn_EN.py: Uses TF-IDF vectorization to extract the top keywords from the cleaned text and saves the results to an Excel file.

    2TopicsGensim_EN.py: Implements LDA topic modeling using Gensim to identify topics in the cleaned text and saves the results.

    2topicModeling_GPT.py: Utilizes OpenAI's GPT model to extract topics from the cleaned text. Make sure to replace "your api key here" with your actual OpenAI API key.


Data Structure

    Input Data: The input data consists of text files located in the data/Questions/onion1, data/Questions/onion2, and data/Questions/onion3 directories.

    Output Data: The cleaned data is saved as Excel files (cleaned_posts_onion1.xlsx, cleaned_posts_onion2.xlsx, cleaned_posts_onion3.xlsx). The topic modeling results are saved as onion3_topics_Sklearn.xlsx, onion3_topics_genism.xlsx, and merged_onion_topics_final_v2_gpt.xlsx.


License

This project is licensed under the MIT License. See the LICENSE file for details.

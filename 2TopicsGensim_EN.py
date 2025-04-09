# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:36:31 2025

@author: Luis
"""

import pandas as pd
import nltk    # pip install gensim nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora
from gensim.models import LdaModel
import re

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Read texts from an Excel file
df = pd.read_excel('data/posts_onion3_clean_translated.xlsx')  # Ensure the file is in the same directory or provide the full path
texts = df['FullText'].tolist()  # Extract the 'FullText' column as a list

# Preprocess the texts
def preprocess(text):
    # Remove punctuation and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

# Initialize a list to hold the results
results = []

# Process each text individually
for i, text in enumerate(texts):
    processed_text = preprocess(text)
    
    # Create a dictionary and corpus for LDA
    dictionary = corpora.Dictionary([processed_text])
    corpus = [dictionary.doc2bow(processed_text)]
    
    # Set parameters for LDA
    num_topics = 1  # Since we are modeling one text at a time, we set this to 1
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)
    
    # Store the topics for each text
    topics = []
    for idx, topic in lda_model.print_topics(-1):
        # Extract the topic words and their weights
        topic_words = topic.split(' + ')
        # Get only the words (excluding weights)
        topic_terms = [word.split('*')[1].strip('"') for word in topic_words]
        topics.append(', '.join(topic_terms[:3]))  # Get the first 3 topic words
    
    # Append the results to the list, keeping original information
    results.append({
        'Topics': ', '.join(topics[:3])  # Join the first 3 topics
    })

# Create a DataFrame from the results
results_df = pd.DataFrame(results)

# Add original columns from the input DataFrame
for column in df.columns:
    results_df[column] = df[column]

# Define the output Excel file path
output_file = 'onion3_topics_genism.xlsx'

# Write the DataFrame to an Excel file
results_df.to_excel(output_file, index=False)

print(f"Data has been written to {output_file}")

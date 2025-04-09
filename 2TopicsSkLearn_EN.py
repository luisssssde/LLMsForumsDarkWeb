# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 17:52:07 2025

@author: Luis
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Step 1: Read abstracts from the Excel file
file_path = "data/posts_onion3_clean_translated.xlsx"

# Read the Excel file and extract the 'FullText' column
df = pd.read_excel(file_path)
abstracts = df['FullText'].tolist()

# Step 2: Vectorize the abstracts using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(abstracts)

# Step 3: Extract top keywords for each abstract
def extract_top_keywords(tfidf_matrix, feature_names, abstracts, top_n=5):
    results = []
    for i, abstract in enumerate(abstracts):
        # Get the TF-IDF scores for the current abstract
        tfidf_scores = tfidf_matrix[i].toarray()[0]
        # Get the indices of the top N keywords
        top_indices = tfidf_scores.argsort()[-top_n:][::-1]
        # Get the top keywords
        top_keywords = [feature_names[j] for j in top_indices]
        
        # Store the results in a dictionary
        results.append({
            'Topics': ', '.join(top_keywords)
        })
    
    return results

# Get the feature names (words)
feature_names = vectorizer.get_feature_names_out()

# Extract top keywords for each abstract
top_keywords_results = extract_top_keywords(X, feature_names, abstracts, top_n=3)

# Step 4: Create a DataFrame to store results and original information
results_df = pd.DataFrame(top_keywords_results)

# Combine the original DataFrame with the results
final_df = pd.concat([df, results_df], axis=1)

# Step 5: Save the results to a new Excel file
output_file_path = "onion3_topics_Sklearn.xlsx"
final_df.to_excel(output_file_path, index=False)

print(f"Results saved to {output_file_path}")

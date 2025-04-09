# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:00:23 2024

@author: Luis
"""

import pandas as pd
from openai import OpenAI

# Set your OpenAI API key
my_api_key = "YOUR API KEY HERE"

client = OpenAI(api_key=my_api_key)

# Function to get topic from ChatGPT
def get_topics(text):
    prompt = f"Topic modeling for the following text: '{text}'\n\n"
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that analyzes and extracts the main topics of forum posts from the dark web. Each topic contains a maximum of 1 word/acronym. And for each post a maximum of 3 topics. Return only the topics separated by commas"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=50,
        n=1,
        temperature=0, #from 0-(deterministic) to 1-(creative)
    )
    topics = response.choices[0].message.content.strip()
    print(topics)
    return topics

# Load the Excel file
file_path = 'results/merged_onion_topics_final_v2.xlsx'
df = pd.read_excel(file_path)

# Check if 'Text' column exists
if 'FullText' not in df.columns:
    raise ValueError("The 'text' column is missing in the Excel file.")

# Analyze sentiment for each review
df['ChatGPT'] = df['FullText'].apply(get_topics)

# Save the results back to a new Excel file
output_file_path = 'merged_onion_topics_final_v2_gpt.xlsx'
df.to_excel(output_file_path, index=False)

print(f"Sentiment analysis completed. Results saved to {output_file_path}.")

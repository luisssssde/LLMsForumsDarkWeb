import os
from google import genai
from google.genai import types
import pandas as pd

API_KEY = "..."
FILENAME = "merged_onion_topics_final.xlsx"
MODEL = "gemini-2.0-flash"

client = genai.Client(api_key=API_KEY)

processed_files = set()

results_file = "gemini_results.csv"    
if not os.path.exists(results_file):
    with open(results_file, 'w') as f:
        f.write("Filename;gemini\n")
else:
    with open(results_file, 'r') as f:
        next(f)  # Skip the header
        for line in f:
            processed_files.add(line.split(',')[0])
    
df = pd.read_excel(FILENAME)
with open(results_file, 'a') as f:
    for index, row in df.iterrows():
        if row['Filename'] in processed_files:
            continue
        
        content = row["FullText"]
        prompt = f"You are a helpful assistant that analyzes and extracts" + \
            " the main topics of forum posts from the dark web. " + \
            "Each topic contains a maximum of 1 word/acronym. " + \
            "Each post contains a maximum of 3 topics. " + \
            "Return only the topics separated by commas." + \
            f"This is the content to analyze: {content}"

        # Send request to Google Gemini API
        response = client.models.generate_content(
            model=MODEL,
            contents=[prompt]
        )

        # Extract the generated content
        if response.text is not None:
            generated_content = response.text.lower().replace("\n", "")
        else:
            generated_content = "NA"
        
        # Write the results to a file    
        f.write(f"{row['Filename']};{generated_content}\n")
        if index % 10 == 0:
            f.flush()

        
            
    
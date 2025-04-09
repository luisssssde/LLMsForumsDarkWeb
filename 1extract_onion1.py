# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 17:06:09 2025

@author: Luis

RULES. Order is important:
Remove all text before "Ask a Question"
Remove the first line
Remove the final 3 lines
Remove all lines starting with *
Remove all lines containing "Advertisments"
Remove all lines containing "Categories"
Remove all lines containing "vote" or "votes"
Remove all lines containing "answer" or "answers" (upper and lowercase)
**vote|votes|answer|answers|answered|commented
Remove all lines started by "asked"
Remove any line containing "Related questions" and all the text that follows
"""

import os
import pandas as pd
import re

def clean_post_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Remove everything before "Ask a Question"
    start_index = next((i for i, line in enumerate(lines) if "Ask a Question" in line), -1)
    if start_index != -1:
        lines = lines[start_index + 1:]
    
    # Remove the first line if it exists
    if lines:
        lines = lines[1:]
    
    # Remove last 3 lines
    if len(lines) > 3:
        lines = lines[:-3]
    else:
        lines = []
    
    # Apply filters to remove unwanted lines
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if (line.startswith("*") or "Advertisments" in line or "Categories" in line or "Ask a Question" in line or "Ask a question" in line or
            re.search(r"\b(vote|votes|answer|answers|answered|commented)\b", line, re.IGNORECASE) or 
            line.startswith("asked")):
            continue
        
        # Stop processing if "Related questions" is found
        if "Related questions" in line:
            break
        
        cleaned_lines.append(line)
    
    return "\n".join(cleaned_lines)

def process_files(folder_path, output_file):
    data = []
    
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            cleaned_text = clean_post_content(file_path)
            data.append([file_name, cleaned_text])
    
    df = pd.DataFrame(data, columns=["Filename", "Cleaned Text"])
    df.to_excel(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    folder_path = "data/Questions/onion1"  # Folder containing text files
    output_file = "cleaned_posts_onion1.xlsx"  # Output Excel file
    process_files(folder_path, output_file)

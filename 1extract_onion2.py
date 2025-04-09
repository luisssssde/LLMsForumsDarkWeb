# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 18:28:07 2025

@author: Luis
"""

import os
import pandas as pd
import re

def clean_post_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Define removal rules
    exact_removals = {"Remember", "Español | English | Português", "Light switch", "Rules", "Posts", "Categories", "Most popular tags", "Latest Chat"}
    starts_with_removals = ("Welcome to", "Advertising", "You must login", "Please log in")
    contains_removals = ("vote", "votes", "answer", "answers", "questions", "comments", "users", "days,", "chats", "Users", "points")
    starts_with_patterns = ("*", "answered", "asked")
    
    # Stop processing if "Related questions" is found
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if "Related questions" in line:
            break
        
        if (line in exact_removals or
            line.startswith(starts_with_removals) or
            any(word in line for word in contains_removals) or
            line.startswith(starts_with_patterns)):
            continue
        
        cleaned_lines.append(line)
    
    # Remove final line if it contains a period
    if cleaned_lines and "." in cleaned_lines[-1]:
        cleaned_lines.pop()
    
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
    folder_path = "data/Questions/onion2"  # Folder containing text files
    output_file = "cleaned_posts_onion2.xlsx"  # Output Excel file
    process_files(folder_path, output_file)

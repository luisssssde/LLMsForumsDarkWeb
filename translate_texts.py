import os
import pandas as pd
from deep_translator import GoogleTranslator

# Set the working directory
working_directory = '.'

# Initialize the translator
translator = GoogleTranslator(source='portuguese', target='english')

# Loop through all xlsx files in the working directory
for file in os.listdir(working_directory):
    if file.endswith('.xlsx'):
        file_path = os.path.join(working_directory, file)
        
        # Read the xlsx file
        df = pd.read_excel(file_path)
        
        translated_topics = []

        # Check if the "Topics" column exists
        if 'FullText' in df.columns:
            topics = df['FullText']            
            for topic in topics:
                if pd.notnull(topic):
                    try:
                        chunk_size = 5000
                        topic_chunks = []
                        current_chunk = ""

                        for line in topic.split('\n'):
                            if len(current_chunk) + len(line) + 1 > chunk_size:
                                topic_chunks.append(current_chunk)
                                current_chunk = line
                            else:
                                current_chunk += "\n" + line if current_chunk else line

                        if current_chunk:
                            topic_chunks.append(current_chunk)

                        translated_topic = ""
                        for chunk in topic_chunks:
                            translated_topic += translator.translate(chunk) + "\n"

                        translated_topics.append(translated_topic)
                    except:
                        translated_topics.append("Error")
                else:
                    translated_topics.append(None)                

            # Translate each row in the "Topics" column
            df['FullText Translated'] = translated_topics
            
            # Save the translated topics to a new xlsx file
            translated_file_path = os.path.join(working_directory, f'translated_{file}')
            df.to_excel(translated_file_path, index=False)
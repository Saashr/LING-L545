import re

def segment_sentences(text):
    # Define a regex pattern that captures common sentence terminators including the Arabic full stop
    sentence_endings_regex = r'([.!?۔])'
    
    # Split the text using the defined regex, capturing the punctuation marks
    parts = re.split(sentence_endings_regex, text)
    
    # Reconstruct sentences by merging split elements with their punctuations, handling special cases manually
    sentences = []
    sentence = ''
    for i in range(0, len(parts) - 1, 2):  
        part = parts[i] + parts[i + 1]
        sentence += part.strip()

        # Manually handle sentences that start with a number (likely years or single dates)
        if i == 0 and part.strip().isdigit():
            continue  

        # Look for decimal points within numbers
        if re.search(r'\d[.۔]\d', part):  
            continue  

        # When the part matches the normal end of a sentence or does not fit any special case
        sentences.append(sentence)
        sentence = ''

    # Add the last part if it was not added 
    if parts and sentence:
        sentences.append(sentence + parts[-1].strip())

    return sentences

def read_and_segment_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
        sentences = segment_sentences(text)
        return sentences
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


file_path = 'wiki.txt'  
sentences = read_and_segment_file(file_path)
for sentence in sentences:
    print(sentence)

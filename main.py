#!/usr/bin/env python3

import re  
# The built-in regular expression library

# Define a function to extract different types of data from text
def extract_data(text):
    # Dictionary of regex patterns with clear labels
    patterns = {
        "Emails": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
        "URLs": r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',
        "Phone Numbers": r'\(?\d{3}\)?[ .-]?\d{3}[ .-]?\d{4}',
        "Credit Cards": r'\b(?:\d{4}[- ]?){3}\d{4}\b',
        "Times": r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?: ?[APap][Mm])?\b'
    }

    results = {}  # Dictionary to store all matches

    # For each pattern, search for all matches in the text
    for label, pattern in patterns.items():
        matches = re.findall(pattern, text)
        results[label] = matches

    return results

# Entry point for the script
if __name__ == "__main__":
    # Read input from a text file (simulating multiple pages of data)
    with open("test_inputs.txt", "r") as file:
        text = file.read()

    # Call the extract_data function
    extracted_info = extract_data(text)

    # Print the results clearly
    for label, data in extracted_info.items():
        print(f"\n{label} Found:")
        for item in data:
            print(f" - {item}")


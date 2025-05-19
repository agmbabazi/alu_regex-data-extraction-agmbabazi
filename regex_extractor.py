#!/usr/bin/env python3

import re

def validate_email(text):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(pattern, text)

def validate_url(text):
    pattern = r'^https?://([\w.-]+\.)+[a-zA-Z]{2,}(/[^\s]*)?$'
    return re.fullmatch(pattern, text)

def validate_phone(text):
    pattern = r'^(\(\d{3}\)\s?|\d{3}[-.])?\d{3}[-.]\d{4}$'
    return re.fullmatch(pattern, text)

def validate_currency(text):
    pattern = r'^\$\d{1,3}(,\d{3})*(\.\d{2})?$|^\$\d+(\.\d{2})?$'
    return re.fullmatch(pattern, text)

def process_file(filename, validator, label):
    print(f"\nValidating {label} in '{filename}':")
    try:
        with open(filename, 'r') as file:
            for i, line in enumerate(file, 1):
                value = line.strip()
                if not value:
                    continue
                if validator(value):
                    print(f"Line {i}: ✅ Valid -> {value}")
                else:
                    print(f"Line {i}: ❌ Invalid -> {value}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")

def main():
    print("🔍 Welcome to the Regex Data Extractor!\n")
    print("Select an option:")
    print("1. Validate Emails (emails.txt)")
    print("2. Validate URLs (urls.txt)")
    print("3. Validate Phone Numbers (phones.txt)")
    print("4. Validate Currency Amounts (currency.txt)")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        process_file("emails.txt", validate_email, "email addresses")
    elif choice == "2":
        process_file("urls.txt", validate_url, "URLs")
    elif choice == "3":
        process_file("phones.txt", validate_phone, "phone numbers")
    elif choice == "4":
        process_file("currency.txt", validate_currency, "currency amounts")
    elif choice == "5":
        print("👋 Exiting program. Goodbye!")
    else:
        print("Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()


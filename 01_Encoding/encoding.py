import unicodedata
import sys

# Characters to remove in shahmukhi punjabi
chars_to_remove = {'\u00A0', '\u200D'}  # Remove NO-BREAK SPACE and ZERO WIDTH JOINER

# Remove characters & calculate frequencies 
normalized_char_frequency = {}
zs_cf_frequency_after_normalization = {}

with open('wiki.txt', 'r', encoding='utf-8') as file:
    for line in file:
        # Normalize the line by removing specific characters
        normalized_line = ''.join(char for char in line if char not in chars_to_remove)
        for char in normalized_line:
            # Update the frequency in the normalized character frequency dictionary
            if char in normalized_char_frequency:
                normalized_char_frequency[char] += 1
            else:
                normalized_char_frequency[char] = 1
            
            # If the character is a Zs or Cf, update zs_cf_frequency_after_normalization
            if unicodedata.category(char) in ['Zs', 'Cf']:
                if char in zs_cf_frequency_after_normalization:
                    zs_cf_frequency_after_normalization[char] += 1
                else:
                    zs_cf_frequency_after_normalization[char] = 1

# Display the character frequencies 
print("Character frequencies after normalization:")
for char, freq in sorted(normalized_char_frequency.items(), key=lambda item: item[1], reverse=True):
    print(f"'{char}': {freq}")

# Display the frequencies of Zs and Cf 
print("\nFrequencies of Zs and Cf characters after normalization:")
for char, freq in sorted(zs_cf_frequency_after_normalization.items(), key=lambda item: item[1], reverse=True):
    char_unicode = f"U+{ord(char):04X}"
    print(f"'{char}' ({unicodedata.name(char)}, {char_unicode}): {freq}")

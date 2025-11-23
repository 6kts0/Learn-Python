"""
SETS DO NOT SUPPORT INDEXING
Faba Kouyate, Fall 2025
"""
from collections import Counter

text = "My name is Walter White... and I live at 800, Negro Auroro lane"
vowels = {'A', 'E', 'I', 'O', 'U'} 

# Converts all instances of lowercase letters into uppercase 
processed_text = text.upper()

# Create the Counter object
counts = Counter(processed_text)

# Sum the counts for all vowels
vowel_count = sum(counts.get(vowel, 0) for vowel in vowels)

# Print total vowels counted in vowel_count 
print(f"The total vowel count is: {vowel_count}")
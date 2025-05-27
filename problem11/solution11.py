

from collections import Counter
import string

rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

# Convert to lowercase and filter only alphabetic characters
filtered = [char.lower() for char in rhyme if char.isalpha()]

# Count frequency
counts = Counter(filtered)

# Find the most frequent character
most_common = counts.most_common(1)[0]

print(f"The most frequent character is '{most_common[0]}' with {most_common[1]} occurrences.")
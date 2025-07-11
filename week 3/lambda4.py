import re

words = ["apple", "banana", "orange", "grape", "umbrella"]

# Capitalize if starts with a vowel
vowel_caps = list(map(lambda w: re.sub(r'^[aeiou]', lambda m: m.group(0).upper(), w), words))
print(vowel_caps)  # ['Apple', 'banana', 'Orange', 'grape', 'Umbrella']
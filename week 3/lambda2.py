import re
data=['hello123','abxv5556b','1xy09z']
cleaned = list(map(lambda s: re.sub(r'[^a-zA-Z]','', s), data))
print(cleaned)  
import re

emails = ["alice@gmail.com.in", "bob@yahoo.com", "user@outlook.com"]

# Extract domain using regex
domains = list(map(lambda s: re.search(r'@(\w+)\.com', s).group(1), emails))
print(domains)  
#pattern for validating url

import re
pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
t = "https://www.example.com"
k = re.search(pattern,t)
if k:
    print("Valid URL", k.group())

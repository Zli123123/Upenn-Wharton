import re

phonenumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phonenumRegex.search("My number is 415-555-4242.")
print(mo.group())

stockup = "BadStock is at +500.64% and will go to -70.111111%, beware. 80%"
x = re.findall(r"(\+*|\-*)(\d+\.*\d*\%)", stockup)
x = re.findall(r"(\+*|\-*)(\d+\.*\d*\%)", 'hello')
print(x)
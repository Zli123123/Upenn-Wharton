nltk.download('punkt')

text = "I do not like green eggs and ham. I like something else than that."

goodstuff = ["soar", "up", "good", "profitable", "increase"]
badstuff = ["plummet", "down", "debt", "decrease"]

a_list = nltk.tokenize.sent_tokenize(text)
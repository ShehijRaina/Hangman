import json

# Load quotes from dataset obtained from 
# https://www.kaggle.com/datasets/akmittal/quotes-dataset
def load_quotes():
	with open("data/quotes.json", "r", encoding="utf-8") as file:
		data = json.load(file)

	quotes = []

	for item in data:
		quote  = item.get("Quote")
		author = item.get("Author")

		if quote and author:
			quotes.append([quote, author])
	
	return quotes
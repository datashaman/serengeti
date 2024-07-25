from pprint import pprint

from transformers import AutoTokenizer, AutoModelForMaskedLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("UBC-NLP/serengeti")
model = AutoModelForMaskedLM.from_pretrained("UBC-NLP/serengeti")

classifier = pipeline("fill-mask", model=model, tokenizer=tokenizer)
pprint(classifier("ẹ jọwọ , ẹ <mask> mi"))

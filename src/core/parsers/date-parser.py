import spacy
from spacy.lang.pt.examples import sentences 

def show_entities(doc):
	if doc.ents:
		for ent in doc.ents:
			print(f'{ent.text} - {ent.label_} - {spacy.explain(ent.label_)}')

nlp = spacy.load("explosion/en_textcat_goemotions")
# nlp = spacy.load('en_core_web_sm')
doc = nlp("hoje consigo ir")
show_entities(doc)
# Write a function to display basic entity info: def show_ents(doc): if doc.ents: for ent in doc.ents: print(ent.text+' - ' +str(ent.start_char) +' - '+ str(ent.end_char) +' - '+ent.label_+ ' - '+str(spacy.explain(ent.label_))) else: print('No named entities found.')

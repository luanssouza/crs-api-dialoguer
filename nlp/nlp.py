import spacy
import en_core_web_sm

def get_age(text):
    nlp = en_core_web_sm.load()
        
    #nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    ageHash = {}
    age =''
    for token in doc:
            ageHash.update({str(token.pos_):str(token.text)})
    return ageHash['NUM']
    #age = body.get_entity_value(resp)
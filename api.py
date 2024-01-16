import paralleldots
paralleldots.set_api_key('api key')

def ner(text):
    ner = paralleldots.ner(text)
    return ner
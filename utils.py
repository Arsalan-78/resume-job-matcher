import spacy
nlp = spacy.load("en_core_web_sm")

def get_resume_summary(text):
    doc = nlp(text)
    num_words = len(text.split())
    num_ents = len(doc.ents)
    top_skills = [ent.text for ent in doc.ents if ent.label_ in ["SKILL", "ORG", "PERSON"]]
    return {
        "word_count": num_words,
        "entities_found": num_ents,
        "top_skills": list(set(top_skills))[:5]
    }
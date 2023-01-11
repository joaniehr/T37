import spacy

nlp = spacy.load('en_core_web_sm')

garden_path_sentences = ["After Bill drank the water proved to be poisoned.",
                         "The old man the boat.",
                         "I convinced her children are noisy.",
                         "Without her contributions would be impossible.",
                         "The girl told the story cried."]

for sentence in garden_path_sentences:
    print(f"Sentence: {sentence}")

    analysis = nlp(sentence)
    print("Sentence analysis: ")
    print([(word.text, word.pos_) for word in analysis])
    print()

print(spacy.explain("ADP"))
print(spacy.explain("AUX"))

"""
I looked up ADP and AUV which returned 'adposition' and 'auxiliary'. 
Yes - these make sense for the positions of the word - 'without' is a preposition and 'would' is an auxiliary verb.
"""

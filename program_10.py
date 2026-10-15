import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import pos_tag, ne_chunk

for p in ['punkt', 'punkt_tab', 'stopwords', 'averaged_perceptron_tagger',
          'averaged_perceptron_tagger_eng', 'maxent_ne_chunker', 'maxent_ne_chunker_tab', 'words']:
    nltk.download(p, quiet=True)

text = ("Barack Obama was born in Hawaii and served as the President "
        "of the United States. He studied at Harvard University and "
        "worked closely with organizations like the United Nations.")
print("Original Text:\n" + text + "\n" + "=" * 70)

words = word_tokenize(text)
print("\n(a) TOKENIZING")
print("Sentence Tokens:", sent_tokenize(text))
print("Word Tokens:", words)

filtered = [w for w in words if w.lower() not in set(stopwords.words('english')) and w.isalnum()]
print("\n(b) FILTERING STOP WORDS")
print("Filtered Words (stop words removed):", filtered)

print("\n(c) STEMMING")
print("Stemmed Words:", [PorterStemmer().stem(w) for w in filtered])

tags = pos_tag(words)
print("\n(d) PART OF SPEECH (POS) TAGGING")
print(tags)

print("\n(e) CHUNKING (Noun Phrase Chunks)")
print(nltk.RegexpParser("NP: {<DT>?<JJ>*<NN.*>+}").parse(tags))

ner = ne_chunk(tags)
print("\n(f) NAMED ENTITY RECOGNITION (NER)")
print(ner)
print("\nNamed Entities Found:")
for t in ner:
    if hasattr(t, 'label'):
        print(f"  {' '.join(w for w, _ in t.leaves()):<19}->  {t.label()}")

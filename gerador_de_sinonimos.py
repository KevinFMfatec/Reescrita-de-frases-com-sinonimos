import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
import random

nltk.download('punkt')
nltk.download('wordnet')

def get_most_similar_synonyms(word):
    most_similar_synonyms = set()
    max_similarity = -1
    
    synsets = wordnet.synsets(word, lang='por')
    if synsets:
        for synset in synsets:
            for lemma in synset.lemmas(lang='por'):
                for synset2 in wordnet.synsets(lemma.name(), lang='por'):
                    similarity = synset.wup_similarity(synset2)
                    if similarity is not None and similarity > max_similarity:
                        most_similar_synonyms.clear()
                        most_similar_synonyms.add(lemma.name())
                        max_similarity = similarity
                    elif similarity is not None and similarity == max_similarity:
                        most_similar_synonyms.add(lemma.name())
    return most_similar_synonyms

def replace_with_synonyms(sentence):
    tokens = word_tokenize(sentence, language='portuguese')
    replaced_sentence = []
    for token in tokens:
        synonyms = get_most_similar_synonyms(token)
        if synonyms and token.isalpha():
            synonym = random.choice(list(synonyms))  # Escolha aleatória de sinônimo
            if synonym != token:
                replaced_sentence.append(synonym)
            else:
                replaced_sentence.append(token)
        else:
            replaced_sentence.append(token)
    return ' '.join(replaced_sentence)

def main():
    sentence = input("Digite uma frase em português: ")
    new_sentence = replace_with_synonyms(sentence)
    print("Frase original:", sentence)
    print("Frase com sinônimos:", new_sentence)

if __name__ == "__main__":
    main()
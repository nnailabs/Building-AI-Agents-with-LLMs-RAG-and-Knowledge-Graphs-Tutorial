import numpy as np

def one_hot_encoding(sentence):
    words = sentence.lower().split()
    vocabulary = sorted(set(words))
    word_to_index = {
        word: i for i, word in enumerate(vocabulary)
    }
    one_hot_matrix = np.zeros((len(words), len(vocabulary)), dtype=int)
    for i, word in enumerate(words):
        one_hot_matrix[i, word_to_index[word]] = 1
    return one_hot_matrix, vocabulary

if __name__ == "__main__":
    sentence = "I love coding in Python and I love solving problems"
    one_hot_matrix, vocabulary = one_hot_encoding(sentence)
    print("Vocabulary:", vocabulary)
    print("One-Hot Encoded Matrix:\n", one_hot_matrix)
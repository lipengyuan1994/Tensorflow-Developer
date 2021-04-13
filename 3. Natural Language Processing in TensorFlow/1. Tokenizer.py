# import tensorflow as tf
# from tensorflow import keras
#
#
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
#
# sentences = [
#     'I love my dog',
#     'I love my cat',
#     'You love my dog!',
#     'Do you think my dog is amazing?'
# ]
#
# tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>")
# tokenizer.fit_on_texts(sentences)
# word_index = tokenizer.word_index
#
# sequences = tokenizer.texts_to_sequences(sentences)
#
# padded = pad_sequences(sequences, maxlen=5)
# print("\nWord Index = " , word_index)
# print("\nSequences = " , sequences)
# print("\nPadded Sequences:")
# print(padded)
#
#
# # Try with words that the tokenizer wasn't fit to
# test_data = [
#     'i really love my dog',
#     'my dog loves my manatee'
# ]
#
# test_seq = tokenizer.texts_to_sequences(test_data)
# print("\nTest Sequence = ", test_seq)
#
# padded = pad_sequences(test_seq, maxlen=10)
# print("\nPadded Test Sequence: ")
# print(padded)

# !wget - -no - check - certificate \
#     https: // storage.googleapis.com / laurencemoroney - blog.appspot.com / sarcasm.json \
#               - O / tmp / sarcasm.json

import json

with open("./tmp/sarcasm.json", 'r') as f:
    datastore = json.load(f)

sentences = []
labels = []
urls = []
for item in datastore:
    sentences.append(item['headline'])
    labels.append(item['is_sarcastic'])
    urls.append(item['article_link'])

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index
print(len(word_index))
print(word_index)
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, padding='post')
print(padded[0])
print(padded.shape)


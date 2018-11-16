import gensim

# Load Google's pre-trained Word2Vec model.
# model = gensim.models.Word2Vec.load_word2vec_format
model = gensim.models.KeyedVectors.load_word2vec_format('/home/mo/Google/GoogleNews-vectors-negative300.bin', binary=True)

print(model['new'])

print(model['york'])

# print(model.most_similar(positive='new'))

print('----')
print(model.most_similar(positive='New'))

print('----')
print(model.most_similar(positive='York'))

print('----')
print(model.most_similar(positive='New_York'))

print('----')
print(model.most_similar(positive=['New', 'York']))
# print(model['new york'])

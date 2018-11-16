from gensim.models import Word2Vec
from gensim.utils import tokenize
import glob
import matplotlib.pyplot as plt
# define training data




def _training():
    sentences = []
    files = sorted(glob.glob('/home/mo/word2vec_test/*.txt'))
    for file_ in files:
        print('processing '+file_)
        for line in open(file_):
            line = line.split('\n')[0]
            sentences.append( [i for i in tokenize(line)] )

            if 'new york' in line:
                line = line.replace('new york','new_york',-1)
                sentences.append( [i for i in tokenize(line)] )

            if 'los angeles' in line:
                line = line.replace('los angeles','los_angeles',-1)
                sentences.append( [i for i in tokenize(line)] )

            if 'san francisco' in line:
                line = line.replace('san francisco','san_francisco',-1)
                sentences.append( [i for i in tokenize(line)] )
        # break

    # train model
    print('training the model')
    model = Word2Vec(sentences, min_count=3)

    # summarize the loaded model
    print('finished training model')
    print(model)

    # summarize vocabulary
    # words = list(model.wv.vocab)
    # print(words)
    # access vector for one word
    print(model['new'])

    print('----')
    print(model.most_similar(positive='new'))

    print('----')
    print(model.most_similar(positive='york'))

    print('----')
    print(model.most_similar(positive='new_york'))

    print('----')
    print(model.most_similar(positive='los_angeles'))

    print('----')
    print(model.most_similar(positive='angeles'))

    print('----')
    print(model.most_similar(positive='london'))

    # save model
    model.save('wiki_model.bin')

def _loading():
    # # load model
    model = Word2Vec.load('wiki_model.bin')

    print('----')
    print(model.most_similar(positive='los_angeles'))

    print('----')
    print(model.most_similar(positive='angeles'))

    print('----')
    print(model.most_similar(positive='los'))

    for words in [['los','angeles']]:
        print('----')
        A = model[words[0]]
        print(A)

        print('----')
        B = model[words[1]]
        print(B)

        print('----')
        C = model[words[0]+'_'+words[1]]
        print(C)

        print()
        print('=-------------------------=')
        plt.plot(A)
        plt.plot(B)
        plt.plot(C)
        plt.show()


_loading()

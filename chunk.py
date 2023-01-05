import nltk
new="Open up your heart to Jesus-Let His Spirit enter in-And,forever,be your Saviour From life's struggles and their sins;Let Him true Companion"
print(new)
from nltk.word_tokenzied
new_token=nltk.word_tokenize(new)
print(new_token)
new_pos=nltk.pos_tag(new_token)
print(new_pos)
grammer="NP:[<DT>?<JJ>*<NN>]"
chunkParser=nltk.parse(grammer)
chunked=nltk.chunkParserparse(new)
print(chunked)
chunked.draw()
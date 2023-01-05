import nltk

new="Hi Good morning im Dona M Thomas.I come from vechoochira. i complete my degree. now i studying mca. "
print(new)
new_token=nltk.word_tokenize(new)
print(new_token)
new_pos=nltk.pos_tag(new_token)
print(new_pos)
grammer="NP:[<DT>?<JJ>*<NN>]"
chunkParser=nltk.parse(grammer)
chunked=nltk.chunkParserparse(new)
print(chunked)
chunked.draw()
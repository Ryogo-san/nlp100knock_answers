def ngram(n,lst):
    # [str[i:] for i in range(2)] -> ["I am an NLPer","am an NLPer"]
    # zip(*[str[i:] for i in range(2)]) -> zip("I am an NLPer","am an NLPer")
    return list(zip(*[lst[i:] for i in range(n)]))

s="I am an NLPer"
words_bi_gram=ngram(2,s.split())
chars_bi_gram=ngram(2,s)

print("単語bi-gram：",words_bi_gram)
print("文字bi-gram：",chars_bi_gram)
from nltk import ConditionalFreqDist, corpus

cfd = ConditionalFreqDist(
	(fileid, name[-1])
	for fileid in ['male.txt', 'female.txt']
	for name in corpus.names.words(fileid)
)

cfd.plot()

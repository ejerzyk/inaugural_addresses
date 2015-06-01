import json, sys, string
import matplotlib.pyplot as plt

top_word_num = 5

filename = 'items.json'
write_to = 'words.json'
stopwords_file = 'stopwords.csv'

stopwords = []

for line in open(stopwords_file):
	words = line.split(',')
	for word in words:
		stopwords = stopwords + [word]

words = {}

for line in open(filename):
	address = json.loads(line)
	if address['year'][0] != '' and address['text'] != '':
		year = int(address['year'][0].split(', ')[1].encode('utf-8'))
		text = address['text'].encode('utf-8').split(' ')
		for raw_word in text:
			word = raw_word.translate(None, string.punctuation).lower().strip()
			if word not in stopwords and word != '':
				if word in words:
					words[word]['num_times'] = words[word]['num_times'] + 1
					if year in words[word]['years']:
						words[word]['years'][year] = words[word]['years'][year] + 1
					else:
						words[word]['years'][year] = 1 
				else:
					map_to = {}
					map_to['num_times'] = 1
					map_to['years'] = {year : 1}
					words[word] = map_to

f = open(write_to, 'w')
f.write(json.dumps(words))
print "Presidents have used %d words, collectively." % len(words)
print "The top " + str(top_word_num) + " most frequently used words are:"
top_words = sorted(words, key=words.get, reverse=True)[:top_word_num]
for w in range(0,top_word_num):
	print str(w+1) + ". " + top_words[w] + " used " + str(words[top_words[w]]['num_times']) + " times."
	d = sorted(words[top_words[w]]['years'])
	x = []
	y = []
	for year in d:
		x = x + [year]
		y = y + [words[top_words[w]]['years'][year]]
	plt.plot(x, y)
	print x 
	print y
print top_words
print "Let me show you in this graph!"
plt.show()
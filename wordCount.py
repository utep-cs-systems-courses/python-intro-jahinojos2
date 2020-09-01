import sys        # command line arguments
import re         # regular expression tools
import os         # checking if file exists

if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

textFname = sys.argv[1]
outFname = sys.argv[2]

#make sure text files exist
if not os.path.exists(textFname):
    print ("text file input %s doesn't exist! Exiting" % textFname)
    exit()

file = open(textFname, 'rt')
text = file.read()
file.close()
text = text.lower()
words = re.split('\W+', text)

words_no_repeat = []

for i in words:
    if i not in words_no_repeat:
        words_no_repeat.append(i)

words_no_repeat.sort()

word_count = [0]*len(words_no_repeat)

for i in range(len(words_no_repeat)):
    for j in words:
        if words_no_repeat[i] == j:
            word_count[i]+=1


inputFile = open(outFname, 'w')
for i in range(len(words_no_repeat)):
    if words_no_repeat[i] != '':
        inputFile.write(words_no_repeat[i] + " " + str(word_count[i]) + "\n")

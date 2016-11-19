print " Welcome Pig Latin mates, have fun here"
pyg = 'ay'
original = raw_input("Enter a word mate:")
#check if there is a string and isalpha function checks if the text entered only contain alphabents not numbers
if len(original) > 0 and original.isalpha():
	print original
else:
	print "there is no word to translate"	
word = original.lower()
first = word[0]
new_word = word+first + pyg
new_word = new_word[1:len(new_word)]
print new_word
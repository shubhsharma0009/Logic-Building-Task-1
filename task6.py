sentence= input("Enter a sentence: ")
words= sentence.split(" ") 
print("The number of words in the sentence is: ", len(words))

unique_words= set(words)
print("The number of unique words in the sentence is: ", len(unique_words))
 
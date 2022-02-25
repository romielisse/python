#!/usr/bin/env python3

def get_sentences_from_file(filename):
    with open(filename) as file:
        text = file.read()    # read str from file
        
    sentences = text.split(".")   # convert str to list
    return sentences

def get_words_from_file(filename):
    with open(filename) as file:
        text = file.read()    # read str from file

    # print(text)
    text = text.replace("\n", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.lower()
    
    words = text.split(" ")   # convert str to list
    words.sort()
    # print(words)
    return words

def get_unique_words(words):
    unique_words = []
    unique_words.append(words[0])
    
    for i in range(1, len(words)):
        if words[i] == words[i - 1]:
            continue
        else:
            unique_words.append(words[i])            
    return unique_words

def main():
    filename = "gettysburg_address.txt"
    print("The Word Counter program\n")  

    # get sentences
    sentences = get_sentences_from_file(filename)
    
    # get words and unique words
    words = get_words_from_file(filename) # get list of words
    unique_words = get_unique_words(words)

    # display number of sentences, words, and unique words   
    print(f"Number of sentences = {len(sentences)}")
    print(f"Number of words = {len(words)}")
    print(f"Number of unique words = {len(unique_words)}")

    # display unique words and their word counts
    print("Unique word occurrences:")
    for word in unique_words:
        print(f"    {word} = {words.count(word)}")
 
if __name__ == "__main__":
    main()

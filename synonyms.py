'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    ''' This funciton returns the cosine similarity between the sparse vectors vec1 and vec2, stored as dictionaries
    Ex cosine_similarity({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}) shoulrd return approximately 0.70 (as a float)
    '''
    #Finds the magnituds each vector
    norm_vec1 = norm(vec1)
    norm_vec2 = norm(vec2)

    #Finds dot product of vec1_values * vec2_values
    dot_product = 0
    for key in vec1:
        if key in vec2:
            dot_product += vec1[key] * vec2[key]

    return dot_product / (norm_vec1 * norm_vec2)


def build_semantic_descriptors(sentences):
    '''
    Input: a list (sentences) which contains lists of strings (words)
    Returns: a dictionary (d) such for everery word (w) that appears in at least one of the sentences, d[w[ is iitself a dictionary which represents the semantic descriptor of (w)
    '''
    '''test:
[["i", "am", "a", "sick", "man"],
["i", "am", "a", "spiteful", "man"],
["i", "am", "an", "unattractive", "man"],
["i", "believe", "my", "liver", "is", "diseased"],
["however", "i", "know", "nothing", "at", "all", "about", "my",
"disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]
    '''
    #runtime analysis:
    # where k is the number of words in each sentence
    # runtime for each sentence 0(k^2 - k)/2)
    # runtime total = sum((k^2 - k)/2) accross all sentences

    d = {}

    #iterates through pairs of words in each sentence
    for sentence in sentences:
        for word_i_1 in range(len(sentence)):
            for word_i_2 in range(word_i_1 + 1, len(sentence)):

                #initialize words for easy reference
                word_1 = sentence[word_i_1]
                word_2 = sentence[word_i_2]

                #situation where both words have appeared before
                if word_1 in d and word_2 in d:
                    #situation where they have been in same sentence before
                    if word_2 in d[word_1]:
                        d[word_2][word_1] += 1
                        d[word_1][word_2] += 1
                    #situation where they have not been in same sentence before
                    else:
                        d[word_2][word_1] = 1
                        d[word_1][word_2] = 1

                #situation where only one word has appeared before
                elif word_1 in d:
                    d[word_1][word_2] = 1
                    d[word_2] = {word_1: 1}

                elif word_2 in d:
                    d[word_2][word_1] = 1
                    d[word_1] = {word_2: 1}

                #situation where neither words have appeared before
                else:
                    d[word_1] = {word_2: 1}
                    d[word_2] = {word_1: 1}

    return d

def build_semantic_descriptors_from_files(filenames):
    ''' Input: a list of filenames of strings, which containts the names of files
    Returns: a dictionary of semantic descriptors
    '''

    #A list containing sentences from all the files
    master_text = []

    for files in filenames:
        #makes the file into a list of strings which represent sentences
        #cleans up text by making letters lowercase and replacing punctuation
        text = open(files, "r", encoding = "latin1").read().lower().replace("!", ".").replace("?", ".").replace(",", " ").replace("-", " ").replace("--", " ").replace(":", " ").replace(";", " ").replace("\n", "").split(".")

        #splits each sentence up into its words individual words and appends to master_text
        for sentence in text:
            if sentence != "":
                master_text.append(sentence.replace(".","").split())

    return build_semantic_descriptors(master_text)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    '''Input: a string (word), a list of strings (choices), a dictionary (semantic_descriptors)
    Returns: the element of (choices) which has the largest semantic similarity to (word) with the semantic similarity computed uing the data in (semantic_descriptors) and the similarity function (similarity_fn)
    The similarity funciton is a function which takes in two sparse vectors stored as dicitonaries and returens a float'''
    similarity = -1
    chosen = choices[0]

    for word_choice in choices:

        if (word in semantic_descriptors) and (word_choice in semantic_descriptors):
            similarity_temp = similarity_fn(semantic_descriptors[word], semantic_descriptors[word_choice])
        else:
            similarity_temp = -1

        if similarity_temp > similarity:
            similarity = similarity_temp
            chosen = word_choice

    return chosen


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    '''Input: filename (string) --> the name of a file in the same format as test.txt
            semantic_discriptors --> dictionary of semantic descriptors made using build_semantic_descriptors_from_file
            similarity_fn --> function used for most_similar_word()

    Returns: percentage (float between 0.0 and 100.0) of questions for which most_similar_word() guesses the answer correctly '''

    text = open(filename, "r", encoding = "latin1").read().strip().split("\n")


    score = 0

    for line in text:
        line = line.split()

        word = line[0]
        answer = line[1]
        choices = line[2:]

        if most_similar_word(word, choices, semantic_descriptors, similarity_fn) == answer:
            score += 1

    return score/len(text) * 100

if __name__ == "__main__":
    f1 = open("text1.txt", "w")
    f2 = open("text2.txt", "w")
    f1.write("I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased.\n")
    f2.write("However, I know nothing at all about my disease, and do not know for certain what ails me.")
    f1.close()
    f2.close()
    sem_desc = build_semantic_descriptors_from_files(["text1.txt", "text2.txt"])

#sem = build_semantic_descriptors_from_files(["pride_and_prejudice.txt", "data2.txt", "text1.txt", "text2.txt", "war_and_peace.txt", "swann's_way.txt", "text_readability.txt"])
#run_similarity_test("testing.txt", sem, cosine_similarity)

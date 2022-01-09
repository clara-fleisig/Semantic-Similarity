# Semantic-Similarity
This project is an intelligent system that can learn to answer Test of English as a Foreign Language (TOEFL). The system approximates the semantic similarly (closeness of meaning) of words using data from english texts. 

## Describing the Problem
The program answers multiple choice questions of the form: given a word, _w_, find which word _s1, s2, s3, s4_ is a synonym of _w_.

## How it Works
The program computes the semantic similarities of _(w, s<sub>1</sub>), (w, s<sub>2</sub>), (w, s<sub>3</sub>), (w, s<sub>4</sub>)_ and choose the word whose similarity to _w_ is the highest.

To measure semantic similarity of pairs of words, the program computes a _semantic descriptor vector_ of each of the word, and then takes the similarity measure to be the _cosine similairty_ between the two vecotrs.

### Semantic Descriptor Vector
The semantic descriptor vector (_desc<sub>w</sub>_) of a word _w_, computed using a text with _n_ words denoted by (_w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>n</sub>)_ will have _n_-dimensions. The _i_-th coordinate of _desc<sub>w</sub>_ is the number of sentences in which both _w_ and _w<sub>i</sub>_ occur. In this program the semantic descriptor vector is sotred as a dicitonary, so that the zeros that correspond to words which don't co-occur with _w_ are not stored.

## Modules Used
`math`

## Files
* `synonyms.py`. A python file containning the program.
* `war_and_peace.txt` and `swann's_way.txt`. Contain works of english litterature in .txt format from http://www.gutenber.org, used to create sematic descriptor vectors
* `testing.txt`. A file where each line represents a TOEFL question. The first word on a line is the given word _w_, the second word is the answer to the TOEFL question and the remaining words in the line are the choices of possible synonyms.

## How to run the program
1. Build semantic descriptor vectors
    
In this example I build the semantic descriptor vectos using the _War and Peace_ and _Swann's Way_ texts, however this can be done using any english litterature text in the form of a `.txt` file.
```python:
sem = build_semantic_descriptors_from_files(["war_and_peace.txt", "swann's_way.txt"])
```
2. Identify which word is a synonym using semantic descriptor vectors
```
''' word --> a string, the word given in the question
choices  --> an array of strings, the options given in the question (one of which is a synonym of _w_)
sem --> a dictionary of dictionaries, which holds the semantic descriptor vectors as defined in 1.
cosine_similarity --> a funciton defined in the program for determining similarity of semantic descriptor vectors, do not vary this funciton argument
answer --> the string in choices which is synomous with _word_
'''

answer = most_similar_word(word, choices, sem, cosine_similarity)
```

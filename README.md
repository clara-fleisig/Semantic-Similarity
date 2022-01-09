# Semantic-Similarity
This project is an intelligent system that can learn to answer Test of English as a Foreign Language (TOEFL). The system approximates the semantic similarly (closeness of meaning) of words using data from english texts. 

## Modules
`math`

## Describing the Problem
The program answers multiple choice questions of the form: given a word, _w_, find which word _s1, s2, s3, s4_ is a synonym of _w_.

## How it Works
The program computes the semantic similarities of _(w, s<sub>1</sub>), (w, s<sub>2</sub>), (w, s<sub>3</sub>), (w, s<sub>4</sub>)_ and choose the word whose similarity to _w_ is the highest.

To measure semantic similarity of pairs of words, the program computes a _semantic descriptor vector_ of each of the words, and then takes the similarity measure to be the _cosine similairty_ between the two vecotrs.

The semantic descriptor vector (_desc<sub>w</sub>_) of a word _w_, computed using a text with _n_ words denoted by (_w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>n</sub>)_ will have _n_-dimensions. The _i_-th coordinate of _desc<sub>w</sub>_ is the number of sentences in which both _w_ and _w<sub>i</sub>_ occur. In this program the semantic descriptor vector is sotred as a dicitonary, so that the zeros that correspond to words which don't co-occur with _w_ are not stored.


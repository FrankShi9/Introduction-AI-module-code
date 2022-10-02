# Degree module Introduction to AI course assignment code

## Description

### AS1
Introduction:
In the problem, we are given a two-dimensional 100x6 array stored in a .csv 
file, where each row represents an instance (or object). For each row, the 
first 5 columns are the attributes of the instance and the final column is the 
label of the instance such as:
a0, a1, a2, a3, a4, l
The following are the task specifications:
• Read the text file and parse its content into a matrix.
• Compute the prior probabilities p(l = 0) and p(l = 1)
• Compute the conditional probabilities p(ai = 0|l = 0), i = 0, 1, 2, 3, 4 
and p(ai = 1|l = 0), i = 0, 1, 2, 3, 4, p(ai = 0|l = 1), i = 0, 1, 2, 3, 4 and 
p(ai = 1|l = 1), i = 0, 1, 2, 3, 4
This report proposes a solution through loading data into a 2-D NumPy int 
ndarray via csv.reader function provided in Python csv library and using 
brute force linear search method to traverse the ndarray to derive the 
count and use divisions to calculate probabilities. In addition, dynamic 
programming techniques are employed to store the frequently used #{l = 0} 
and #{l = 1} in a bid to reduce the time overhead.

### AS2
Introduction
Text categorization is focused on classifying a set of documents into categories of 
predefined labels. Texts cannot be directly handled by our model. The indexing 
procedure is the first step that maps a text dj into a numeric representation during the 
training and validation. The standard TFIDF function is used to represent the text. The 
unique words from English vocabulary are represented as a dimension of the dataset.
We are given a dataset with 5 labels (folders) consisting 2726 data files in total each after 
Latin-1 decoding presents some written words in email communications, for instance.
Problem:
1.Preprocessing
➢ Read the text files from 5 subdirectories in dataset and split the document text 
into words (splitting separator is non-alphabet letters).
➢ Remove the stopwords from the text collections, which are frequent words that 
carry no information. Stopwords list are given in the file stopwords.txt. Convert all 
words into their lower case form. Delete all non-alphabet characters from the text.
➢ Perform word stemming to remove the word suffix.
TFIDF representation 
![image](https://user-images.githubusercontent.com/53264047/193474428-f04dcf3f-a7e8-4ccc-9784-337ce4aa0b14.png)

## Getting Started

### Dependencies

* numpy
* codecs
* ntlk
* hashlib
* flask

## License

This project is licensed under the GNU License - see the LICENSE.md file for details

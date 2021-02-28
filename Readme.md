# Information Retrieval Assignment 1

Team: [Sandeep](), [Sajeel](https://github.com/khansajeel), [Shekhar](https://github.com/24sharkS), [Nischal](https://github.com/nischal18350), [Devender](https://github.com/DS-654)
## Directory Structure

 - [stories](stories)				# Contains all files that needs to be indexed 
 - [main.ipynb](main.ipynb)			# Inverted Index creation code
 - [mapping.json](mapping.json) 		# Mapping of document ID with document location
 - [output.json](output.json)			# Inverted Index i.e terms with list of DocID containing them
 - [requirements.txt](requirements.txt) 	# Libraries required for running this project 


## Methodology
- The list containing all file names is stored in a file.
- Then preprocessing is done for data of each file.
	- Most of the files were decoded using "utf-8" codec while for some "unicode_escape" was used.
- Finally, inverted index was generated using all the words and cached in a file.

### Query
The logical operations on query keywords were performed as follows:
- **OR** -> set union
- **AND** -> set intersection
- **NOT** -> set difference

### Number of Comparisons
We take the  posting lists corresponding to the two keywords and then simply compute the number of comparisons by traversing till we encounter the end of any one list.

For each input query, we first perform preprocessing then extracted keywords are stored in a list. From left to right, we perform operations on two words, save the results and use it in further computations.

### Result
From the input query, we retrieve the total number of relevant documents and the minimum number of comparisons. Both document name and the associated ID are retrieved.

## Preprocessing Steps
- Text conversion to lowercase.
- Tokenization using nltk.
- Removal of stop words using nltk.
- Special characters excluding alphanumeric are removed.
- All singly occuring characters are removed.
- Finally a set of all the words is created.

## Assumptions
- Input Query is case insensitive.
- We retrieve the results from the unstemmed query keywords. At demo it can be also be presented for stemmed keywords.

# Part 1:  Calculate the frequency of a term in each document

### Notes
* The mapper reads the files in the `inputDirectory` directory
* mapper.py and reducer.py are written in python Python 2.6.6.
* To test the mapper and reducer using pipes use:  
` python2 mapper.py | sort | python2 reducer.py `

### MR Input & Output
* **Input**  
The input of this MapReducer is the files located in the `inputDirectory` directory. The mapper reads the contents of every file line by line. The mapper does not recieve anything from STDIN.

* **Output**  
The output of this MapReducer is a list of pairs in the following form:  
` ((term, document identifier), count) `

* **Example** 
If we have two files `1.txt` and `2.txt` in our `inputDirectory` and the content of each file is as follows:  
`1.txt : "hello hello"`  
`2.txt : "hi"`  
The mapper will read these files and emit the following pairs:  
`(hello 1.txt   1)`  
`(hello 1.txt   1)`  
`(hi 2.txt   1)`  
The reducer will recieve these pairs as input through STDIN and emit:  
`((hello 1.txt), 2)`  
`((hi 2.txt), 1)`
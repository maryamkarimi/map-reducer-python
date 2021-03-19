# Part 2: Count Bigrams

### Notes
* This MR counts the number of bigrams in a single document.
* mapper.py and reducer.py are written in Python 2.6.6.
* To test the mapper and reducer using pipes use:  
  * `cat doc.txt | python2 mapper.py | sort | python2 reducer.py`  
or   
  * `echo "hello hi hello hi hello" | python2 mapper.py | sort | python2 reducer.py`

### MR Input & Output
* **Input**  
The input of this MapReducer comes from STDIN (standard input). When using pipes, this can be done using either `cat` or `echo`.  
In Hadoop, when we run the following script we specify the name of the file/directory for input (notice `"-input  $INPUT"`): 
  ``` hadoop jar $STREAMJAR \
   -file  $CODE_DIR/mapper.py -mapper mapper.py  \
   -file  $CODE_DIR/reducer.py -reducer reducer.py  \
   -input  $INPUT \
   -output $OUTPUT
  ```  
  So the input is lines of our document.

* **Output**  
The output of this MapReducer is a list of pairs in the following form:  
` (bigram, frequency) `  
where bigram is a bigram that exists in our document and frequency is the number of times it appears in the document.

* **Example** 
If we have a file with the following content: `"hello hi hello hi"`  
The mapper will read the content of this file and emit the following pairs:  
`(hello hi   1)`  
`(hi hello   1)`  
`(hello hi   1)`  
The reducer will recieve these pairs as input through STDIN and emit:  
`(hello hi, 2)`  
`(hi hello, 1)`

### Instructions to run in Hadoop
See runMR.sh
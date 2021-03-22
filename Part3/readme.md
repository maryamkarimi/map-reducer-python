# Part 3: Count Unique Bigrams

## **Notes**
* This solution consists of two mapReducers.
* The first MR counts the frequency of every bigram in a single document.
* The second MR receives the output of first MR as input and counts the total number of bigrams that only appear once in a document.
* All the code is written in Python 2.6.6.
* To test the mappers and reducers using pipes use:

  ``` 
  cat doc.txt | python2 mapper1.py | sort | python2 reducer1.py | python2 mapper2.py | sort | python2 reducer2.py
  ```  
  or  

  ```
  echo "hello hi hello hi" | python2 mapper1.py | sort | python2 reducer1.py | python2 mapper2.py | sort | python2 reducer2.py
  ```

## **MR Input & Output**
* **MapReducer 1**

  * **Input:**
  The input of the first MapReducer comes from STDIN (standard input). When using pipes, this can be done using either `cat` or `echo`.  
  In Hadoop, when we run the following script we specify the name of the file/directory for input (notice `"-input  $INPUT"`): 
     ``` hadoop jar $STREAMJAR \
     -file  $CODE_DIR/mapper1.py -mapper mapper1.py  \
     -file  $CODE_DIR/reducer1.py -reducer reducer1.py  \
     -input  $INPUT \
     -output $OUTPUT
     ```  
     So the input is lines of our document.

  * **Output:**  
  The output of the first MapReducer is a list of pairs in the following form:  
  `bigram   frequency`  
  where bigram is a bigram that exists in our document and frequency is the number of times it appears in the document.

* **MapReducer 2**
  * **Input:**
  The input of this MR is the output of the first MR, which consists of a list of pairs in the following form:  
  `bigram   frequency` 

  * **Output:** 
  The output of the second MR is a single number representing the total number of unique bigrams in a single document.

* **Example**  
If we have a file with the following content: `"hello hi hello hi"`  

  **Mapper 1** will read the content of this file and emit the following pairs:  
  `(hello hi   1)`  
  `(hi hello   1)`  
  `(hello hi   1)`  

  **Reducer 1** will receive these pairs (sorted) as input through STDIN and emit:  
  `(hello hi, 2)`  
  `(hi hello, 1)`  

  Then, **Mapper 2** will check the counts in these pairs and for every pair with count set to 1, emit: `1`

  Finally, **Reducer 2** will add up all the `1`s it receives and emit the total count.

## **Hadoop Instructions**
See runMR.sh
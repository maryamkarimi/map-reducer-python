# Part 1:  Calculate the frequency of a term in each document

## Notes
* The mapper reads the files in the `Documents` directory
* All the code is in Python 2.6.6.
* This solution consists of three mapReducers.
* MR 1 reads the content of all the files and calculates the tf for every term and document.
* MR 2 calculates the df of every term.
* MR 3 calculates the idf and tf-idf.
* To test the mapper and reducer using pipes use:  
    ```
    python2 mapper1.py | sort | python2 reducer1.py | python2 mapper2.py | sort | python2 reducer2.py | python2 mapper3.py | sort | python2 reducer3.py
    ```


## MR Input & Output
* **MapReducer 1**

  MapReducer 1 Calculates tf for every term and doc.
  * **Input:**  
  The input of MR 1 is the files located in the `Documents` directory. The mapper reads the contents of every file line by line. The mapper does not receive anything from STDIN.
  
  * **Output**  
  The output of MR 1 is a list of pairs in the following form:`doc_identifier term    tf`

* **MapReducer 2**

  MapReducer 2 Calculates df for every term.
  * **Input:**  
  The input of MR 2 is the output of MR 1 which is a sorted list of pairs in the following form: `doc_identifier term    tf`
  
  * **Output**  
  The output of MR 2 is a list of pairs in the following form: `term doc_identifier tf   df`

* **MapReducer 3**

  MapReducer 3 Calculates idf for every term and tf-idf for every term in a document.
  * **Input:**  
  The input of MR 3 is the output of MR 2 which is a sorted list of pairs in the following form: `term doc_identifier tf   df`
  
  * **Output**  
  The output of MR 3 is a list of pairs in the following form: `((term doc_identifier), (tf idf tf-idf))`

* **Example**   
If we have three files `1.txt`, `2.txt`, and `3.txt` in our `Documents` and the content of each file is as follows:  
`1.txt : "This movie is very scary and long"`  
`2.txt : "This movie is not scary and is slow"`
`3.txt : "This movie is spooky and good"`  

  **Mapper 1** will read these files and emit the following pairs:  
  `(1.txt and	     1)`  
  `(1.txt is	     1)`  
  `(1.txt long	 1)`  
  `(1.txt movie	 1)`  
  `(1.txt scary	 1)`  
  `(1.txt This	 1)`  
  `(1.txt very	 1)`  
  `(2.txt and	     1)`  
  `(2.txt is	     1)`  
  `(2.txt is    	 1)`  
  `(2.txt movie	 1)`  
  `(2.txt not  	 1)`  
  `(2.txt scary	 1)`  
  `(2.txt slow	 1)`  
  `(2.txt This	 1)`  
  `(3.txt and 	 1)`  
  `(3.txt good	 1)`  
  `(3.txt is  	 1)`  
  `(3.txt movie	 1)`  
  `(3.txt spooky	 1)`  
  `(3.txt This	 1)`  

  **Reducer 1** will receive the above pairs as input through STDIN, calculate the tf of every term and document and emit:  
  `(1.txt and 	0.142857142857)`  
  `(1.txt is 	0.142857142857)`  
  `(1.txt long  	0.142857142857)`  
  `(1.txt movie	 0.142857142857)`  
  `(1.txt scary 	0.142857142857)`  
  `(1.txt This	 0.142857142857)`  
  `(1.txt very 	0.142857142857)`  
  `(2.txt and	 0.125)`  
  `(2.txt is 	0.25)`  
  `(2.txt movie	 0.125)`  
  `(2.txt not	 0.125)`  
  `(2.txt scary 	0.125)`  
  `(2.txt slow	 0.125)`  
  `(2.txt This 	0.125)`  
  `(3.txt and 	0.166666666667)`  
  `(3.txt good 	0.166666666667)`  
  `(3.txt is 	 0.166666666667)`  
  `(3.txt movie 	0.166666666667)`  
  `(3.txt spooky 	0.166666666667)`  
  `(3.txt This 	0.166666666667)`

  **Mapper 2** will receive the above pairs and simply flip the order of document identifier and term. This will ensure pairs will get sorted by term as key which is needed for the next reducer to be able to calculate df of every term.


  **Reducer 2** will receive the above pairs and calculates df of every term and emit:   
  `term doc_identifier tf  df`  

  `(and 1.txt 0.142857142857 	3)`  
  `(and 2.txt 0.125	 3)`  
  `(and 3.txt 0.166666666667	 3)`  
  `(good 3.txt 0.166666666667	 1)`  
  `(is 1.txt 0.142857142857	 3)`  
  `(is 2.txt 0.25	 3)`  
  `(is 3.txt 0.166666666667	 3)`  
  `(long 1.txt 0.142857142857	 1)`  
  `(movie 1.txt 0.142857142857	 3)`  
  `(movie 2.txt 0.125	 3)`  
  `(movie 3.txt 0.166666666667 	3)`  
  `(not 2.txt 0.125	 1)`  
  `(scary 1.txt 0.142857142857 	2)`  
  `(scary 2.txt 0.125	 2)`  
  `(slow 2.txt 0.125	 1)`  
  `(spooky 3.txt 0.166666666667	 1)`  
  `(This 1.txt 0.142857142857 	3)`  
  `(This 2.txt 0.125	 3)`  
  `(This 3.txt 0.166666666667 	3)`  
  `(very 1.txt 0.142857142857	 1)`

  **Mapper 3** will receive the above pairs and simply flip the order of document identifier and term. This will ensure pairs will get sorted by doc as key which is needed for the next reducer to be able to calculate the total number of documents in the corpus.

  **Reducer 3** receives the above pairs and calculates idf and tf-idf. It will emit the following pairs:  
  `((term doc_identifier), (tf idf tf-idf))`  

  `((1.txt, and), (0.142857142857, 0.0, 0.0))`  
  `((1.txt, is), (0.142857142857, 0.0, 0.0))`  
  `((1.txt, long), (0.142857142857, 0.47712125472, 0.0681601792456))`  
  `((1.txt, movie), (0.142857142857, 0.0, 0.0))`  
  `((1.txt, scary), (0.142857142857, 0.176091259056, 0.0251558941508))`  
  `((1.txt, This), (0.142857142857, 0.0, 0.0))`  
  `((1.txt, very), (0.142857142857, 0.47712125472, 0.0681601792456))`  
  `((2.txt, and), (0.125, 0.0, 0.0))`  
  `((2.txt, is), (0.25, 0.0, 0.0))`  
  `((2.txt, movie), (0.125, 0.0, 0.0))`  
  `((2.txt, not), (0.125, 0.47712125472, 0.05964015684))`  
  `((2.txt, scary), (0.125, 0.176091259056, 0.022011407382))`  
  `((2.txt, slow), (0.125, 0.47712125472, 0.05964015684))`  
  `((2.txt, This), (0.125, 0.0, 0.0))`  
  `((3.txt, and), (0.166666666667, 0.0, 0.0))`  
  `((3.txt, good), (0.166666666667, 0.47712125472, 0.0795202091201))`  
  `((3.txt, is), (0.166666666667, 0.0, 0.0))`  
  `((3.txt, movie), (0.166666666667, 0.0, 0.0))`  
  `((3.txt, spooky), (0.166666666667, 0.47712125472, 0.0795202091201))`  
  `((3.txt, This), (0.166666666667, 0.0, 0.0))`
#!/bin/sh

# Path of Hadoop streaming JAR library
STREAMJAR=/usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar

# Directory that input & output of first mapReducer are stored into
INPUT1=/user/cloudera/input1
OUTPUT1=/user/cloudera/output1

# Create input directory
hadoop fs -mkdir $INPUT1
# Create the test file and move it to input directory
echo "hello hi hello hi" > doc.txt
hadoop fs -copyFromLocal doc.txt $INPUT1/doc.txt

CODE_DIR=/home/cloudera/asn2

hadoop fs -rm -f -r $OUTPUT1

hadoop jar $STREAMJAR \
   -file  $CODE_DIR/mapper1.py -mapper mapper1.py  \
   -file  $CODE_DIR/reducer1.py -reducer reducer1.py  \
   -input  $INPUT1 \
   -output $OUTPUT1


# Directory that input & output of second mapReducer are stored into
INPUT2=/user/cloudera/input2
OUTPUT2=/user/cloudera/output2

# Create input directory
hadoop fs -mkdir $INPUT2
# Merge the results from the first MapReducer and move to input2 directory
hadoop fs -getmerge $OUTPUT1/* outputFile
hadoop fs -copyFromLocal outputFile $INPUT2/outputFile

hadoop fs -rm -f -r $OUTPUT2

hadoop jar $STREAMJAR \
   -file  $CODE_DIR/mapper2.py -mapper mapper2.py  \
   -file  $CODE_DIR/reducer2.py -reducer reducer2.py  \
   -input  $INPUT2 \
   -output $OUTPUT2

# See the results
hadoop fs -cat $OUTPUT2/part-00000
#!/bin/sh

# Path of Hadoop streaming JAR library
STREAMJAR=/usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.6.0-mr1-cdh5.12.0.jar

#Directory that input & output are stored into
INPUT=/user/cloudera/input
OUTPUT=/user/cloudera/output

# Create input directory
hadoop fs -mkdir $INPUT
# Create the test file and move it to input directory
echo "hello hi hello hi" > doc.txt
hadoop fs -copyFromLocal doc.txt $INPUT/doc.txt

CODE_DIR=/home/cloudera/asn2

hadoop fs -rm -f -r $OUTPUT

hadoop jar $STREAMJAR \
   -file  $CODE_DIR/mapper.py -mapper mapper.py  \
   -file  $CODE_DIR/reducer.py -reducer reducer.py  \
   -input  $INPUT \
   -output $OUTPUT

#Use this by running it on a particular (available) port, say 1234
#in another terminal on the same machine, run 
#nc -l portnumber
#Then anything you type in the terminal running nc will have wordcount run on it

from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext

def main(port):
    conf = SparkConf().setAppName("netcount")
    sc = SparkContext(conf=conf)
    ssc = StreamingContext(sc, 1)

    word_counts = ssc.socketTextStream("localhost", port) \
                     .flatMap(lambda line: line.split(" ")) \
                     .map(lambda x: (x, 1)) \
                     .reduceByKey(lambda x, y: x + y)

    word_counts.pprint()

    ssc.start()
    ssc.awaitTermination()

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Must specify port to listen to.")
        sys.exit(1)

    main(int(sys.argv[1]))

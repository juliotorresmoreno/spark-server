
## Spark Application - execute with spark-submit

## Imports
from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext

## Module Constants
APP_NAME = "Spark Application"

## Main functionality

def inicialize():
    conf = SparkConf().setMaster("local[*]")
    conf = conf.setAppName(APP_NAME)
    sc   = SparkContext(conf=conf).getOrCreate()

    return HiveContext(sc)
import re
import xml.etree.ElementTree as ET
from numpy import array
from math import sqrt
import random

from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

langDict = {'javascript': 0, 'java': 1, 'php': 2, 'python': 3, 'c#': 4, 'c++': 5, 'ruby': 6, 'css': 7, 'objective-c': 8, 'perl': 9, 'scala': 10, 'haskell': 11, 'matlab': 12, 'clojure': 13, 'groovy': 14, 'html': 15, 'r': 16, 'asp.net': 17}
LANG_DISTANCE = 1000000
CLUSTERS_NUMBER = 40

conf = SparkConf().setAppName("Large-Scale Clustering")
sc = SparkContext(conf=conf)
sqlCtx = SQLContext(sc)

def hasTags( xmlStr ):
    try:
        xmlObj = ET.fromstring(xmlStr)
        if 'Tags' in xmlObj.attrib:
            return True
    except:
        return False


def hasLangTags( xmlStr ):
    try:
        xmlObj = ET.fromstring(xmlStr)
        if 'Tags' in xmlObj.attrib:
            tags = ET.fromstring(xmlStr).attrib['Tags']
            tags = re.split('>',tags)
            for tag in tags:
                tag = tag.replace('<', '').lower()
                return tag in langDict
        else:
            return False
    except:
        return False


def is_valid_post_record( xmlStr ):
    try:
        xmlObj = ET.fromstring(xmlStr)
        return ('ViewCount' in xmlObj.attrib or 'AnswerCount' in xmlObj.attrib or 'CommentCount' in xmlObj.attrib or 'FavoriteCount' in xmlObj.attrib) and 'Tags' in xmlObj.attrib
    except:
        return False


def is_valid_question_record( xmlStr ):
    try:
        xmlObj = ET.fromstring(xmlStr)
        return 'PostTypeId' in xmlObj.attrib and xmlObj.attrib['PostTypeId'] == '1' and 'Tags' in xmlObj.attrib
    except:
        return False


def getKmeans_activity_vector(xmlStr):
    xmlObj = ET.fromstring(xmlStr)
    if 'ViewCount' not in xmlObj.attrib:
        viewCount = 0
    else:
        viewCount = int(xmlObj.attrib['ViewCount'])

    if 'CommentCount' not in xmlObj.attrib:
        commentCount = 0
    else:
        commentCount = int(xmlObj.attrib['CommentCount'])

    if 'FavoriteCount' not in xmlObj.attrib:
        favoriteCount = 0
    else:
        favoriteCount = int(xmlObj.attrib['FavoriteCount'])

    activity = viewCount + commentCount + favoriteCount

    tags = xmlObj.attrib['Tags']
    tags = re.split('>', tags)
    for tag in tags:
        tag = tag.replace('<', '')
        if tag in langDict:
            return array([langDict[tag] * LANG_DISTANCE, activity])

records = sc.textFile("/data/stackOverflow2017")

# FILTERING STAGE
posts = records.filter(lambda data: is_valid_post_record(data) and hasLangTags(data))
questions = records.filter(lambda data: is_valid_question_record(data) and hasLangTags(data))

# MAPPING STAGE
activity_vector = posts.map(getKmeans_activity_vector)

# K-MEANS STAGE
activity_clusters = KMeans.train(activity_vector, CLUSTERS_NUMBER, maxIterations=10, initializationMode="random")

# PLOTTING STAGE
def get_plot_data ( input_data , kmeans_model):
    result = kmeans_model.predict(input_data)
    return [input_data, result]

plot_activity_data = activity_vector.map(lambda data : get_plot_data(data, activity_clusters))

plot_activity_data.saveAsTextFile('dataPlotLanguage')

"""
CsvToDataframeApp.py - CSV ingestion in a dataframe.

"""
import findspark
from pyspark.sql import SparkSession

findspark.init()

absolute_file_path = "file:///Users/ashujha/Data/issue_export_dataframe.csv"
spark = SparkSession.builder.appName("CSV to Dataset").master("local[*]").getOrCreate()


def extract_data():
    """Load data from Parquet file format.
    :param spark: Spark session object.
    :return: Spark DataFrame.
    """
    df = (
        spark
            .read
            .csv(header=True, inferSchema=True, path=absolute_file_path))

    df.show(5)
    return df

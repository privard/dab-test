from shared_lib import my_module


def main():
    spark = my_module.get_spark()
    df = spark.createDataFrame([(1, 2), (3, 4)], schema="a int, b int")
    df.show()


if __name__ == "__main__":
    main()

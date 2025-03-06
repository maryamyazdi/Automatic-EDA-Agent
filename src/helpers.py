import pandas as pd


def get_df_info(df: pd.DataFrame) -> str:
    """
    Returns the columns and respective data types of the given dataframe as string.

    :param df: dataframe to get its info
    :return:
    """
    info = [f"{col_name}: {dtype}" for col_name, dtype in df.dtypes.items()]
    return "\n".join(info)


def code_extractor(python_code: str) -> str:
    """
    Extracts raw python code from gpt response, removing additional unnecessary characters or formatting.

    :param python_code: gpt response containing python code
    :return:
    """
    if "```" in python_code:
        python_code = python_code.split("```")[1]
    if "python" in python_code:
        python_code = python_code.split("python")[1]

    # since TabularData.data is already read from csv/xlsx, no need to repeat read_csv in the code
    python_code = "\n".join(
        [line for line in python_code.split("\n") if "read_csv" not in line]
    )
    return python_code

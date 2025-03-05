generate_code_prompt = """I have a pandas dataframe with the following columns and corresponding data types:
{df_info}

I want to {analysis} in a {manner} manner. Write the python code to {analysis} in a {manner} manner.

ATTENTION:
- Do not plot any data.
- Output only the python code without any extra text.
- If the output contains tabular data, separate each row and column with "|" when printing.
"""

explain_output_prompt = """I have a pandas dataframe with the following columns and corresponding data type:
{df_info}

On this dataframe, I wanted to {analysis} in a {manner} manner. I ran a python code consisting some dataframe analytics (exploratory data analysis, statistical analysis, etc.). Using the outputs of the python code, I want you to explain and interpreter the output/provided statistical results in a {manner} manner in 3 paragraphs.
What do you understand from these results?
Remember to keep your explanation concise and insightful within maximum 3 paragraphs, avoid any exaggeration or uncertain interpretations. Write the explanation in passive voice.

Here is the outputs of the python code:
{statistics}
"""

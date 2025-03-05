visualizer_prompt = """I have a pandas dataframe with the following columns and corresponding data type:
{df_info}

Write python code to generate visualizations and plots in order to {analysis}. The plot or plots should have relevant titles.
Only output the python code. Do not output anything other than python code.
"""

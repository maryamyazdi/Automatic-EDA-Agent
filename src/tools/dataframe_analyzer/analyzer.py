import os
from contextlib import redirect_stdout
from src.helpers import *
from src.tools.dataframe_analyzer.prompts import *
from src.openai_client import ask_gpt

class DataAnalyzer:
    description = "Use this tool when you need to interpret or analyze any tabular data in form of a pandas dataframe with a certain goal."

    def __init__(self):
        self.df = None
        self.df_info = None

    def run(self, df, analysis, complexity="simple"):
        self.df = df
        self.df_info = get_df_info(df)

        for attempt in range(3):
            try:
                python_code = ask_gpt(
                    [generate_code_prompt.format(df_info=self.df_info, analysis=analysis, manner=complexity)]
                )["result"]
                python_code = code_extractor(python_code)

                # Capture execution output
                output_buffer = io.StringIO()
                with redirect_stdout(output_buffer):
                    exec(python_code)
                code_output = output_buffer.getvalue()

                # Generate final analysis
                output_query = explain_output_prompt.format(
                    df_info=self.df_info, analysis=analysis, manner=complexity, statistics=code_output
                )
                final_analysis = ask_gpt([output_query], system_role="You are a brilliant data analyst.")["result"]

                return f"- Statistical Analysis:\n{code_output}\n\n- Interpretation:\n{final_analysis}"

            except TimeoutError:
                print(f"Attempt {attempt + 1} failed due to TimeoutError. Retrying...")

        return "Analysis failed after multiple attempts."


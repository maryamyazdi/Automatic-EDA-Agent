import pandas as pd

from src.tools.dataframe_visualizer.prompts import *
from src.helpers import *
from src.openai_client import ask_gpt


def create_global_var(var):
    global df
    df = var


class VisualizeOutput:
    def __init__(self, python_code):
        python_code = "\n".join(
            [line for line in python_code.split("\n") if "plt.show()" not in line]
        )
        self.python_code = python_code

    def __call__(self):
        return self.python_code

    def show(self):
        exec(self.python_code + "\nplt.show()")

    def save(self, path):
        exec(self.python_code + f'\nplt.savefig(fname="{path}")')


class DataVisualizer:
    description = "Use this tool when you want to make visualizations."

    def __init__(self):
        self.df = None
        self.df_info = None

    def run(self, df: pd.DataFrame, analysis: str):
        self.df = df
        self.df_info = get_df_info(df)
        # When called from other modules needs to be global
        create_global_var(df)

        prompt = visualizer_prompt.format(
            df_info=self.df_info,
            analysis=analysis,
        )
        python_code = ask_gpt([prompt])["result"]
        python_code = code_extractor(python_code)
        for _ in range(3):
            output = VisualizeOutput(python_code)
            try:
                output.show()
                return output
            except:
                print("Process failed with TimeoutError.")
                python_code = ask_gpt([prompt])["result"]
                python_code = code_extractor(python_code)


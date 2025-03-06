import re

from src.types import TabularData
from src.bot.prompts import *
from src.openai_client import ask_gpt
from src.helpers import *
from src.tools import all_tools
from src.tools import DataAnalyzer, DataVisualizer


class Agent:
    def __init__(self, path: str):
        self.df = TabularData(path=path)
        print(f"Data loaded!")
        self.df_info = get_df_info(self.df.data)
        self.user_query = None
        self.tasks = None
        self.analyzer = DataAnalyzer()
        self.visualizer = DataVisualizer()

    def generate_tasks(self):
        print(f"Processing the query...")
        self.tasks = ask_gpt(
            prompts=[
                generate_tasks_prompt.format(
                    user_query=self.user_query, df_info=self.df_info
                )
            ],
            version="gpt-4",
            system_role="You are very smart data scientist.",
        )["result"]

    def get_available_tools(self):
        return "\n".join([f"{tool.__name__}: {tool.description}" for tool in all_tools])

    def execute_tasks(self):
        self.tasks = re.findall(r"Task number \d+:\n\s+- Description: (.*)", self.tasks)
        for task_num, task in enumerate(self.tasks):
            print(f"\n#####\n - Task {task_num + 1}/{len(self.tasks)}:", task)
            tool = ask_gpt(
                [
                    select_tool_prompt.format(
                        df_info=self.df_info,
                        task=task,
                        tools=self.get_available_tools(),
                    )
                ]
            )["result"]
            print(" - Tool:", tool)
            if tool == "DataAnalyzer":
                result = self.analyzer.run(df=self.df.data, analysis=task)
                print(result)
            if tool == "DataVisualizer":
                result = self.visualizer.run(df=self.df.data, analysis=task)
                print(result)

    def process_query(self, user_query: str):
        self.user_query = user_query
        self.generate_tasks()
        self.execute_tasks()

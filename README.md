# Exploratory Data Analysis (EDA) Agent

This agent helps you better understand your dataset! It performs exploratory data analysis (EDA) on your data and provides insightful information using statistical summaries, visualizations, and AI-driven interpretations of your data.

If you have a specific query, this agent also helps you run it comprehensively. You can see the step-by-step results satisfying different requirements of your query.

## Steps to run the project:
- Setting up the environment:
  
  - `cd` to the project directory
    ```
    cd path/to/the/project/folder
    ```
  - Checkout/switch the `master` branch locally
    ```
    git checkout master
    ```
  - Create an environment (if did not before) and activate it
  -  Install the requirements in the active environment
      ```
      pip install -r requirements.txt
      ```
- Running the test notebook:
  
  - Run jupyter notebook in the active environment
    ```
    jupyter notebook
    ```
  - In jupyter, open `tests/test_agent.ipynb` ([this file](https://github.com/maryamyazdi/Automatic-EDA-Agent/blob/master/tests/test_agent.ipynb)) and observe how it works on sample datasets.

  - To test the agent on your own dataset, replace the placeholders in the cell below and copy/paste the third cell in the `tests/test_agent.ipynb` notebook.
    ```python
    agent = Agent(path='[path/to/your/local/dataset]')  # currently supporting .xlcx and .csv files
    
    query = """[informaton about the dataset (optional) and your desired analyses]
    """
    
    agent.process_query(user_query=query)
    ```
  - Run the cell and see the results being produced per each task

## Project structure:
```
src/
├── __init__.py
├── agent/
│   ├── prompts.py
│   └── EDA_agent.py
├── tools/
│   ├── __init__.py
│   ├── dataframe_nalyzer/
│   │   ├── analyzer.py
│   │   └── prompts.py
│   └── dataframe_visualizer/
│       ├── visualizer.py
│       └── prompts.py
├── data_types/
│   ├── __init__.py
│   └── tabular.py
├── helpers.py
├──openai_client.py
│
tests/
└── test_agent.ipynb
```
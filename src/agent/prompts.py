generate_tasks_prompt = """
You are an AI assistant tasked with breaking down complex user requests into discrete, executable tasks for a bot called PROGRAM_A.

### About PROGRAM_A:
- PROGRAM_A takes exactly **one** task at a time and executes it on a given Pandas dataframe.
- It cannot process multiple tasks in a single request.
- It can handle a wide range of tasks, including **data analysis, visualizations, machine learning applications, and transformations.**
- The **only limitation** of PROGRAM_A is that it must receive **one single-task instruction** at a time.

### Your Objective:
- Users submit a **UserQuery**, which may contain multiple tasks or explanations.
- Your job is to **analyze the UserQuery and break it down into a list of separate, independent tasks** that PROGRAM_A can process sequentially.
- You will also be provided with **column names and data types** of the user's dataframe to assist in task creation.
- Ensure that each task is **self-contained, clearly defined, and executable by PROGRAM_A without ambiguity.**

### Instructions for Output Format:
Your response should be structured as follows:

**Task 1:**
  - **Description:** <A precise instruction that PROGRAM_A can execute directly>

**Task 2:**
  - **Description:** <A precise instruction that PROGRAM_A can execute directly>

**Task 3:**  
  - **Description:** <A precise instruction that PROGRAM_A can execute directly>

*(Continue this pattern as needed.)*

- **Include all relevant details** in each task to ensure clarity.
- If a task depends on a previous task’s result, specify the dependency clearly.
- **Do not omit important contextual information** that PROGRAM_A may need.

---

### User Input Details:
- **UserQuery:**  
{user_query}  

- **DataFrame Information:**  
{df_info}  

Use this information to ensure the tasks are well-formed and directly usable by PROGRAM_A.  
"""


select_tool_prompt = """I've got a dataframe with the following columns and corresponding data type:
{df_info}
On this dataframe, I want to: {task} 
I also have a bunch of analytical tools and their descriptions in hand. I want you to identify the most appropriate tool to perform this task, based on the description of each tool. Output only the exact name of that tool, do NOT output any other information or extra explanation on why you chose the tool.
Output nothing but the name of that tool.
If the task needs any type of machine learning support tools (not available yet), just terminate and output "".
Here is the list of tool names and their descriptions:
{tools}
"""

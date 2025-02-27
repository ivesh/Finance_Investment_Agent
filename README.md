
# Comprehensive Stock Analysis and News Platform

## Project Overview
This project aims to provide a versatile and comprehensive platform for investors, analysts, and anyone interested in understanding the performance and outlook of publicly traded companies across various global markets. Unlike the initial focus on NVIDIA Corporation (NVDA), the project has now been expanded to cover a wider range of markets, including the United States, Europe, China, Germany, France, and India.

The key objective of this platform is to empower users with the necessary tools and insights to make informed investment decisions. By offering a seamless experience for exploring and analyzing stocks, the project caters to a diverse audience seeking to gain a deeper understanding of the financial markets and the companies that shape them.

## Key Features

1. **Market and Stock Selection**:
   Users will be able to select the country they are interested in from a dropdown menu. Based on the chosen country, the tool will present a list of available major stock markets. Once a market is selected, users can then choose the specific stock they wish to analyze.

2. **Analyst Recommendations**:
   For the selected stock, the tool will retrieve and display the latest analyst recommendations, including the breakdown of "Strong Buy", "Buy", "Hold", "Sell", and "Strong Sell" ratings over different time periods. This provides valuable insight into the current market sentiment surrounding the stock.

3. **Competitor Analysis**:
   In addition to the target stock, the tool will also provide information on the stock's key competitors within the same market. This allows users to compare the performance and analyst sentiments across similar companies, offering a more comprehensive view of the stock's positioning and potential.

4. **Latest News**:
   The platform will gather and present the most recent news articles and events related to the selected stock and its competitors. By staying informed about the latest developments, users can better anticipate how these factors may impact the stocks they are interested in.

5. **Financial Data Analysis**:
   The tool will offer in-depth analysis of the selected stock's financial performance, including metrics such as revenue, cost, profit margin trends, and other relevant financial data. Intuitive data visualizations, such as charts and graphs, will be used to help users better understand the stock's financial health and outlook.

6. **Streamlit-based Interface**:
   The platform will be accessible through a user-friendly Streamlit web application, providing a seamless and interactive experience for exploring the stock analysis features. This ensures the tool is accessible and easy to use for both novice and experienced users.

## Installation and Setup

To set up the project, please follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ivesh/Finance_Investment_Agent.git
   ```

2. **Install Python and Poetry**:
   Ensure that you have Python 3.10 installed on your system. Then, install Poetry, a dependency management tool for Python, by following the [official Poetry installation guide](https://python-poetry.org/docs/).

3. **Create a Virtual Environment from vs code from the project folder**:
   ```bash
   cd Finance_Investment
   poetry shell
   ```
   This will create a new virtual environment and install the project's dependencies.

4. **Set up Environment Variables**:
   The project uses environment variables to store sensitive information, such as API keys. Create a `.env` file in the project root directory and add the required variables.

5. **Run the Application**:
   ```bash
   poetry run streamlit run app.py
   ```
   This will launch the Streamlit-based web application in your default web browser.

## Technical Details

The project leverages the following key technologies and libraries:

- **Python**: The primary programming language used for the project.
- **Streamlit**: A Python library for building interactive web applications.
- **Groq**: A deep learning-based language model used for various tasks, such as web scraping and data processing.
- **OpenAIChat**: An alternative language model that can be used in place of Groq.
- **DuckDuckGo**: A web search tool used to gather the latest news and information.
- **YFinanceTools**: A library for retrieving financial data, including stock prices, analyst recommendations, and company information.

The project follows a modular architecture, with separate components for web agents, finance agents, and an overall agent team. This design allows for easy extensibility and the incorporation of additional features or data sources in the future.

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your branch to your forked repository.
5. Submit a pull request to the original repository, explaining the changes you've made.

Please ensure that your contributions adhere to the project's coding standards and guidelines.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

I would like to acknowledge the following resources that has contributed to the development of this project:

- The [Anthropic](https://www.anthropic.com/) ,[OpenAI](),[Google],[Meta],[Microsoft] team for creating the powerful language models and tools used in this project.
- The open-source community for developing the libraries and frameworks utilized in this project, such as Streamlit, Groq, and YFinanceTools.
- [Phil Taboada](https://github.com/philtaboada) for providing the initial project structure and guidance.

If you have any questions or feedback, please don't hesitate to reach out. We're excited to collaborate and improve this project further.

---
# Developing Guidelines with Branch
A comprehensive guide for team members to collaborate on this project.

---

## **Understanding the Original and Cloned Repository**

### What Is the Original Repository?
The **original repository** is the main project repository hosted on GitHub, owned by the project maintainer or organization. In this guide, the original repository is:
```
https://github.com/ivesh/Finance_Investment_Agent
```
This is the **source of truth** where all approved changes will eventually be merged.

### What Is a Cloned Repository?
A **cloned repository** is a local copy of the original repository on your computer. Each team member clones the original repository to their machine to work on it locally. 

### Important Notes:
1. **You cannot directly edit the original repository** unless:
   - You are working locally on a cloned repository and pushing your changes.
   - You have been granted write access to the original repository.
2. **Changes are merged into the original repository through pull requests.**

---

## Sections in This Guide

1. [Clone the Repository](#clone-the-repository)
2. [Verify Git Repository](#verify-git-repository)
3. [Re-Cloning the Repository](#re-cloning-the-repository)
4. [Open the Repository in VS Code](#open-the-repository-in-vs-code)
5. [Create a New Branch](#create-a-new-branch)
6. [Make Changes and Commit](#make-changes-and-commit)
7. [Push the Branch to GitHub](#push-the-branch-to-github)
8. [Create a Pull Request (PR)](#create-a-pull-request-pr)
9. [Sync Your Repository with the Original Repository](#sync-your-repository-with-the-original-repository)
10. [Additional Notes](#additional-notes)

---

## Clone the Repository

1. **Open a folder** of your choice and name it `project`.
2. Clone the original repository to your local machine:
   ```bash
   git clone https://github.com/ivesh/Finance_Investment_Agent
   ```

3. Navigate into the cloned directory:
   ```bash
   cd Finance_Investment
   ```

4. **Verify your Git setup**:
   ```bash
   git remote -v
   ```
   Expected Output:
   ```
   origin  https://github.com/ivesh/Finance_Investment_Agent.git (fetch)
   origin  https://github.com/ivesh/Finance_Investment_Agent.git (push)
   ```
   This confirms your cloned repository is connected to the original repository.

---

## Verify Git Repository

1. Run the following command to confirm the directory is a Git repository:
   ```bash
   git status
   ```
2. If the output shows:
   ```
   fatal: not a git repository (or any of the parent directories): .git
   ```
   This means the `.git` folder is missing. Follow the **Re-Cloning the Repository** steps below.

---

## Re-Cloning the Repository

1. Navigate to the parent directory:
   ```bash
   cd ..
   ```

2. Remove the problematic folder:
   ```bash
   rmdir /s /q Challenge_1
   ```

3. Re-clone the repository:
   ```bash
   git clone https://github.com/ivesh/Finance_Investment_Agent
   ```

4. Navigate into the cloned directory:
   ```bash
   cd Finance_Investment
   ```

5. Confirm the repository is set up correctly:
   ```bash
   git status
   ```

---

## Open the Repository in VS Code

1. Open the cloned repository in VS Code:
   ```bash
   code .
   ```

2. Verify:
   - Check the bottom-left corner of VS Code. You should see the branch name (e.g., `main` or `feature/checking_features_built`).

---

## Create a New Branch

1. To work on a new feature or task, create and switch to a new branch:
   ```bash
   git checkout -b feature/your-branch-name
   ```

2. Push the branch to the remote repository:
   ```bash
   git push origin feature/your-branch-name
   ```

---

## Make Changes and Commit

1. **Make changes** to project files using VS Code.
2. Check the status of your changes:
   ```bash
   git status
   ```

3. Stage the changes:
   ```bash
   git add .
   ```

4. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Added feature: user authentication"
   ```

---

## Push the Branch to GitHub

Push your changes to your feature branch:
```bash
git push origin feature/your-branch-name
```

---

## Create a Pull Request (PR)

1. Go to the **original repository** on GitHub.
2. Navigate to the **Pull Requests** tab and select **New Pull Request**.
3. Select:
   - **Base branch**: `main` (original repository)
   - **Compare branch**: Your feature branch
4. Add a **Title** and **Description** for the PR.
5. Submit the pull request for review.

---

## Sync Your Repository with the Original Repository

To ensure your local repository stays up-to-date with the latest changes in the original repository:

1. Add the original repository as an **upstream remote**:
   ```bash
   git remote add upstream https://github.com/ivesh/Finance_Investment_Agent
   ```

2. Fetch the latest changes from the original repository:
   ```bash
   git fetch upstream
   ```

3. Merge updates from the original repository into your local `main` branch:
   ```bash
   git checkout main
   git merge upstream/main
   ```

4. Push the updated `main` branch to your fork:
   ```bash
   git push origin main
   ```

---

## Additional Notes

### Distinction Between Local, Forked, and Original Repositories
- **Local Repository**: Your Git clone on your computer.
- **Original Repository**: The main repository on GitHub (source of truth).
- **Remote Repository**: A GitHub-hosted repository you cloned or forked.

---

By adding these steps and clarifying the relationship between the original and cloned repositories, your team will better understand the process. Let me know if further adjustments are needed!
 

## Install Poetry using the developer guide-
Reference Links:
poetry: https://python-poetry.org/docs/pyproject/ 
reinstall poetry if error faced: https://stackoverflow.com/questions/70064449/how-to-force-reinstall-poetry-environment-from-scratch

**Observation:** We need to check which version of python is running in our system if it is python 3.9
then go to add/remove programs in control panel search for python delete all python versions and install the required one in this case python 3.10 was installed in the pc after removing 3.9.
**Solution:** Install python 3.10 and then install poetry using the developer guide.
**enviroment creation**: There is less flexibility in creating python environment in poetry however there is a higher flexibility if anaconda is used to create environment. eg: conda create -p myenv python==3.10 but the project in this case has to be set up with requirements.txt and setup.py for requirements and package management where the same thing can be avoided in poetry.


1. To check the python version
```bash
python --version
```
2. To install the required python version go the official python website and download the python version required make sure to check the python version by typing the above command as the virtual env created in poetry will be equal to the system python version.
3. Install Poetry by using the below command install pipx if not present in the system.
```bash 
pipx install poetry(force install again)
```
4. Check poetry is accurately installed using the command below
```bash
poetry --version
```
5. To check the base python and virtualenv version
poetry env info
6. To create virtual environment
```bash
poetry shell
```
7. To install packages
```bash
 poetry install --no-root
 ```
8. To add dependencies in poetry 
```bash
poetry add phidata
```  
9. Update the python packages
```bash
poetry update
```
10. Run Your Python File: Once the virtual environment is activated, you can run your Python file using the python command:
```bash
python your_file.py
```
11. Alternatively, if you prefer not to activate the virtual environment, you can run the Python file directly using Poetry's run command:
```bash
poetry run python your_script.py
```
- Install the required packages using poetry install
- Run the crew using poetry run main.py
## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)


## Screenshots of Streamlit app usage and project structure.

---------------------------------------------
- **Loading Environment**  
  - `load_dotenv()` is called to load environment variables (e.g., any API keys). This ensures that any credentials or configuration variables are available to the agents at runtime.

- **Defining the Web Agent**  
  1. **Provider/Model**: Uses `Groq(id="llama-3.3-70b-versatile")` as its underlying language model.  
  2. **Identifier**: Named `"Web Agent"` and assigned a unique `agent_id="web-agent"` and `session_id="session_web"`.  
  3. **Behavioral Settings**:  
     - `add_chat_history_to_messages=True` so previous conversation context is included.  
     - `show_tool_calls=True` so any sub-tool usage is shown in the output.  
     - `markdown=True` for formatted text (tables, bullet points, etc.).  
     - `debug_mode=False` to suppress low-level debug logs.  
  4. **Instructions**: `["Always include sources"]` guides how this agent should format answers (it must cite sources).  
  5. **Tools**: `[DuckDuckGo()]` for web searches/news retrieval. The agent can call this tool to find online information.

- **Defining the Finance Agent**  
  1. **Provider/Model**: Also uses `Groq(id="llama-3.3-70b-versatile")`.  
  2. **Identifier**: Named `"Finance Agent"`, with `agent_id="finance-agent"` and `session_id="session_finance"`.  
  3. **Behavioral Settings**:  
     - `add_chat_history_to_messages=True` for context.  
     - `show_tool_calls=True` and `markdown=True`.  
     - `debug_mode=False` to keep logs less verbose.  
  4. **Instructions**:  
     - `"Get financial data"`,  
     - `"Use tables to display data"`.  
    This tells the agent to fetch and present financial data in a tabular format.
  5. **Tools**: `[YFinanceTools(...)]` for stock data, analyst recommendations, company info, and historical prices. This agent can call those YFinance utilities to get real-time or historical financial data.

- **Creating the Team Agent**  
  1. **Provider/Model**: `Groq(id="llama-3.3-70b-versatile")` once again.  
  2. **Identifier**: Named `"Agent Team"`, with `agent_id="agent-team"` and `session_id="session_team"`.  
  3. **Behavioral Settings**:  
     - `add_chat_history_to_messages=True`,  
     - `show_tool_calls=True` (so the final output shows when tasks are transferred to sub-agents),  
     - `markdown=True` for rich formatting,  
     - `debug_mode=False` to limit logs.  
  4. **Instructions**:  
     - `"Always include sources"`,  
     - `"Use tables to display data"`.  
    These instructions apply on top of the sub‐agents’ instructions and shape the final combined response.
  5. **Team**: `[web_agent, finance_agent]`. The team agent can delegate tasks to either sub‐agent (Web Agent or Finance Agent), depending on what’s needed—like fetching news from DuckDuckGo or financial data from YFinance.

- **Running the Code**  
  1. The `if __name__ == "__main__": ...` block calls `agent_team.print_response(...)` with the prompt:  
     > "Summarize analyst recommendations and share the latest news for NVDA"  
  2. **Orchestration**:  
     - The “Team” agent receives the prompt.  
     - It dispatches relevant sub-requests:  
       - **Web Agent** to retrieve and summarize recent NVDA news.  
       - **Finance Agent** to get analyst recommendations, stock history, or other financial metrics.  
     - It merges and formats the results (including sources, tables, etc.) following the instructions.  
  3. **Streaming Output**: `stream=True` prints the response tokens as they are generated, showing the multi-step process (e.g., “Running: transfer_task_to_finance_agent(...)”).

- **Overall Goal & Benefit**  
  - This structure allows multiple specialized “agents” (one for web searching/news, another for financial data) to collaborate under a single “team” agent.  
  - The final output is an **integrated** summary for stock investors: up-to-date analyst recommendations, recent news headlines (with sources), and relevant financial tables.  
  - By using `show_tool_calls=True`, the user can see how each sub-agent is invoked, providing transparency into the steps taken to gather and compile the information.


------------------------------------------




![Prompt Usage Example: Summarize analyst recommendations and share the lates NVDA news]

![alt text](image-2.png)


(![alt text](image.png))

![alt text](image-1.png)

Response output from the streamit run app.py(from within the poetry environment):

App Interface Streamlit is running in the localhost :

![alt text](image-3.png)

Stock choosen: AAPL

┏━ Message ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                                                                        ┃
┃ Tell me about the latest news and its competitors price history of this stock and compare the analyst recommendation for  the stock    ┃
┃ and it's competitors.                                                                                                                  ┃
┃                                                                                                                                        ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
┏━ Response (211.0s) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                                                                        ┃
┃ Running:                                                                                                                               ┃
┃                                                                                                                                        ┃
┃  • transfer_task_to_web_agent(task_description=Provide the latest news for the stock, expected_output=A list of the latest news for    ┃
┃    the stock, additional_information=Use duckduckgo_news to get the latest news for the stock)                                         ┃
┃  • transfer_task_to_finance_agent(task_description=Get the current stock price and the price history of the stock and its competitors, ┃
┃    expected_output=A table comparing the current stock price and the price history of the stock and its competitors,                   ┃
┃    additional_information=...)                                                                                                         ┃
┃  • transfer_task_to_finance_agent(task_description=Get the analyst recommendations for the stock and its competitors,                  ┃
┃    expected_output=A table comparing the analyst recommendations for the stock and its competitors, additional_information=Use         ┃
┃    get_analyst_recommendations to get the analyst recommendations for the stock and its competitors)                                   ┃
┃                                                                                                                                        ┃
┃ Here is the latest news for the stock:                                                                                                 ┃
┃                                                                                                                                        ┃
┃  • Stock Market Today: Dow set to fall but Nasdaq to rise after tech index's biggest dive of the year; Nvidia to bounce; Fed meeting   ┃
┃    to begin. - MarketWatch                                                                                                             ┃
┃  • Nvidia's plunge a 'difficult lesson' for investors betting on single-stock ETFs - MSN                                               ┃
┃  • DeepSeek Panic Live Updates: Trump Calls AI Development 'Positive' Despite Tech Stock Plunge - Forbes on MSN.com                    ┃
┃  • Stock Market Today: Nasdaq, S&P 500 down sharply as DeepSeek fears spark $1.1 trillion tech rout, Nvidia drops 14%; Dow turns       ┃
┃    positive - MarketWatch                                                                                                              ┃
┃  • The AI-stock wipeout lays bare 2 risks investors have been happy to ignore - until now - Markets Insider on MSN.com                 ┃
┃                                                                                                                                        ┃
┃ These news articles provide updates on the current stock market situation, including the impact of DeepSeek on the tech industry and   ┃
┃ the performance of major stocks like Nvidia. They offer insights into the potential risks and opportunities in the market and how      ┃
┃ investors are responding to the latest developments.                                                                                   ┃
┃                                                                                                                                        ┃
┃ Here is the table comparing the current stock price and the price history of the stock and its competitors:                            ┃
┃                                                                                                                                        ┃
┃                                                                                                                                        ┃
┃   Company                                                Current Stock Price   Price History                                           ┃
┃  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ┃
┃   AAPL                                                   $229.86               {"1735534800000":{"Open":252.2299957275,"High":253.5…   ┃
┃                                                                                Splits":0.0}}                                           ┃
┃   GOOG                                                   $193.77               {"1735534800000":{"Open":190.8650054932,"High":193.7…   ┃
┃                                                                                Splits":0.0}}                                           ┃
┃   MSFT                                                   $434.56               {"1735534800000":{"Open":426.0599975586,"High":427.5…   ┃
┃                                                                                Splits":0.0}}                                           ┃
┃   Note: The current stock prices are based on the                                                                                      ┃
┃   latest available data and may not reflect the                                                                                        ┃
┃   current market price. The price history is a sample                                                                                  ┃
┃   of the historical data and may not reflect the                                                                                       ┃
┃   entire history of the stock.                                                                                                         ┃
┃                                                                                                                                        ┃
┃                                                                                                                                        ┃
┃ Here is the table comparing the analyst recommendations for the stock and its competitors:                                             ┃
┃                                                                                                                                        ┃
┃                                                                                                                                        ┃
┃   Company                                                                               Strong Buy   Buy   Hold   Sell   Strong Sell   ┃
┃  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ┃
┃   AAPL                                                                                  8            23    11     2      2             ┃
┃   GOOG                                                                                  14           35    12     0      0             ┃
┃   MSFT                                                                                  14           39    5      0      0             ┃
┃   Note: The analyst recommendations are based on the latest available data and may                                                     ┃
┃   not reflect the current market sentiments. The numbers represent the number of                                                       ┃
┃   analysts with each recommendation.                                                                                                   ┃
┃                                                                                                                                        ┃
┃                                                                                                                                        ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛